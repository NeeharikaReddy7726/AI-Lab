import time

# BASIC
def isSafe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def basic_solve(board, row, n, nodes):
    nodes[0] += 1

    if row == n:
        return 1

    count = 0
    for col in range(n):
        if isSafe(board, row, col):
            board[row] = col
            count += basic_solve(board, row + 1, n, nodes)
            board[row] = -1
    return count


# OPTIMIZED
def get_domains(board, n):
    domains = {}
    for row in range(n):
        if board[row] == -1:
            possible = []
            for col in range(n):
                safe = True
                for r in range(n):
                    if board[r] != -1:
                        if board[r] == col or abs(board[r] - col) == abs(r - row):
                            safe = False
                            break
                if safe:
                    possible.append(col)
            domains[row] = possible
    return domains

def select_row(domains):
    return min(domains, key=lambda r: len(domains[r]))

def solve_optimized(board, n, nodes):
    nodes[0] += 1

    domains = get_domains(board, n)

    if not domains:
        return 1

    row = select_row(domains)
    count = 0

    for col in domains[row]:
        board[row] = col
        count += solve_optimized(board, n, nodes)
        board[row] = -1

    return count


# MAIN
n = int(input("Enter N: "))

# BASIC
board = [-1]*n
nodes_basic = [0]

start = time.time()
solutions_basic = basic_solve(board, 0, n, nodes_basic)
end = time.time()

time_basic = end - start


# OPTIMIZED
board = [-1]*n
nodes_opt = [0]

start = time.time()
solutions_opt = solve_optimized(board, n, nodes_opt)
end = time.time()

time_opt = end - start


print("\n--- COMPARISON ---")
print("N =", n)

print("\nBasic Backtracking:")
print("Solutions:", solutions_basic)
print("Nodes Explored:", nodes_basic[0])
print("Time:", time_basic)

print("\nOptimized Backtracking:")
print("Solutions:", solutions_opt)
print("Nodes Explored:", nodes_opt[0])
print("Time:", time_opt)