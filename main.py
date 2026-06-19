import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("400x500")
root.resizable(False, False)

current_player = "X"
board = [""] * 9

x_score = 0
o_score = 0
draw_score = 0

def update_score():
    score_label.config(
        text=f"X: {x_score}    O: {o_score}    Draws: {draw_score}"
    )

def check_winner():
    wins = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]

    for a, b, c in wins:
        if board[a] == board[b] == board[c] != "":
            return board[a]

    if "" not in board:
        return "Draw"

    return None

def button_click(index):
    global current_player, x_score, o_score, draw_score

    if board[index] == "":
        board[index] = current_player

        color = "blue" if current_player == "X" else "red"

        buttons[index].config(
            text=current_player,
            fg=color
        )

        result = check_winner()

        if result:
            if result == "X":
                x_score += 1
                update_score()
                messagebox.showinfo("Winner", "Player X Wins!")

            elif result == "O":
                o_score += 1
                update_score()
                messagebox.showinfo("Winner", "Player O Wins!")

            else:
                draw_score += 1
                update_score()
                messagebox.showinfo("Draw", "Match Draw!")

            reset_board()
            return

        current_player = "O" if current_player == "X" else "X"
        turn_label.config(text=f"Turn: {current_player}")

def reset_board():
    global current_player, board

    board = [""] * 9
    current_player = "X"

    for btn in buttons:
        btn.config(text="", bg="white")

    turn_label.config(text="Turn: X")

def reset_all():
    global x_score, o_score, draw_score

    x_score = 0
    o_score = 0
    draw_score = 0

    update_score()
    reset_board()

title = tk.Label(
    root,
    text="TIC TAC TOE",
    font=("Arial", 24, "bold")
)
title.pack(pady=10)

score_label = tk.Label(
    root,
    text="X: 0    O: 0    Draws: 0",
    font=("Arial", 14, "bold")
)
score_label.pack()

turn_label = tk.Label(
    root,
    text="Turn: X",
    font=("Arial", 16)
)
turn_label.pack(pady=10)

frame = tk.Frame(root)
frame.pack()

buttons = []

for i in range(9):
    btn = tk.Button(
        frame,
        text="",
        font=("Arial", 28, "bold"),
        width=4,
        height=2,
        bg="white",
        command=lambda i=i: button_click(i)
    )

    btn.grid(row=i//3, column=i%3, padx=3, pady=3)
    buttons.append(btn)

tk.Button(
    root,
    text="New Match",
    font=("Arial", 12, "bold"),
    command=reset_board
).pack(pady=8)

tk.Button(
    root,
    text="Reset Scores",
    font=("Arial", 12, "bold"),
    command=reset_all
).pack()

update_score()
root.mainloop()