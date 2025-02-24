import tkinter as tk
import numpy as np

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe with Minimax AI")
        self.board = np.full((3, 3), '')
        self.current_player = 'X'
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()
    
    def create_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.window, text='', font=('Arial', 20), height=2, width=5,
                                               command=lambda row=i, col=j: self.on_click(row, col))
                self.buttons[i][j].grid(row=i, column=j)
    
    def on_click(self, row, col):
        if self.board[row, col] == '' and self.current_player == 'X':
            self.board[row, col] = 'X'
            self.buttons[row][col].config(text='X')
            if self.check_winner('X'):
                self.display_winner('X')
                return
            self.current_player = 'O'
            self.ai_move()
    
    def ai_move(self):
        best_score = -float('inf')
        best_move = None
        for i in range(3):
            for j in range(3):
                if self.board[i, j] == '':
                    self.board[i, j] = 'O'
                    score = self.minimax(False)
                    self.board[i, j] = ''
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        
        if best_move:
            row, col = best_move
            self.board[row, col] = 'O'
            self.buttons[row][col].config(text='O')
            if self.check_winner('O'):
                self.display_winner('O')
                return
            self.current_player = 'X'
    
    def minimax(self, is_maximizing):
        if self.check_winner('O'):
            return 1
        if self.check_winner('X'):
            return -1
        if '' not in self.board:
            return 0
        
        if is_maximizing:
            best_score = -float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i, j] == '':
                        self.board[i, j] = 'O'
                        score = self.minimax(False)
                        self.board[i, j] = ''
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i, j] == '':
                        self.board[i, j] = 'X'
                        score = self.minimax(True)
                        self.board[i, j] = ''
                        best_score = min(score, best_score)
            return best_score
    
    def check_winner(self, player):
        for i in range(3):
            if all(self.board[i, :] == player) or all(self.board[:, i] == player):
                return True
        if all([self.board[i, i] == player for i in range(3)]) or all([self.board[i, 2 - i] == player for i in range(3)]):
            return True
        return False
    
    def display_winner(self, winner):
        win_label = tk.Label(self.window, text=f"{winner} wins!", font=('Arial', 20))
        win_label.grid(row=3, column=0, columnspan=3)
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(state=tk.DISABLED)
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()