def to_roman(arabic_num):
    roman_numeral = ""
    roman_mapping = {
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

    for value, numeral in roman_mapping.items():
        while arabic_num >= value:
            roman_numeral += numeral
            arabic_num -= value

    return roman_numeral