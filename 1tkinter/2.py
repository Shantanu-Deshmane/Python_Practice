import tkinter as tk
from tkinter import messagebox

def factorial():
    n=int(entry.get())
    if n < 0:
        messagebox.showerror("Input Error", "Factorial does not exist for negative numbers.")
        return
    result = 1
    for i in range(1, n + 1):
        result *= i
        label_result.config(text=f"Factorial: {result}")  

root = tk.Tk()
root.title("Factorial Calculator")

root.geometry("300x200")

label_instruction = tk.Label(root, text="Enter a number:")
label_instruction.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

button_calculate = tk.Button(root, text="Calculate Factorial", command=factorial)
button_calculate.pack(pady=10)

label_result = tk.Label(root, text="Factorial: ")
label_result.pack(pady=10)

root.mainloop()
