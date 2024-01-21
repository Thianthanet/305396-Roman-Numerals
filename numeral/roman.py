# numeral/roman.py

def to_roman(arabic_num):
    if not 0 < arabic_num < 4000:
        raise ValueError("Input must be between 1 and 3999")

    roman_numeral = ""
    roman_numerals = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I"
    }

    for value, numeral in sorted(roman_numerals.items(), key=lambda x: x[0], reverse=True):
        while arabic_num >= value:
            roman_numeral += numeral
            arabic_num -= value

    return roman_numeral
