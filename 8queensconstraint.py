# Backtracking Search for 8-Queens Problem

N = 8

def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col:
            return False

        if abs(board[i] - col) == abs(i - row):
            return False

    return True


def solve(board, row):
    if row == N:
        return True

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col

            if solve(board, row + 1):
                return True

            board[row] = -1

    return False


board = [-1] * N

if solve(board, 0):
    print("8-Queens Solution:")
    for row in range(N):
        print(" ".join("Q" if board[row] == col else "."
                       for col in range(N)))
else:
    print("No solution")