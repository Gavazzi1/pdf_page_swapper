from PyPDF2 import PdfFileReader
import sys
from swapper import swap_pages
from util import writer2reader
from merger import merge_pdf

if __name__ == '__main__':
    # arg parsing
    if len(sys.argv) < 3:
        sys.exit('main.py <input pdf fn> <output pdf fn>')
    else:
        in_fn = sys.argv[1]
        out_fn = sys.argv[2]

    # read file and swap pages
    input_pdf = PdfFileReader(in_fn)

    print('swapping pages')
    pdf_writer = swap_pages(input_pdf)

    # get new reader for new pdf and merge every 2 pages
    newrdr = writer2reader(pdf_writer)

    print('merging pages')
    merged_writer = merge_pdf(newrdr)

    # write pdf
    with open(out_fn, 'wb') as output_file:
        print('writing pdf')
        merged_writer.write(output_file)
