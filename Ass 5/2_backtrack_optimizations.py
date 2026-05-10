#2. Optimizations for Backtracking
def optimized_nqueens(N, mode):
    cols = set()
    diag1 = set()   # r - c
    diag2 = set()   # r + c

    board = [["." for _ in range(N)] for _ in range(N)]

    solutions = []
    backtracks = 0
    nodes = 0

    def solve(row):
        nonlocal backtracks, nodes

        nodes += 1

        if row == N:
            solutions.append([" ".join(r) for r in board])
            return mode == "single"

        for col in range(N):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue
            # place queen
            board[row][col] = "Q"
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)

            if solve(row + 1):
                return True

            # backtrack
            board[row][col] = "."
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)
            backtracks += 1

        return False

    solve(0)

    return solutions, backtracks, nodes


N = int(input("Enter N: "))
mode = input("Mode (single/all): ").strip()

solutions, backtracks, nodes = optimized_nqueens(N, mode)

print("\nBoard configuration(s):\n")
for sol in solutions:
    for row in sol:
        print(row)
    print()

print("Total solutions:", len(solutions))
print("Backtracks:", backtracks)
print("Nodes explored:", nodes)
