import sys
import time

def isSafe(board, row, col):
    for i in range(row):
        # same column
        if board[i] == col:
            return False

        # diagonal
        if abs(board[i] - col) == abs(i - row):
            return False

    return True

def solve(row):
    global backtracks, mode, firstFound

    if row == N:
        solutions.append(board.copy())

        if mode == "single":
            firstFound = True
        return

    for col in range(N):
        if isSafe(board, row, col):
            board[row] = col
            solve(row + 1)

            if mode == "single" and firstFound:
                return

            board[row] = -1
            backtracks += 1

def boardToString(config):
    lines = []
    for r in range(N):
        rowStr = ""
        for c in range(N):
            if config[r] == c:
                rowStr += "Q "
            else:
                rowStr += ". "
        lines.append(rowStr.strip())
    return "\n".join(lines)

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, "r") as f:
    N = int(f.readline().strip())
    mode = f.readline().strip()

board = [-1] * N
solutions = []
backtracks = 0
firstFound = False

start = time.time()

solve(0)

end = time.time()

with open(output_file, "w") as f:
    for idx, sol in enumerate(solutions, 1):
        f.write(f"Solution {idx}:\n")
        f.write(boardToString(sol))
        f.write("\n\n")

    f.write(f"Total solutions: {len(solutions)}\n")
    f.write(f"Backtracks: {backtracks}\n")
    f.write(f"Execution time: {end - start:.6f} seconds\n")
