import tkinter as tk
import random

# Word list
word_list = ['python', 'hangman', 'challenge', 'programming', 'streamlit', 'developer', 'keyboard']
word = random.choice(word_list)
guessed_letters = set()
attempts_left = 6

# Initialize display
current_display = ['_' for _ in word]

# GUI setup
root = tk.Tk()
root.title("Hangman Game")
root.geometry("400x300")
root.resizable(False, False)

title_label = tk.Label(root, text="🎯 Hangman Game", font=('Arial', 18))
title_label.pack(pady=10)

word_label = tk.Label(root, text=" ".join(current_display), font=('Arial', 24))
word_label.pack(pady=10)

message_label = tk.Label(root, text="", font=('Arial', 12))
message_label.pack()

attempts_label = tk.Label(root, text=f"Attempts left: {attempts_left}", font=('Arial', 12))
attempts_label.pack(pady=5)

guess_entry = tk.Entry(root, font=('Arial', 14))
guess_entry.pack(pady=5)

def update_display():
    word_label.config(text=" ".join(current_display))
    attempts_label.config(text=f"Attempts left: {attempts_left}")

def check_guess():
    global attempts_left
    guess = guess_entry.get().lower()
    guess_entry.delete(0, tk.END)

    if len(guess) != 1 or not guess.isalpha():
        message_label.config(text="❗ Please enter a single letter.")
        return

    if guess in guessed_letters:
        message_label.config(text="🔁 Already guessed.")
        return

    guessed_letters.add(guess)

    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                current_display[i] = guess
        message_label.config(text="✅ Correct guess!")
    else:
        attempts_left -= 1
        message_label.config(text="❌ Wrong guess!")

    update_display()

    if "_" not in current_display:
        message_label.config(text=f"🎉 You won! Word: {word}")
        guess_button.config(state="disabled")
    elif attempts_left == 0:
        word_label.config(text=word)
        message_label.config(text=f"💀 Game Over! Word: {word}")
        guess_button.config(state="disabled")

guess_button = tk.Button(root, text="Guess", command=check_guess, font=('Arial', 12))
guess_button.pack(pady=5)

# Start GUI loop
update_display()
root.mainloop()
