"""Test cases for Roman numerals"""

#Standard library

#3rd Part library
import pytest

# Project library
from numerals.roman import to_roman

def test_calling_function():
    """Call a roman numeral function."""
    

class ToRomanTest:
    """Test cases for to_roman()."""
    @pytest.mark.parametrize(
    "arabic_num, roman_num",
    [
        (1, "I"),
        (5, "V")
    ]
    )
    def test_base_case(self, arabic_num, roman_num):
        """Test roman"""
        # Arrange
        # Act
        result = to_roman(arabic_num)

        # Assert
        assert result == roman_num
        
        @pytest.mark.parametrize(
            "arabic_num, roman_num",
            [
                (2, "II"),
                (6, "VI")
            ]
        )
        def test_add_case(self, arabic_num, roman_num):
            """Test roman"""
            # Arrange
            # Act
            result = to_roman(arabic_num)

            # Assert
            assert result == roman_num
            
        @pytest.mark.parametrize(
            "arabic_num, roman_num",
            [
            (4, "IV"),
            (9, "IX")
            ]
        )
        def test_sub_case(self, arabic_num, roman_num):
            """Test roman"""
            # Arrange
            # Act
            result = to_roman(arabic_num)

            # Assert
            assert result == roman_num