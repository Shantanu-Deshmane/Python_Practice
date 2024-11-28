import tkinter as tk
from my_package import calculate

def sumProduct():
    a=(num.get())
    result=calculate(a)
    label.config(text=result)

root=tk.Tk()

heading=tk.Label(root, text="Enter a number to calulate sum and product.")
heading.pack()

num=tk.Entry(root)
num.pack()

button=tk.Button(root, text="Calculate", command=sumProduct)
button.pack()

label=tk.Label(root,text="Sum and Product is: ")
label.pack()

tk.mainloop()