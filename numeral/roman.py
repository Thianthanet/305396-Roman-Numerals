"""Create Function"""

import unittest

def to_roman(num):
    if not 0 < num < 4000:
        raise ValueError("Input must be between 1 and 3888")

    roman_numerals = [
        ("M", 1000),
        ("CM", 900),
        ("DCCC", 800)
        ("D", 500),
        ("CD", 400),
        ("C", 100),
        ("XC", 90),
        ("L", 50),
        ("XL", 40),
        ("X", 10),
        ("IX", 9),
        ("V", 5),
        ("IV", 4),
        ("I", 1)
    ]

    result = ""
    for numeral, value in roman_numerals:
        while num >= value:
            result += numeral
            num -= value

    return result

class TestIntToRoman(unittest.TestCase):
    def test_positive_values(self):
        self.assertEqual(to_roman(1), 'I')
        self.assertEqual(to_roman(3888), 'MMMDCCLXXXVIII')
        self.assertEqual(to_roman(2022), 'MMXX')

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            to_roman(0)

        with self.assertRaises(ValueError):
            to_roman(4000)

if __name__ == "__main__":
    unittest.main()