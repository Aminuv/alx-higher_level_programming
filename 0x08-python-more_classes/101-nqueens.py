#!/usr/bin/python3
"""the N-queens puzzle solved."""

import sys


def init_board(n):
    """Initializing an `n`x`n` sized chessboard with 0's."""
    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]
    return (board)


def board_deepcopy(board):
    """Return the deepcopy of chessboard."""
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return (board)


def get_solution(board):
    """Return a list of lists representation in the board."""
    solution = []
    for q in range(len(board)):
        for ch in range(len(board)):
            if board[q][ch] == "Q":
                solution.append([q, ch])
                break
    return (solution)


def xout(board, row, col):
    """an X spots on a chessboard."""

    for ch in range(col + 1, len(board)):
        board[row][ch] = "x"

    for ch in range(col - 1, -1, -1):
        board[row][ch] = "x"

    for q in range(row + 1, len(board)):
        board[q][col] = "x"

    for q in range(row - 1, -1, -1):
        board[q][col] = "x"

    ch = col + 1
    for q in range(row + 1, len(board)):
        if ch >= len(board):
            break
        board[q][ch] = "x"
        ch += 1

    ch = col - 1
    for q in range(row - 1, -1, -1):
        if ch < 0:
            break
        board[q][ch]
        ch -= 1

    ch = col + 1
    for q in range(row - 1, -1, -1):
        if ch >= len(board):
            break
        board[q][ch] = "x"
        ch += 1

    ch = col - 1
    for q in range(row + 1, len(board)):
        if ch < 0:
            break
        board[q][ch] = "x"
        ch -= 1


def recursive_solve(board, row, queens, solutions):
    """Recursively solve for  N-queens puzzle."""

    if queens == len(board):
        solutions.append(get_solution(board))
        return (solutions)

    for ch in range(len(board)):
        if board[row][ch] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][ch] = "Q"
            xout(tmp_board, row, ch)
            solutions = recursive_solve(tmp_board, row + 1,
                                        queens + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)
