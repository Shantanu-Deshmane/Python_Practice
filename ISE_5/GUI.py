import tkinter as tk
from tkinter import messagebox

def is_armstrong(number):
    num_str = str(number)
    n = len(num_str) 
    sum_of_powers = sum(int(digit) ** n for digit in num_str) 
    return sum_of_powers == number

def check_armstrong():

        number = int(entry.get())
        
        if is_armstrong(number):
            result = f"{number} is an Armstrong number!"
        else:
            result = f"{number} is not an Armstrong number."
        
        messagebox.showinfo("Result", result)


root = tk.Tk()
root.title("Armstrong Number Checker")

label = tk.Label(root, text="Enter a number:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

button = tk.Button(root, text="Check", command=check_armstrong)
button.pack(pady=20)

root.mainloop()
