# numeral/roman.py

def to_roman(arabic_num):
    if not 0 < arabic_num < 4000:
        raise ValueError("Input must be between 1 and 3999")

    roman_numerals = [
        ("M", 1000),
        ("CM", 900),
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
    for roman, value in roman_numerals:
        while arabic_num >= value:
            result += roman
            arabic_num -= value

    return result
