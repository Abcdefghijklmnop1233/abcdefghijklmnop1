import tkinter as tk
import random

# Function to display the difficulty selection screen
def displayMenu():
    def set_difficulty(level):
        global difficulty
        difficulty = level
        menu_window.destroy()
        startQuiz()

    menu_window = tk.Tk()
    menu_window.title("Maths Quiz - Difficulty Level")
    tk.Label(menu_window, text="Choose your difficulty level:", font=("Arial", 16)).pack(pady=10)

    tk.Button(menu_window, text="Easy", command=lambda: set_difficulty(1), width=20).pack(pady=5)
    tk.Button(menu_window, text="Moderate", command=lambda: set_difficulty(2), width=20).pack(pady=5)
    tk.Button(menu_window, text="Advanced", command=lambda: set_difficulty(3), width=20).pack(pady=5)

    menu_window.mainloop()

# Function to generate random integers based on difficulty
def randomInt(difficulty):
    if difficulty == 1:
        return random.randint(1, 9)
    elif difficulty == 2:
        return random.randint(10, 99)
    elif difficulty == 3:
        return random.randint(1000, 9999)

# Function to decide the operation (+ or -)
def decideOperation():
    return random.choice(['+', '-'])

# Function to start the quiz
def startQuiz():
    global question_count, score, current_answer
    question_count = 0
    score = 0
    showQuestion()

# Function to display a new question
def showQuestion():
    global num1, num2, operation, current_answer, question_count, question_label, answer_entry

    if question_count < 10:
        num1 = randomInt(difficulty)
        num2 = randomInt(difficulty)
        operation = decideOperation()
        current_answer = num1 + num2 if operation == '+' else num1 - num2

        question_window = tk.Tk()
        question_window.title("Maths Quiz")

        question_label = tk.Label(question_window, text=f"Question {question_count + 1}: {num1} {operation} {num2} = ", font=("Arial", 16))
        question_label.pack(pady=10)

        answer_entry = tk.Entry(question_window, font=("Arial", 14))
        answer_entry.pack(pady=5)

        submit_button = tk.Button(question_window, text="Submit", command=lambda: checkAnswer(question_window))
        submit_button.pack(pady=5)

        question_count += 1
    else:
        displayResults()

# Function to check the user's answer
def checkAnswer(question_window):
    global score
    user_answer = int(answer_entry.get())

    if user_answer == current_answer:
        score += 10
        question_window.destroy()
        showQuestion()
    else:
        tk.Label(question_window, text="Incorrect. Try again!", font=("Arial", 12)).pack(pady=5)
        answer_entry.delete(0, tk.END)

# Function to display the final results
def displayResults():
    result_window = tk.Tk()
    result_window.title("Quiz Results")

    tk.Label(result_window, text=f"Your final score is {score} out of 100.", font=("Arial", 16)).pack(pady=10)

    if score > 90:
        rank = "A+"
    elif score > 80:
        rank = "A"
    elif score > 70:
        rank = "B"
    elif score > 60:
        rank = "C"
    else:
        rank = "Needs Improvement"

    tk.Label(result_window, text=f"Rank: {rank}", font=("Arial", 14)).pack(pady=5)

    tk.Button(result_window, text="Play Again", command=lambda: [result_window.destroy(), displayMenu()]).pack(pady=5)
    tk.Button(result_window, text="Exit", command=result_window.destroy).pack(pady=5)

    result_window.mainloop()

if __name__ == "__main__":
    displayMenu()
