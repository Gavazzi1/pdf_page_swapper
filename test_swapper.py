import unittest
from PyPDF2 import PdfFileReader, PdfFileWriter
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from swapper import swap_pages


# returns a reader for the contents of a given writer
def writer2reader(wrtr):
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


class MyTestCase(unittest.TestCase):
    def test_swapper_1page(self):
        test_rdr = make_test_pdf(1)
        wrtr = swap_pages(test_rdr)

        rdr = writer2reader(wrtr)
        self.assertEqual(rdr.numPages, 4)
        self.assertEqual(rdr.getPage(0).extractText(), '0\n')
        self.assertFalse('/Contents' in rdr.getPage(1))
        self.assertFalse('/Contents' in rdr.getPage(2))
        self.assertFalse('/Contents' in rdr.getPage(3))

    def test_swapper_2page(self):
        test_rdr = make_test_pdf(2)
        wrtr = swap_pages(test_rdr)

        rdr = writer2reader(wrtr)
        self.assertEqual(rdr.numPages, 4)
        self.assertEqual(rdr.getPage(0).extractText(), '0\n')
        self.assertFalse('/Contents' in rdr.getPage(1))
        self.assertEqual(rdr.getPage(2).extractText(), '1\n')
        self.assertFalse('/Contents' in rdr.getPage(3))

    def test_swapper_3page(self):
        test_rdr = make_test_pdf(3)
        wrtr = swap_pages(test_rdr)

        rdr = writer2reader(wrtr)
        self.assertEqual(rdr.numPages, 4)
        self.assertEqual(rdr.getPage(0).extractText(), '0\n')
        self.assertEqual(rdr.getPage(1).extractText(), '2\n')
        self.assertEqual(rdr.getPage(2).extractText(), '1\n')
        self.assertFalse('/Contents' in rdr.getPage(3))

    def test_swapper_4page(self):
        test_rdr = make_test_pdf(4)
        wrtr = swap_pages(test_rdr)

        rdr = writer2reader(wrtr)
        self.assertEqual(rdr.numPages, 4)
        self.assertEqual(rdr.getPage(0).extractText(), '0\n')
        self.assertEqual(rdr.getPage(1).extractText(), '2\n')
        self.assertEqual(rdr.getPage(2).extractText(), '1\n')
        self.assertEqual(rdr.getPage(3).extractText(), '3\n')

    def test_swapper_5page(self):
        test_rdr = make_test_pdf(5)
        wrtr = swap_pages(test_rdr)

        rdr = writer2reader(wrtr)
        self.assertEqual(rdr.numPages, 8)
        self.assertEqual(rdr.getPage(0).extractText(), '0\n')
        self.assertEqual(rdr.getPage(1).extractText(), '2\n')
        self.assertEqual(rdr.getPage(2).extractText(), '1\n')
        self.assertEqual(rdr.getPage(3).extractText(), '3\n')
        self.assertEqual(rdr.getPage(4).extractText(), '4\n')
        self.assertFalse('/Contents' in rdr.getPage(5))
        self.assertFalse('/Contents' in rdr.getPage(6))
        self.assertFalse('/Contents' in rdr.getPage(7))

    def test_swapper_6page(self):
        test_rdr = make_test_pdf(6)
        wrtr = swap_pages(test_rdr)

        rdr = writer2reader(wrtr)
        self.assertEqual(rdr.numPages, 8)
        self.assertEqual(rdr.getPage(0).extractText(), '0\n')
        self.assertEqual(rdr.getPage(1).extractText(), '2\n')
        self.assertEqual(rdr.getPage(2).extractText(), '1\n')
        self.assertEqual(rdr.getPage(3).extractText(), '3\n')
        self.assertEqual(rdr.getPage(4).extractText(), '4\n')
        self.assertFalse('/Contents' in rdr.getPage(5))
        self.assertEqual(rdr.getPage(6).extractText(), '5\n')
        self.assertFalse('/Contents' in rdr.getPage(7))

    def test_swapper_7page(self):
        test_rdr = make_test_pdf(7)
        wrtr = swap_pages(test_rdr)

        rdr = writer2reader(wrtr)
        self.assertEqual(rdr.numPages, 8)
        self.assertEqual(rdr.getPage(0).extractText(), '0\n')
        self.assertEqual(rdr.getPage(1).extractText(), '2\n')
        self.assertEqual(rdr.getPage(2).extractText(), '1\n')
        self.assertEqual(rdr.getPage(3).extractText(), '3\n')
        self.assertEqual(rdr.getPage(4).extractText(), '4\n')
        self.assertEqual(rdr.getPage(5).extractText(), '6\n')
        self.assertEqual(rdr.getPage(6).extractText(), '5\n')
        self.assertFalse('/Contents' in rdr.getPage(7))

    def test_swapper_8page(self):
        test_rdr = make_test_pdf(8)
        wrtr = swap_pages(test_rdr)

        rdr = writer2reader(wrtr)
        self.assertEqual(rdr.numPages, 8)
        self.assertEqual(rdr.getPage(0).extractText(), '0\n')
        self.assertEqual(rdr.getPage(1).extractText(), '2\n')
        self.assertEqual(rdr.getPage(2).extractText(), '1\n')
        self.assertEqual(rdr.getPage(3).extractText(), '3\n')
        self.assertEqual(rdr.getPage(4).extractText(), '4\n')
        self.assertEqual(rdr.getPage(5).extractText(), '6\n')
        self.assertEqual(rdr.getPage(6).extractText(), '5\n')
        self.assertEqual(rdr.getPage(7).extractText(), '7\n')


if __name__ == '__main__':
    unittest.main()
