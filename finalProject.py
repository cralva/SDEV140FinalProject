"""
Author: Cristian Alvarez
Date: 4/27/2025
Assignment: SDEV 140 Final Project
Version: 1.0
"""


import tkinter as tk
from tkinter import messagebox



# module for data validation. Error message will pop up is input is not a positive number or if its a letter
def validate_and_calculate():
    try:
        income = float(incomeEntry.get()) #getting income, expense, and savings
        expenses = float(expenseEntry.get())
        savings = float(savingsEntry.get())

        if income <= 0 or expenses < 0 or savings < 0: #if statement for the wrong data inputs
            raise ValueError

        leftover = income - expenses - savings #formula for leftover income

        resultLabel.config(text=f"Leftover after savings: ${leftover:.2f}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter positive numeric values in all fields.") # the error that will pop up is data is not valid

#for our button that will initalize the calculator
def open_budget_window():
    welcomeWindow.withdraw()
    budgetWindow.deiconify()

#we will use this module for our clear button. this will clear any inputs
def clear_fields():
    incomeEntry.delete(0, tk.END)
    expenseEntry.delete(0, tk.END)
    savingsEntry.delete(0, tk.END)
    resultLabel.config(text="")


#attach this to our exit button. will close the program when pressed
def exit_app():
    welcomeWindow.destroy()



welcomeWindow = tk.Tk() #our welcome window (window 1)
welcomeWindow.title("BudgetBeast - Welcome")
welcomeWindow.geometry("350x400")

icon = tk.PhotoImage(file="BudgetBeastLogo.png") #a web icon for the program
welcomeWindow.iconphoto(True, icon)


logo = tk.PhotoImage(file="BudgetBeastLogo.png")  # first logo, main logo for program
logoLabel = tk.Label(welcomeWindow, image=logo, text="BudgetBeast Logo", compound="top")
logoLabel.pack(pady=10)

welcomeLabel = tk.Label(welcomeWindow, text="Welcome to BudgetBeast!", font=("Arial", 18, "bold"))
welcomeLabel.pack(pady=10)

goButton = tk.Button(welcomeWindow, text="Go to Budget Calculator", command=open_budget_window) #calling the open_budget_window function
goButton.pack(pady=10)

exitButton1 = tk.Button(welcomeWindow, text="Exit", command=exit_app) # exit button that closes the app
exitButton1.pack(pady=10)


budgetWindow = tk.Toplevel() #making our second gui window
budgetWindow.title("BudgetBeast - Calculator")
budgetWindow.geometry("450x720")
budgetWindow.withdraw()


icon2 = tk.PhotoImage(file="MoneyIcon.png")  # second image
iconLabel = tk.Label(budgetWindow, image=icon2, text="Enter Your Financials Below:", compound="top")
iconLabel.pack(pady=5)

label1 = tk.Label(budgetWindow, text="Enter monthly income:") #label asking for monthly income
label1.pack()
incomeEntry = tk.Entry(budgetWindow) #entry box to input monthy income
incomeEntry.pack(pady=5)

label2 = tk.Label(budgetWindow, text="Enter monthly expenses:") #label for monthly expenses
label2.pack()
expenseEntry = tk.Entry(budgetWindow) #entry box to input expenses
expenseEntry.pack(pady=5)

label3 = tk.Label(budgetWindow, text="Enter savings goal:") #label asking user for savings goal
label3.pack()
savingsEntry = tk.Entry(budgetWindow) #entry box to input savings goal
savingsEntry.pack(pady=5)

generateButton = tk.Button(budgetWindow, text="Generate Budget", command=validate_and_calculate) # calling our formula function so that the numbers can be calculated
generateButton.pack(pady=10)

resultLabel = tk.Label(budgetWindow, text="", font=("Arial", 12, "bold"))
resultLabel.pack(pady=10)

clearButton = tk.Button(budgetWindow, text="Clear", command=clear_fields) #button that calls clear_fields which will clear all entry boxes
clearButton.pack(pady=5)

exitButton2 = tk.Button(budgetWindow, text="Exit", command=exit_app) #button that kills the program
exitButton2.pack(pady=10)


welcomeWindow.mainloop()