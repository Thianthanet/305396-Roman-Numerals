"""Test cases for Roman numerals"""

#Standard library

#3rd Part library
import pytest

# Project library
from numerals.roman import to_roman

@pytest.mark.parametrize(
    "arabic_num, roman_num",
    [
        (1, "I"),
        (5, "V"),
        (10, "X"),
        (50, "L"),
        (100, "C"),
        (1000, "M"),
        
        # Addition case
        (2, "II"),
        (3, "III"),
        (6, "VI"),
        
        # Subtraction
        (4, "IV"),
        (9, "IX"),
        (3888, "MMMDCCCLXXXVIII")
    ]
)
def test_to_roman(arabic_num, roman_num):
    """Test roman"""
    # Arrange

    # Act
    result = to_roman(arabic_num)

    # Assert
    assert result == roman_num