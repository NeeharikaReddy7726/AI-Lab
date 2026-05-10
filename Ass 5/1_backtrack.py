N= int(input())
mode= input().strip()
board = [["." for _ in range(N)] for _ in range(N)]
solutions = []
backtracks = 0

def issafe(board, row, col, N):
    #column check
    for i in range(row):
        if board[i][col] == "Q":
            return False
    #check left diagonal
    i, j= row-1, col-1
    while i >= 0 and j >= 0:
        if board[i][j]== "Q":
            return False
        i-=1
        j-=1
    #check right diagonal
    i, j= row-1, col+1
    while i >= 0 and j < N:
        if board[i][j]== "Q":
            return False
        i-=1
        j+=1
    return True

def solve(row):
    global backtracks

    if row == N:
        solutions.append([" ".join(r) for r in board])
        return True if mode == "single" else False

    for col in range(N):
        if issafe(board, row, col, N):
            board[row][col] = "Q"

            if solve(row + 1):
                return True

            board[row][col] = "."
            backtracks += 1

    return False

solve(0)

for sol in solutions:
    for row in sol:
        print(row)
    print()

print("Total solutions:", len(solutions))
print("Backtracks:", backtracks)
