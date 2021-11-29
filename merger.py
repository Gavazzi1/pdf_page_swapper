from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2.pdf import PageObject


# Given a reader for a given pdf, every 2 pages vertically
# Assume input pdf has page count divisible by 2 because it comes from the swapper function
def merge_pdf(rdr: PdfFileReader, do_print=True):
    wrtr = PdfFileWriter()
    for i in range(0, rdr.numPages, 2):
        if do_print:
            print('Merging {} of {}'.format(int(i/2)+1, int(rdr.numPages/2)))

        pg1 = rdr.getPage(i)
        pg2 = rdr.getPage(i + 1)

        # TODO can we make the mergeTranslatedPage and mergePage calls faster? they're the most time consuming by a lot
        newpg = PageObject.createBlankPage(None, pg1.mediaBox.getWidth(), pg1.mediaBox.getHeight() * 2)
        newpg.mergeTranslatedPage(pg1, 0, pg1.mediaBox.getHeight())
        newpg.mergePage(pg2)
        wrtr.addPage(newpg)

    return wrtr

