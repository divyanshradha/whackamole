import tkinter as tk
import random
import time
import winsound

class WhackAMole:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Whack-a-Mole")
        self.score = 0
        self.high_score = self.load_high_score()
        self.score_label = tk.Label(self.root, text=f"Score: 0\nHigh Score: {self.high_score}", font=("Helvetica", 24))
        self.score_label.pack()
        self.time_label = tk.Label(self.root, text="Time: 20", font=("Helvetica", 24))
        self.time_label.pack()
        self.mole_button = None
        self.create_mole()
        self.countdown(20)
        self.root.mainloop()

    def load_high_score(self):
        try:
            with open("high_score.txt", "r") as f:
                return int(f.read())
        except FileNotFoundError:
            return 0

    def save_high_score(self):
        with open("high_score.txt", "w") as f:
            f.write(str(self.high_score))

    def create_mole(self):
        if self.mole_button:
            self.mole_button.destroy()
        x = random.randint(10, 300)
        y = random.randint(10, 300)
        self.mole_button = tk.Button(self.root, width=5, height=2, command=self.whack_mole)
        self.mole_button.place(x=x, y=y)
        self.mole_button.config(text="Mole!", bg="brown")

    def whack_mole(self):
        winsound.Beep(2500, 100)
        self.score += 1
        self.score_label.config(text=f"Score: {self.score}\nHigh Score: {self.high_score}")
        self.mole_button.destroy()
        self.create_mole()
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()

    def countdown(self, count):
        self.time_label.config(text=f"Time: {count}")
        if count > 0:
            self.root.after(1000, lambda: self.countdown(count-1))
        else:
            self.time_label.config(text="Time's up!")
            self.score_label.config(text=f"Final Score: {self.score}\nHigh Score: {self.high_score}")
            if self.mole_button:
                self.mole_button.destroy()

if __name__ == "__main__":
    game = WhackAMole()