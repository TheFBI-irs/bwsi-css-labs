"""
tests_1cd.py

This module contains unit tests for the max_subarray_sum function defined in lab_1c.py
and the two_sum function defined in lab_1d.py.
"""

import pytest
from labs.lab_1.lab_1c import max_subarray_sum
from labs.lab_1.lab_1d import two_sum


# ===== Tests for max_subarray_sum =====

def test_max_subarray_mixed():
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6  # Standard LeetCode example

def test_max_subarray_all_positive():
    assert max_subarray_sum([1, 2, 3, 4, 5]) == 15  # Entire array is the max subarray

def test_max_subarray_all_negative():
    assert max_subarray_sum([-3, -1, -2]) == -1  # Least negative number

def test_max_subarray_single_element():
    assert max_subarray_sum([5]) == 5             # Single positive element
    assert max_subarray_sum([-5]) == -5           # Single negative element

def test_max_subarray_empty():
    with pytest.raises(ValueError, match="Input list cannot be empty."):
        max_subarray_sum([])                      # Empty list edge case

def test_max_subarray_with_zeros():
    assert max_subarray_sum([0, -1, 0, 2, 0]) == 2  # Zeros in the array


# ===== Tests for two_sum =====

def test_two_sum_basic():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]  # Standard LeetCode example

def test_two_sum_negative_numbers():
    assert two_sum([-3, 4, 3, 90], 0) == [0, 2]  # Negative and positive

def test_two_sum_duplicates():
    assert two_sum([3, 3], 6) == [0, 1]           # Same number used at different indices

def test_two_sum_larger_array():
    assert two_sum([1, 2, 3, 4, 5], 9) == [3, 4] # Larger array

def test_two_sum_no_solution():
    assert two_sum([1, 2, 3], 100) == []          # No solution returns empty list

def test_two_sum_with_zero():
    assert two_sum([0, 4, 3, 0], 0) == [0, 3]    # Target is zero


if __name__ == "__main__":
    pytest.main()
