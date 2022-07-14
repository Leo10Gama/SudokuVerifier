"""Main driver that will run Sudoku verification algorithm"""

from verifier import verify_sudoku


def main():
    """Driver method for primary functionality."""
    # Prompt for Sudoku
    puzzle = input("Enter Sudoku puzzle (top left, read right):\n")
    # Run verifier
    print("Verifying...")
    res = verify_sudoku(puzzle)
    # Print result
    print("Valid sudoku!" if res else "Invalid sudoku. Try again!")


if __name__ == "__main__":
    main()
