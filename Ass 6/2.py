import math

class AlphaBetaTicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.nodes_mm = 0
        self.nodes_ab = 0
        self.alpha_cutoffs = 0
        self.beta_cutoffs = 0

    def print_board(self):
        for i in range(0, 9, 3):
            print(f" {self.board[i]} | {self.board[i+1]} | {self.board[i+2]} ")
            if i < 6:
                print("-----------")
        print()

    def is_winner(self, player):
        win_states = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        return any(all(self.board[i] == player for i in combo) for combo in win_states)

    def is_board_full(self):
        return ' ' not in self.board

    # --- ORIGINAL MINIMAX (For Benchmarking Only) ---
    def minimax(self, is_maximizing):
        self.nodes_mm += 1
        if self.is_winner('X'): return 1
        if self.is_winner('O'): return -1
        if self.is_board_full(): return 0

        if is_maximizing:
            best_score = -math.inf
            for i in range(9):
                if self.board[i] == ' ':
                    self.board[i] = 'X'
                    best_score = max(best_score, self.minimax(False))
                    self.board[i] = ' '
            return best_score
        else:
            best_score = math.inf
            for i in range(9):
                if self.board[i] == ' ':
                    self.board[i] = 'O'
                    best_score = min(best_score, self.minimax(True))
                    self.board[i] = ' '
            return best_score

    # --- NEW: ALPHA-BETA PRUNING ---
    def alpha_beta(self, is_maximizing, alpha, beta):
        self.nodes_ab += 1
        
        if self.is_winner('X'): return 1
        if self.is_winner('O'): return -1
        if self.is_board_full(): return 0

        if is_maximizing:
            best_score = -math.inf
            for i in range(9):
                if self.board[i] == ' ':
                    self.board[i] = 'X'
                    score = self.alpha_beta(False, alpha, beta)
                    self.board[i] = ' '
                    best_score = max(score, best_score)
                    alpha = max(alpha, best_score)
                    
                    # Beta Cutoff
                    if best_score >= beta:
                        self.beta_cutoffs += 1
                        break 
            return best_score
        else:
            best_score = math.inf
            for i in range(9):
                if self.board[i] == ' ':
                    self.board[i] = 'O'
                    score = self.alpha_beta(True, alpha, beta)
                    self.board[i] = ' '
                    best_score = min(score, best_score)
                    beta = min(beta, best_score)
                    
                    # Alpha Cutoff
                    if best_score <= alpha:
                        self.alpha_cutoffs += 1
                        break
            return best_score

    def get_best_move(self):
        self.nodes_mm = 0
        self.nodes_ab = 0
        self.alpha_cutoffs = 0
        self.beta_cutoffs = 0
        
        best_val = math.inf
        move = -1
        
        # Benchmarking standard Minimax
        for i in range(9):
            if self.board[i] == ' ':
                self.board[i] = 'O'
                self.minimax(True)
                self.board[i] = ' '

        # Running Alpha-Beta for the actual decision
        alpha = -math.inf
        beta = math.inf
        
        for i in range(9):
            if self.board[i] == ' ':
                self.board[i] = 'O'
                move_val = self.alpha_beta(True, alpha, beta)
                self.board[i] = ' '
                if move_val < best_val:
                    best_val = move_val
                    move = i
                beta = min(beta, best_val)
                
        return move, best_val

    def play(self):
        print("Alpha-Beta Tic-Tac-Toe: Human (X) vs AI (O)")
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
            print("AI is thinking...\n")
            ai_move, minimax_val = self.get_best_move()
            self.board[ai_move] = 'O'
            
            # Calculating percentage reduction
            if self.nodes_mm > 0:
                reduction = ((self.nodes_mm - self.nodes_ab) / self.nodes_mm) * 100
            else:
                reduction = 0
            
            # Reporting
            print(f"--- AI Move Report ---")
            print(f"Chosen Index: {ai_move} (Value: {minimax_val})")
            print(f"Nodes Explored (Plain Minimax): {self.nodes_mm:,}")
            print(f"Nodes Explored (Alpha-Beta):    {self.nodes_ab:,}")
            print(f"Efficiency Gain:                {reduction:.2f}% reduction")
            print(f"Alpha ($\alpha$) Cutoffs (Minimizer stopped early): {self.alpha_cutoffs:,}")
            print(f"Beta ($\beta$) Cutoffs (Maximizer stopped early):  {self.beta_cutoffs:,}")
            print(f"----------------------\n")
            
            self.print_board()

            if self.is_winner('O') or self.is_board_full():
                break

        if self.is_winner('X'): print("X wins!")
        elif self.is_winner('O'): print("O wins!")
        else: print("It's a draw!")

if __name__ == "__main__":
    AlphaBetaTicTacToe().play()