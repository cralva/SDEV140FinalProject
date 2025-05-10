"""
Author: Cristian Alvarez
Date: 4/27/2025
Assignment: SDEV 140 Final Project
Version: 1.0
"""

import tkinter as tk

window = tk.Tk()
window.title("BudgetBeast")
window.geometry("300x400")

icon = tk.PhotoImage(file="BudgetBeastLogo.png")
window.iconphoto(True, icon)

firstLabel = tk.Label(window, text="BudgetBeast Budget Tracker",
                      font=("Arial", 20, "bold")
                      )
firstLabel.pack(pady=10)

incomeLabel = tk.Label(window, text="Enter how much you make per month:")
incomeLabel.pack()


incomeEntry = tk.Entry(window)
incomeEntry.pack(pady=5)

expenseLabel = tk.Label(window, text="How much do you spend a month?")
expenseLabel.pack()

expenseEntry = tk.Entry(window)
expenseEntry.pack(pady=5)

savingsLabel = tk.Label(window, text="How much do you want to save a month?")
savingsLabel.pack()

savingsEntry = tk.Entry(window)
savingsEntry.pack(pady=5)

generateButton = tk.Button(window, text="Generate Budget")
generateButton.pack(pady=5)






window.mainloop()
