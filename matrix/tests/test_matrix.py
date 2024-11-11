"""Test suite to ensure that each function words correctly."""

from matrix import __version__

from matrix import main

# Reference for the use of pytest.approx:
# https://docs.pytest.org/en/6.2.x/reference.html#pytest-approx


def test_version():
    """Confirm that the version of the program is correct."""
    assert __version__ == "0.1.0"


def test_count_negative_numbers_in_matrix():
    """Confirm that an exhaustive function can detect a prime number."""
    # Test case inspired by the example at:
    # https://towardsdatascience.com/python-string-manipulation-for-data-scientists-in-2021-c5b9526347f4
    matrix = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
    negative_number_count = main.count_negatives_in_matrix(matrix)
    assert negative_number_count == 8


def test_convert_matrix_text_to_grid():
    """Ensure that it is possible to convert text of matrix to a grid."""
    matrix_text = (
        "100,19,9,9\n"
        "10,9,8,7\n"
        "6,4,2,-1\n"
        "4,2,0,-1\n"
        "3,0,-1,-2\n"
        "-1,-1,-2,-5"
    )
    matrix = main.construct_matrix(matrix_text)
    assert len(matrix) == 6
    assert len(matrix[0]) == 4
    assert matrix[0][0] == 100
