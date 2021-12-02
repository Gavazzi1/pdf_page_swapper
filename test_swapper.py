import unittest
from swapper import swap_pages
from util import writer2reader, make_test_pdf


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
