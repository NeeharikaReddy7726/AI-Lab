import time

def isSafe(board, row, col, n):
    #column
    for i in range(row):
        if board[i] == col:
            return False

    # left diagonal
    for i in range(row):
        if abs(board[i] - col) == abs(i - row):
            return False

    return True


# Backtracking
def solve(board, row, n, solutions, mode, backtracks):
    if row == n:
        solutions.append(board[:])
        return True if mode == "single" else False

    found = False

    for col in range(n):
        if isSafe(board, row, col, n):
            board[row] = col

            result = solve(board, row + 1, n, solutions, mode, backtracks)

            if result:  # if single solution found
                return True
        else:
            backtracks[0] += 1

    return False


def printBoard(solution, n):
    for i in range(n):
        row = ['.'] * n
        row[solution[i]] = 'Q'
        print(" ".join(row))
    print()


n = int(input("Enter N: "))
mode = input("Mode (single/all): ")

board = [-1] * n
solutions = []
backtracks = [0]

start = time.time()

solve(board, 0, n, solutions, mode, backtracks)

end = time.time()

print("\nSolutions:\n")
for sol in solutions:
    printBoard(sol, n)

print("Total Solutions:", len(solutions))
print("Backtracks:", backtracks[0])
print("Execution Time:", end - start, "seconds")