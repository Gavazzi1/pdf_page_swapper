import io
from PyPDF2 import PdfFileReader, PdfFileWriter


# returns a reader for the contents of a given writer
def writer2reader(wrtr: PdfFileWriter):
    final = io.BytesIO()
    wrtr.write(final)
    rdr = PdfFileReader(final)
    return rdr
