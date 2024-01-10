import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

from art import logo
from Questions import quiz

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")

        self.current_player_index = 0
        self.player_list = []
        self.player_score = {}
        self.current_question_index = 0

        self.intro_label = tk.Label(root, text=logo, font=("Arial", 16))
        self.intro_label.pack(pady=10)

        self.intro_button = tk.Button(root, text="Start Quiz", command=self.start_quiz)
        self.intro_button.pack(pady=10)

    def start_quiz(self):
        self.intro_label.destroy()
        self.intro_button.destroy()

        players_input = simpledialog.askstring("Players", "Enter 2 Players separated by a space:")
        self.player_list = players_input.split()
        self.player_score = {player: 0 for player in self.player_list}

        self.show_question()

    def show_question(self):
        if self.current_question_index < len(quiz):
            question = list(quiz.keys())[self.current_question_index]
            question_text = quiz[question]["question"]

            self.question_label = tk.Label(self.root, text=question_text, font=("Arial", 12))
            self.question_label.pack(pady=10)

            self.answer_entry = tk.Entry(self.root, font=("Arial", 12))
            self.answer_entry.pack(pady=10)

            self.submit_button = tk.Button(self.root, text="Submit Answer", command=self.check_answer)
            self.submit_button.pack(pady=10)
        else:
            self.print_winner()

    def check_answer(self):
        answer = self.answer_entry.get().strip().lower()
        correct_answer = quiz[list(quiz.keys())[self.current_question_index]]["answer"].strip().lower()

        if answer == correct_answer:
            messagebox.showinfo("Correct Answer", f"Correct Answer! {self.player_list[self.current_player_index]}'s score is {self.player_score[self.player_list[self.current_player_index]] + 1}!")
            self.player_score[self.player_list[self.current_player_index]] += 1
        else:
            messagebox.showinfo("Wrong Answer", f"Wrong Answer :( You have 1 attempt left! Try again...")

        self.answer_entry.delete(0, tk.END)

        self.current_player_index = (self.current_player_index + 1) % len(self.player_list)
        self.current_question_index += 1

        self.show_question()

    def print_winner(self):
        if self.player_score[self.player_list[0]] > self.player_score[self.player_list[1]]:
            messagebox.showinfo("Winner", f"{self.player_list[0]} WON! The score is {self.player_score[self.player_list[0]]}")
        elif self.player_score[self.player_list[0]] < self.player_score[self.player_list[1]]:
            messagebox.showinfo("Winner", f"{self.player_list[1]} WON! The score is {self.player_score[self.player_list[1]]}")
        else:
            messagebox.showinfo("Draw", "It's a DRAW!")

        self.root.destroy()

    def mainloop(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    app.mainloop()
