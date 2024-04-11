#!/usr/bin/python3
"""
Solution to the N-queens problem
"""
import sys


def is_safe(row, col, n, cols, positive_diagonal, negative_diagonal):
    """
    Check if placing a queen at (row, col) is safe
    """
    if col in cols or (row + col) in positive_diagonal or (row - col) in negative_diagonal:
        return False
    return True


def place_queen(row, n, cols, positive_diagonal, negative_diagonal, board, solutions):
    """
    Place queens recursively
    """
    if row == n:
        queens = []
        for r in range(n):
            for c in range(n):
                if board[r][c] == 1:
                    queens.append([r, c])
        solutions.append(queens)
        return

    for col in range(n):
        if is_safe(row, col, n, cols, positive_diagonal, negative_diagonal):
            cols.add(col)
            positive_diagonal.add(row + col)
            negative_diagonal.add(row - col)
            board[row][col] = 1

            place_queen(row + 1, n, cols, positive_diagonal, negative_diagonal, board, solutions)

            cols.remove(col)
            positive_diagonal.remove(row + col)
            negative_diagonal.remove(row - col)
            board[row][col] = 0


def nqueens(n):
    """
    Solution to the N-queens problem
    Args:
        n (int): Number of queens. Must be >= 4.
    Returns:
        List of solutions, where each solution is a list of queen positions.
    """
    if n < 4:
        raise ValueError("N must be at least 4")

    cols = set()
    positive_diagonal = set()
    negative_diagonal = set()
    board = [[0] * n for _ in range(n)]
    solutions = []

    place_queen(0, n, cols, positive_diagonal, negative_diagonal, board, solutions)

    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        n = int(sys.argv[1])
        solutions = nqueens(n)
        for solution in solutions:
            for queen in solution:
                print(f"{queen[0]},{queen[1]}", end=" ")
            print()
    except ValueError:
        print("N must be a number")
        sys.exit(1)
