import unittest


def convert(input):
    return "I"


class RomanConverterTest(unittest.TestCase):

    # def test_convert2k18(self):
    #     self.assertEqual('MMXVIII', convert(2018), "The number 2018 should be converted to MMXVIII")

    def test_convert_test1(self):
        self.assertEqual('I', convert(1), "Number 1 in roman numnerals (I)")
    def test_convert_testX(self):
        self.assertEqual('X', convert(10), "Number 10 in roman numnerals (X)")


if __name__ == "__main__":
    unittest.main()
