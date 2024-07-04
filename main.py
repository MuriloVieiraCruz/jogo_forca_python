import tkinter as tk
from tkinter import messagebox

class JogoDaVelha:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Velha")

        self.current_player = 'X'
        self.board = [['' for _ in range(3)] for _ in range(3)]

        self.buttons = [[None]*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text='', font=('Arial', 20), width=8, height=4,
                                               command=lambda row=i, col=j: self.clicked(row, col))
                self.buttons[i][j].grid(row=i, column=j)

        self.restart_button = tk.Button(self.root, text='Reiniciar', font=('Arial', 14), command=self.restart)
        self.restart_button.grid(row=3, columnspan=3)

    def clicked(self, row, col):
        if self.board[row][col] == '' and not self.check_winner():
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Fim do jogo", f"Jogador {self.current_player} venceu!")
                self.restart()
            elif self.check_draw():
                messagebox.showinfo("Fim do jogo", "Empate!")
                self.restart()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != '':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != '':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            return True
        return False

    def check_draw(self):
        for row in self.board:
            for cell in row:
                if cell == '':
                    return False
        return True

    def restart(self):
        self.current_player = 'X'
        self.board = [['' for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text='')

if __name__ == "__main__":
    root = tk.Tk()
    jogo = JogoDaVelha(root)
    root.mainloop()