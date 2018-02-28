import unittest


def convert(input):
    return


class RomanConverterTest(unittest.TestCase):

    def test_convert2k18(self):
        self.assertEqual('MMXVIII', convert(2018), "The number 2018 should be converted to MMXVIII")


if __name__ == "__main__":
    unittest.main()
