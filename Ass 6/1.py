import math

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.human = 'X'
        self.ai = 'O'
        self.nodes_explored = 0

    def print_board(self):
        for i in range(0, 9, 3):
            print(f" {self.board[i]} | {self.board[i+1]} | {self.board[i+2]} ")
            if i < 6:
                print("-----------")
        print()

    def is_winner(self, player):
        win_states = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8], # Cols
            [0, 4, 8], [2, 4, 6]             # Diagonals
        ]    
        return any(all(self.board[i] == player for i in combo) for combo in win_states)

    def is_board_full(self):
        return ' ' not in self.board

    def get_utility(self):
        if self.is_winner('X'): return 1
        if self.is_winner('O'): return -1
        return 0

    def minimax(self, is_maximizing):
        self.nodes_explored += 1
        
        # Terminal states
        if self.is_winner('X'): return 1
        if self.is_winner('O'): return -1
        if self.is_board_full(): return 0

        if is_maximizing:
            best_score = -math.inf
            for i in range(9):
                if self.board[i] == ' ':
                    self.board[i] = 'X'
                    score = self.minimax(False)
                    self.board[i] = ' '
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = math.inf
            for i in range(9):
                if self.board[i] == ' ':
                    self.board[i] = 'O'
                    score = self.minimax(True)
                    self.board[i] = ' '
                    best_score = min(score, best_score)
            return best_score

    def get_best_move(self):
        self.nodes_explored = 0
        best_val = math.inf
        move = -1
        
        for i in range(9):
            if self.board[i] == ' ':
                self.board[i] = 'O'
                move_val = self.minimax(True)
                self.board[i] = ' '
                if move_val < best_val:
                    best_val = move_val
                    move = i
        return move, best_val

    def play(self):
        print("Tic-Tac-Toe: Human (X) vs AI (O)")
        self.print_board()

        while True:
            # Human Turn
            try:
                move = int(input("Enter move (0-8): "))
                if self.board[move] != ' ':
                    print("Occupied! Try again.")
                    continue
            except (ValueError, IndexError):
                print("Invalid input. Use 0-8.")
                continue

            self.board[move] = 'X'
            self.print_board()

            if self.is_winner('X') or self.is_board_full():
                break

            # AI Turn
            print("AI is thinking...")
            ai_move, minimax_val = self.get_best_move()
            self.board[ai_move] = 'O'
            
            print(f"AI chose index {ai_move}")
            print(f"Minimax Value: {minimax_val}")
            print(f"Nodes Explored: {self.nodes_explored}")
            self.print_board()

            if self.is_winner('O') or self.is_board_full():
                break

        if self.is_winner('X'): print("X wins!")
        elif self.is_winner('O'): print("O wins!")
        else: print("It's a draw!")

if __name__ == "__main__":
    TicTacToe().play()