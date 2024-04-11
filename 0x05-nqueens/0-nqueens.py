#!/usr/bin/python3
"""
N-Queens Problem Solution
"""

import sys


def backtrack(row, n, cols, pos_diag, neg_diag, board):
    """
    Backtracking function to find solutions to the N-Queens problem.

    Args:
        row (int): Current row being processed.
        n (int): Size of the board and the number of queens.
        cols (set): Set of columns occupied by queens.
        pos_diag (set): Set of positive diagonals occupied by queens.
        neg_diag (set): Set of negative diagonals occupied by queens.
        board (list): Representation of the board.

    Returns:
        None. Prints solutions to the console.
    """
    if row == n:
        solution = []
        for row_index in range(len(board)):
            for col_index in range(len(board[row_index])):
                if board[row_index][col_index] == 1:
                    solution.append([row_index, col_index])
        print(solution)
        return

    for col in range(n):
        if col in cols or (row + col) in pos_diag or (row - col) in neg_diag:
            continue

        cols.add(col)
        pos_diag.add(row + col)
        neg_diag.add(row - col)
        board[row][col] = 1

        backtrack(row + 1, n, cols, pos_diag, neg_diag, board)

        cols.remove(col)
        pos_diag.remove(row + col)
        neg_diag.remove(row - col)
        board[row][col] = 0


def nqueens(n):
    """
    Solves the N-Queens problem and prints solutions.

    Args:
        n (int): Size of the board and the number of queens.

    Returns:
        None. Prints solutions to the console.
    """
    cols = set()
    pos_diag = set()
    neg_diag = set()
    board = [[0] * n for _ in range(n)]

    backtrack(0, n, cols, pos_diag, neg_diag, board)


if __name__ == "__main__":
    args = sys.argv
    if len(args) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(args[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueens(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
