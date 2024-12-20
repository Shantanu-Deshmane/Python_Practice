import tkinter as tk
from my_package import gcd

def calculate_gcd():
    a = int(num1.get())
    b = int(num2.get())
    gcd1 = gcd(a, b)
    label_result.config(text=f"GCD: {gcd1}")

root = tk.Tk()

heading = tk.Label(root, text="Enter two numbers to calculate GCD:")
heading.pack()

# first number
num1 = tk.Entry(root)
num1.pack()

# second number
num2 = tk.Entry(root)
num2.pack()

# Button
button_calculate = tk.Button(root, text="Calculate GCD", command=calculate_gcd)
button_calculate.pack()

# Output result
label_result = tk.Label(root, text="GCD: ")
label_result.pack()

root.mainloop()
