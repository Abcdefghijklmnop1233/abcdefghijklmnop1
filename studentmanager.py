import tkinter as tk
from tkinter import ttk, messagebox
import os

# Read student data from the file
def load_student_data():
    if not os.path.exists("studentMarks.txt"):
        messagebox.showerror("Error", "The file 'studentMarks.txt' is missing.")
        return []

    with open("studentMarks.txt", "r") as file:
        lines = file.readlines()

    # Parse the data
    student_data = []
    for line in lines[1:]:  # Skip the first line with the number of students
        parts = line.strip().split(",")
        student_data.append({
            "id": parts[0],
            "name": parts[1],
            "coursework": list(map(int, parts[2:5])),
            "exam": int(parts[5])
        })
    return student_data

# Calculate total, percentage, and grade for a student
def calculate_scores(student):
    coursework_total = sum(student["coursework"])
    overall_total = coursework_total + student["exam"]
    percentage = (overall_total / 160) * 100

    if percentage >= 70:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "F"

    return coursework_total, percentage, grade

# Display all student records
def view_all_records():
    output.delete(1.0, tk.END)
    total_percentage = 0

    for student in students:
        coursework_total, percentage, grade = calculate_scores(student)
        total_percentage += percentage

        output.insert(tk.END, f"Name: {student['name']}\n")
        output.insert(tk.END, f"ID: {student['id']}\n")
        output.insert(tk.END, f"Coursework Total: {coursework_total}\n")
        output.insert(tk.END, f"Exam: {student['exam']}\n")
        output.insert(tk.END, f"Overall Percentage: {percentage:.2f}%\n")
        output.insert(tk.END, f"Grade: {grade}\n")
        output.insert(tk.END, "-" * 30 + "\n")

    avg_percentage = total_percentage / len(students)
    output.insert(tk.END, f"Total Students: {len(students)}\n")
    output.insert(tk.END, f"Average Percentage: {avg_percentage:.2f}%\n")

# Display individual student record
def view_individual_record():
    selected_student = student_combo.get()
    if not selected_student:
        messagebox.showwarning("Warning", "Please select a student.")
        return

    student = next((s for s in students if s["name"] == selected_student), None)
    if student:
        coursework_total, percentage, grade = calculate_scores(student)
        output.delete(1.0, tk.END)
        output.insert(tk.END, f"Name: {student['name']}\n")
        output.insert(tk.END, f"ID: {student['id']}\n")
        output.insert(tk.END, f"Coursework Total: {coursework_total}\n")
        output.insert(tk.END, f"Exam: {student['exam']}\n")
        output.insert(tk.END, f"Overall Percentage: {percentage:.2f}%\n")
        output.insert(tk.END, f"Grade: {grade}\n")

# Show student with highest score
def show_highest_score():
    highest = max(students, key=lambda s: sum(s["coursework"]) + s["exam"])
    coursework_total, percentage, grade = calculate_scores(highest)
    output.delete(1.0, tk.END)
    output.insert(tk.END, f"Highest Scorer: {highest['name']}\n")
    output.insert(tk.END, f"ID: {highest['id']}\n")
    output.insert(tk.END, f"Coursework Total: {coursework_total}\n")
    output.insert(tk.END, f"Exam: {highest['exam']}\n")
    output.insert(tk.END, f"Overall Percentage: {percentage:.2f}%\n")
    output.insert(tk.END, f"Grade: {grade}\n")

# Show student with lowest score
def show_lowest_score():
    lowest = min(students, key=lambda s: sum(s["coursework"]) + s["exam"])
    coursework_total, percentage, grade = calculate_scores(lowest)
    output.delete(1.0, tk.END)
    output.insert(tk.END, f"Lowest Scorer: {lowest['name']}\n")
    output.insert(tk.END, f"ID: {lowest['id']}\n")
    output.insert(tk.END, f"Coursework Total: {coursework_total}\n")
    output.insert(tk.END, f"Exam: {lowest['exam']}\n")
    output.insert(tk.END, f"Overall Percentage: {percentage:.2f}%\n")
    output.insert(tk.END, f"Grade: {grade}\n")

# Load student data
students = load_student_data()

# Create main window
root = tk.Tk()
root.title("Student Manager")
root.geometry("600x500")

# Title label
title_label = tk.Label(root, text="Student Manager", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Buttons for actions
frame = tk.Frame(root)
frame.pack(pady=5)

view_all_button = tk.Button(frame, text="View All Student Records", command=view_all_records, width=20)
view_all_button.grid(row=0, column=0, padx=5, pady=5)

highest_score_button = tk.Button(frame, text="Show Highest Score", command=show_highest_score, width=20)
highest_score_button.grid(row=0, column=1, padx=5, pady=5)

lowest_score_button = tk.Button(frame, text="Show Lowest Score", command=show_lowest_score, width=20)
lowest_score_button.grid(row=0, column=2, padx=5, pady=5)

# Dropdown and individual view
individual_frame = tk.Frame(root)
individual_frame.pack(pady=10)

student_combo = ttk.Combobox(individual_frame, values=[s["name"] for s in students], width=25)
student_combo.grid(row=0, column=0, padx=5, pady=5)
student_combo.set("Select Student")

view_individual_button = tk.Button(individual_frame, text="View Record", command=view_individual_record)
view_individual_button.grid(row=0, column=1, padx=5, pady=5)

# Output box
output = tk.Text(root, height=15, width=70)
output.pack(pady=10)

# Run the application
root.mainloop()
