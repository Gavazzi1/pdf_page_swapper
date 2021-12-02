from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2.pdf import PageObject
from concurrent.futures import ThreadPoolExecutor, wait
from io import BytesIO


# Given a reader for a given pdf, every 2 pages vertically
# Assume input pdf has page count divisible by 2 because it comes from the swapper function
def merge_pdf(rdr: PdfFileReader, do_print=True):
    wrtr = PdfFileWriter()
    for i in range(0, rdr.numPages, 2):
        if do_print:
            print('Merging {} of {}'.format(int(i/2)+1, int(rdr.numPages/2)))

        pg1 = rdr.getPage(i)
        pg2 = rdr.getPage(i + 1)

        newpg = PageObject.createBlankPage(None, pg1.mediaBox.getWidth(), pg1.mediaBox.getHeight() * 2)
        newpg.mergeTranslatedPage(pg1, 0, pg1.mediaBox.getHeight())
        newpg.mergePage(pg2)

        wrtr.addPage(newpg)

    return wrtr


"""
Ok so i tried making this parallel but it runs slower no matter what I try
mergeTranslatedPage and mergePage run much slower in threads and so it ultimately runs slower overall
I'm keeping the code here in case I have an epiphany, but for now it's useless
"""


def merge2(rdr_in, startidx, bufidx, buf, do_print):
    rdr = PdfFileReader(BytesIO(rdr_in.stream.getbuffer()))

    if do_print:
        print('Merging {} of {}'.format(int(startidx / 2) + 1, int(rdr.numPages / 2)))

    pg1 = rdr.getPage(startidx)
    pg2 = rdr.getPage(startidx + 1)

    newpg = PageObject.createBlankPage(None, pg1.mediaBox.getWidth(), pg1.mediaBox.getHeight() * 2)
    newpg.mergeTranslatedPage(pg1, 0, pg1.mediaBox.getHeight())
    newpg.mergePage(pg2)

    buf[bufidx] = newpg


def merge_pdf_parallel(rdr: PdfFileReader, do_print=True):
    # guaranteed if input comes from swapper, but necessary still
    assert(rdr.numPages % 2 == 0)

    MAXTHREADS = 4
    buf = [None] * MAXTHREADS
    wrtr = PdfFileWriter()
    num_full_bufs = int(rdr.numPages/(MAXTHREADS*2))

    for i in range(num_full_bufs):
        with ThreadPoolExecutor(max_workers=MAXTHREADS) as executor:
            futures = set()
            for j in range(MAXTHREADS):
                futures.add(executor.submit(merge2, rdr, i * MAXTHREADS * 2 + j * 2, j, buf, do_print))
            wait(futures)

            for pg in buf:
                wrtr.addPage(pg)

    with ThreadPoolExecutor(max_workers=MAXTHREADS) as executor:
        futures = set()
        rest = int((rdr.numPages % (MAXTHREADS * 2)) / 2)
        for j in range(rest):
            futures.add(executor.submit(merge2, rdr, num_full_bufs * MAXTHREADS * 2 + j * 2, j, buf, do_print))
        wait(futures)

        for j in range(rest):
            pg = buf[j]
            wrtr.addPage(pg)

    return wrtr

