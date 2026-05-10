import math
import matplotlib.pyplot as plt

# Board
board = [' '] * 9

# Node counters
minimax_nodes = []
alphabeta_nodes = []


# ---------------- CHECK WIN ----------------
def check_winner(b):
    win_positions = [(0,1,2),(3,4,5),(6,7,8),
                     (0,3,6),(1,4,7),(2,5,8),
                     (0,4,8),(2,4,6)]
    
    for (i,j,k) in win_positions:
        if b[i] == b[j] == b[k] and b[i] != ' ':
            return b[i]
    
    if ' ' not in b:
        return 'Draw'
    
    return None


# ---------------- MINIMAX ----------------
def minimax(b, isMax, counter):
    counter[0] += 1
    
    result = check_winner(b)
    if result == 'O':
        return 1
    elif result == 'X':
        return -1
    elif result == 'Draw':
        return 0

    if isMax:
        best = -math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'O'
                best = max(best, minimax(b, False, counter))
                b[i] = ' '
        return best
    else:
        best = math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'X'
                best = min(best, minimax(b, True, counter))
                b[i] = ' '
        return best


# ---------------- ALPHA-BETA ----------------
def alphabeta(b, isMax, alpha, beta, counter):
    counter[0] += 1
    
    result = check_winner(b)
    if result == 'O':
        return 1
    elif result == 'X':
        return -1
    elif result == 'Draw':
        return 0

    if isMax:
        best = -math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'O'
                val = alphabeta(b, False, alpha, beta, counter)
                b[i] = ' '
                best = max(best, val)
                alpha = max(alpha, best)
                if beta <= alpha:
                    break
        return best
    else:
        best = math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'X'
                val = alphabeta(b, True, alpha, beta, counter)
                b[i] = ' '
                best = min(best, val)
                beta = min(beta, best)
                if beta <= alpha:
                    break
        return best


# ---------------- BEST MOVE ----------------
def best_move_minimax():
    counter = [0]
    best_val = -math.inf
    move = -1

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            val = minimax(board, False, counter)
            board[i] = ' '
            if val > best_val:
                best_val = val
                move = i

    minimax_nodes.append(counter[0])
    return move


def best_move_alphabeta():
    counter = [0]
    best_val = -math.inf
    move = -1

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            val = alphabeta(board, False, -math.inf, math.inf, counter)
            board[i] = ' '
            if val > best_val:
                best_val = val
                move = i

    alphabeta_nodes.append(counter[0])
    return move


# ---------------- PLAY GAME ----------------
def play_game():
    turn = 0
    while True:
        print(board[0:3])
        print(board[3:6])
        print(board[6:9])
        print()

        if turn % 2 == 0:
            pos = int(input("Enter position (0-8): "))
            if board[pos] == ' ':
                board[pos] = 'X'
        else:
            print("AI Move...")
            best_move_minimax()      # run minimax
            move = best_move_alphabeta()  # run alphabeta
            board[move] = 'O'

        result = check_winner(board)
        if result:
            print("Result:", result)
            break

        turn += 1


# ---------------- RUN ----------------
play_game()

# ---------------- GRAPH ----------------
moves = list(range(1, len(minimax_nodes)+1))

plt.bar(moves, minimax_nodes, label="Minimax")
plt.bar(moves, alphabeta_nodes, label="Alpha-Beta")

plt.xlabel("Moves")
plt.ylabel("Nodes Explored")
plt.title("Minimax vs Alpha-Beta")
plt.legend()

plt.show()