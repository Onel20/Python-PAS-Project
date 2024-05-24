import tkinter as tk
from tkinter import ttk as tema
from tkinter.messagebox import showinfo
import ttkbootstrap as tb

def kirim():
    score = 0
    if question1.get() == "Python":
        score += 10
    if question2.get() == "tkinter":
        score += 10
    if question3.get() == "StringVar":
        score += 10

    result = f"Your score: {score}/30"
    showinfo(title="Quiz Result", message=result)

root = tb.Window(themename="darkly")
root.title("Quiz")
root.geometry("550x700")
root.resizable(False, False)

frame = tema.Frame(root)
frame.pack(padx=10, pady=10, fill="both", expand=True)

question1 = tk.StringVar()
question2 = tk.StringVar()
question3 = tk.StringVar()

# QUESTION 1
labelQ1 = tema.Label(frame, text="1. What is the name of this programming language?", font=("Arial", 12, 'bold'))
labelQ1.grid(row=0, column=0, padx=10, pady=10, sticky="w")

option1 = tema.Radiobutton(frame, value="Java", text="Java", variable=question1)
option1.grid(row=1, column=0, padx=10, pady=10, sticky="w")

option2 = tema.Radiobutton(frame, value="Python", text="Python", variable=question1)
option2.grid(row=2, column=0, padx=10, pady=10, sticky="w")

option3 = tema.Radiobutton(frame, value="HTML", text="HTML", variable=question1)
option3.grid(row=3, column=0, padx=10, pady=10, sticky="w")


# QUESTION 2
labelQ2 = tema.Label(frame, text="2. What is the GUI library used in this quiz?", font=("Arial", 12, 'bold'))
labelQ2.grid(row=4, column=0, padx=10, pady=10, sticky="w")

option1 = tema.Radiobutton(frame, value="Kivy", text="Kivy", variable=question2)
option1.grid(row=5, column=0, padx=10, pady=10, sticky="w")

option2 = tema.Radiobutton(frame, value="PySimpleGUI", text="PySimpleGUI", variable=question2)
option2.grid(row=6, column=0, padx=10, pady=10, sticky="w")

option3 = tema.Radiobutton(frame, value="tkinter", text="tkinter", variable=question2)
option3.grid(row=7, column=0, padx=10, pady=10, sticky="w")


# QUESTION 3
labelQ3 = tema.Label(frame, text="3. What is the variable type for text input in tkinter?", font=("Arial", 12, 'bold'))
labelQ3.grid(row=8, column=0, padx=10, pady=10, sticky="w")

option1 = tema.Radiobutton(frame, value="IntVar", text="IntVar", variable=question3)
option1.grid(row=9, column=0, padx=10, pady=10, sticky="w")

option2 = tema.Radiobutton(frame, value="StringVar", text="StringVar", variable=question3)
option2.grid(row=10, column=0, padx=10, pady=10, sticky="w")

option3 = tema.Radiobutton(frame, value="BoolVar", text="BoolVar", variable=question3)
option3.grid(row=11, column=0, padx=10, pady=10, sticky="w")

submit_button = tema.Button(frame, text="Submit", command=kirim)
submit_button.grid(row=12, column=0, padx=10, pady=10, sticky="w")

root.mainloop()