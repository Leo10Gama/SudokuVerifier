"""Algorithm for verifying that a given Sudoku puzzle is valid."""

def verify_sudoku(puzzle: str) -> bool:
    """Verify that a given puzzle is a valid Sudoku solution.
    
    Parameters
    ----------
    puzzle: str
        An 81-character string consisting entirely of numeric characters,
        representative of a Sudoku puzzle as read from the top-left corner
        to the bottom-right corner.

    Returns
    -------
    bool
        Whether or not the given string is a valid Sudoku solution
    """
    puzzle = str(puzzle)
    if len(puzzle) != 81 or not puzzle.isnumeric() or not puzzle.replace('0', 'a').isnumeric():
        # Puzzle is >81 characters; doesn't contain only numbers; has invalid number (0)
        return False

    # Verify rows
    for row_index in range(9):
        row = puzzle[row_index * 9:(row_index * 9) + 9]
        if not _verify_section(row):
            return False

    # Verify columns
    for col_index in range(9):
        col = puzzle[col_index::9]
        if not _verify_section(col):
            return False

    # Verify boxes
    for box_index in [0, 3, 6, 27, 30, 33, 54, 57, 60]:  # NOTE: box_index = upper left corner of 3x3 box
        box = puzzle[box_index:box_index+3] + puzzle[box_index+9: box_index+9+3] + puzzle[box_index+18:box_index+18+3]
        if not _verify_section(box):
            return False

    return True


def _verify_section(chunk: str) -> bool:
    """Verifies a given chunk of 9 numbers is valid in a Sudoku row, column, or box.
    
    Parameters
    ----------
    chunk: str
        A 9-character string representative of a Sudoku row, column, or box.

    Returns
    -------
    bool
        Whether or not all 9 characters are unique numbers in range(1,9).
    """
    if len(chunk) != 9:
        raise ValueError(f"Did not receive the expected 9 characters, and instead got '{chunk}'")

    seen = set()
    expected = set(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
    for num in chunk:
        seen.add(num)
    return seen == expected

    