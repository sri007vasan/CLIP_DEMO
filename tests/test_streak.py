import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Test that an empty list returns 0."""
    assert longest_positive_streak([]) == 0

def test_multiple_streaks():
    """Test that the longest streak is returned when there are multiple."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3
    assert longest_positive_streak([1, 2, 3, -5, 1, 2]) == 3
    assert longest_positive_streak([1, 2, -5, 1, 2, 3, 4]) == 4

def test_with_zeros():
    """Test that zeros break the streak."""
    assert longest_positive_streak([1, 2, 0, 3, 4, 5]) == 3

def test_with_negatives():
    """Test that negative numbers break the streak."""
    assert longest_positive_streak([1, 2, -3, 4, 5]) == 2

def test_all_positive():
    """Test a list with all positive numbers."""
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_all_non_positive():
    """Test a list with all non-positive numbers."""
    assert longest_positive_streak([-1, -2, 0, -5]) == 0

def test_single_element_list():
    """Test lists with a single element."""
    assert longest_positive_streak([1]) == 1
    assert longest_positive_streak([-1]) == 0
    assert longest_positive_streak([0]) == 0

def test_long_list():
    """Test with a longer list."""
    assert longest_positive_streak([1, 2, 3, -1, 5, 6, 7, 0, 4, 1, 2, 3, 4, 5, 6, -10, 1]) == 7