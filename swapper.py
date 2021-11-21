from PyPDF2 import PdfFileReader, PdfFileWriter


# Pads a given pdf to a multiple of 4 pages and, for every 4 pages in the pdf, swaps pages 2 and 3
# Returns a PdfFileWriter of the newly written pdf
def swap_pages(input_pdf: PdfFileReader):
    pdf_writer = PdfFileWriter()

    # loop over pdf in steps of 4 pages
    # loop body only executes if there is another group of 4 pages to handle
    pgn = 3
    while pgn < input_pdf.numPages:
        pdf_writer.addPage(input_pdf.getPage(pgn - 3))
        pdf_writer.addPage(input_pdf.getPage(pgn - 1))  # here's where the page swapping happens
        pdf_writer.addPage(input_pdf.getPage(pgn - 2))
        pdf_writer.addPage(input_pdf.getPage(pgn - 0))

        pgn += 4

    # if pdf has multiple of 4 pages, pgn - numPages == 3, which is the max possible distance
    # if pgn - numPages == 2, there is one more page past a multiple of 4 -- insert 3 empty pages
    # if pgn - numPages == 1, there are 2 more pages past a multiple of 4 -- insert 2 empty pages then swap 2 and 3
    # if pgn - numPages == 0, there are 3 more pages past a multiple of 4 -- insert 1 empty page then swap 2 and 3

    diff = pgn - input_pdf.numPages
    if diff == 2:
        pdf_writer.addPage(input_pdf.getPage(input_pdf.numPages - 1))  # add last page
        pdf_writer.addBlankPage()
        pdf_writer.addBlankPage()
        pdf_writer.addBlankPage()

    elif diff == 1:
        # insert blank page between last 2 pages so that they will be back to back on final printed copy
        pdf_writer.addPage(input_pdf.getPage(input_pdf.numPages - 2))
        pdf_writer.addBlankPage()
        pdf_writer.addPage(input_pdf.getPage(input_pdf.numPages - 1))
        pdf_writer.addBlankPage()

    elif diff == 0:
        # swap pages 2 and 3, then add a blank page
        pdf_writer.addPage(input_pdf.getPage(input_pdf.numPages - 3))
        pdf_writer.addPage(input_pdf.getPage(input_pdf.numPages - 1))
        pdf_writer.addPage(input_pdf.getPage(input_pdf.numPages - 2))
        pdf_writer.addBlankPage()

    return pdf_writer
