from PyPDF2 import PdfFileReader, PdfFileWriter
import sys
from swapper import swap_pages


if __name__ == '__main__':
    # arg parsing
    if len(sys.argv) < 3:
        sys.exit('main.py <input pdf fn> <output pdf fn>')
    else:
        in_fn = sys.argv[1]
        out_fn = sys.argv[2]

    # get reader and writer
    input_pdf = PdfFileReader(in_fn)
    pdf_writer = swap_pages(input_pdf, PdfFileWriter())

    with open(out_fn, 'wb') as output_file:
        pdf_writer.write(output_file)
