import io
from PyPDF2 import PdfFileReader, PdfFileWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


# returns a reader for the contents of a given writer
def writer2reader(wrtr: PdfFileWriter):
    final = io.BytesIO()
    wrtr.write(final)
    rdr = PdfFileReader(final)
    return rdr


# makes a pdf with "npages" pages, each of which has the text that is just the page number and a newline
# returns a reader to that pdf
def make_test_pdf(npages):
    writer = PdfFileWriter()

    # from https://stackoverflow.com/questions/1180115/add-text-to-existing-pdf-using-python
    for i in range(npages):
        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)
        can.drawString(10, 100, str(i))
        can.save()

        # move to the beginning of the StringIO buffer
        packet.seek(0)
        new_pdf = PdfFileReader(packet)
        writer.addPage(new_pdf.getPage(0))

    return writer2reader(writer)
