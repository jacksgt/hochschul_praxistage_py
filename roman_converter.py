import unittest


def convert(input):
    output = ""
    x = input // 10
    i = input % 10

    l = x // 5
    x = x % 5

    output = l * "L" + x * "X" + i * "I"
    return output


class RomanConverterTest(unittest.TestCase):

    # def test_convert2k18(self):
    #     self.assertEqual('MMXVIII', convert(2018), "The number 2018 should be converted to MMXVIII")

    def test_convert_test1(self):
        self.assertEqual('I', convert(1), "Number 1 in roman numnerals (I)")
    def test_convert_testX(self):
        self.assertEqual('X', convert(10), "Number 10 in roman numnerals (X)")
    def test_convert_test50(self):
        self.assertEqual('L', convert(50), "Number 50 in roman numerals (L)")
    def test_convert_test50(self):
        self.assertEqual('XL', convert(40), "Number 40 in roman numerals (XL)")



if __name__ == "__main__":
    unittest.main()
