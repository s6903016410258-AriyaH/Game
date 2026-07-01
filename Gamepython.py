import tkinter as tk
from tkinter import messagebox

score = 0
time_left = 10
game_running = False


def start_game():
    global score, time_left, game_running

    score = 0
    time_left = 10
    game_running = True

    score_label.config(text=f"Score: {score}")
    timer_label.config(text=f"Time: {time_left}")

    click_button.config(state="normal")
    start_button.config(state="disabled")

    countdown()


def click():
    global score

    if game_running:
        score += 1
        score_label.config(text=f"Score: {score}")


def countdown():
    global time_left, game_running

    if time_left > 0:
        timer_label.config(text=f"Time: {time_left}")
        time_left -= 1
        root.after(1000, countdown)
    else:
        game_running = False
        click_button.config(state="disabled")
        messagebox.showinfo("Game Over", f"Your final score is {score}!")
        start_button.config(state="normal")


# ---------------- GUI ----------------

root = tk.Tk()
root.title("Click the Button Game")
root.geometry("400x300")
root.resizable(False, False)

title = tk.Label(root, text="🎮 Click the Button Game",
                 font=("Arial", 20, "bold"))
title.pack(pady=10)

score_label = tk.Label(root, text="Score: 0",
                       font=("Arial", 16))
score_label.pack()

timer_label = tk.Label(root, text="Time: 10",
                       font=("Arial", 16))
timer_label.pack(pady=5)

click_button = tk.Button(
    root,
    text="CLICK ME!",
    font=("Arial", 18),
    width=12,
    height=2,
    bg="dodgerblue",
    fg="white",
    state="disabled",
    command=click
)
click_button.pack(pady=20)

start_button = tk.Button(
    root,
    text="Start Game",
    font=("Arial", 14),
    width=12,
    command=start_game
)
start_button.pack()

root.mainloop()