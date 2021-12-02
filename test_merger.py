import unittest
from merger import merge_pdf
from util import writer2reader, make_test_pdf


class MyTestCase(unittest.TestCase):
    def test_merger_2(self):
        test_rdr = make_test_pdf(4)
        wrtr = merge_pdf(test_rdr, do_print=False)

        rdr = writer2reader(wrtr)
        self.assertEqual(rdr.numPages, 2)
        self.assertEqual(rdr.getPage(0).extractText(), '0\n1\n')
        self.assertEqual(rdr.getPage(1).extractText(), '2\n3\n')

    def test_merger_40(self):
        test_rdr = make_test_pdf(40)
        wrtr = merge_pdf(test_rdr, do_print=False)

        rdr = writer2reader(wrtr)
        self.assertEqual(rdr.numPages, 20)
        for i in range(19):
            self.assertEqual(rdr.getPage(i).extractText(), '{}\n{}\n'.format(i*2, i*2+1))


if __name__ == '__main__':
    unittest.main()
