"""Count the number of negative numbers in a sorted matrix."""

# TODO: Add all of the required imports for this project

# TODO: create a Typer object to support the command-line interface


def confirm_valid_file(file: Path) -> bool:
    # TODO: Add all of the required source code to confirm
    # that the file provided on the input is valid.
    # TODO: Make sure that the file is not None and
    # that the file exists on the file system


def construct_matrix(matrix_contents: str) -> List[List[int]]:
    """Construct a matrix of int values out of a string representation of the matrix."""
    # TODO: Make sure that you understand how this source code works!
    matrix = [
        [int(num) for num in line.split(",")] for line in matrix_contents.splitlines()
    ]
    return matrix


def print_matrix(matrix: List[List[int]]) -> None:
    """Display a matrix in the console in a formatted fashion."""
    # Use the tabulate package
    print(tabulate(matrix))


def count_negatives_in_matrix(matrix: List[List[int]]) -> int:
    # TODO: Count the number of negative values inside of the provided matrix
    # TODO: You may assume that each row and column of the matrix is
    # sorted on non-increasing order
    # TODO: Refer to the following web site for a further description of this function:
    # https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
    # TODO: Please remember that the aforementioned web site may not be configured
    # at first to display Python source code. Your solution must be in Python!


@cli.command()
def matrix(
    matrix_dir: Path = typer.Option(None),
    matrix_file: Path = typer.Option(None),
) -> None:
    matrix_file_fully_qualified = matrix_dir / matrix_file
    matrix_contents = ""
    # confirm that the file is valid and then perform computation
    if confirm_valid_file(matrix_file_fully_qualified):
        matrix_contents = matrix_file_fully_qualified.read_text()
        # TODO: create a console for rich text output
        # TODO: construct the matrix from the contents of the text file
        # TODO: display the contents of the matrix in a tabular format
        # TODO: count the number of negatives in the matrix
        # TODO: display the count of the negatives in the matrix
        # TODO: refer to the READEM for a description of what the
        # program's output should look like!
    else:
        print(
            f":person_shrugging: {matrix_file_fully_qualified} was not a valid matrix file"
        )
