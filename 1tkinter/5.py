import tkinter as tk

def calculate():
        
        num1, num2 = float(entry_num1.get()), float(entry_num2.get())
        operation = operation_var.get()
        if operation == "Add": result = num1 + num2
        elif operation == "Subtract": result = num1 - num2
        elif operation == "Multiply": result = num1 * num2
        elif operation == "Divide": result = num1 / num2 if num2 != 0 else "Error! Division by zero."
        result_label.config(text=f"Result: {result}")

root = tk.Tk()
root.title("Calculator")

tk.Label(root, text="First number:").pack(pady=5)
entry_num1 = tk.Entry(root); entry_num1.pack(pady=5)
tk.Label(root, text="Second number:").pack(pady=5)
entry_num2 = tk.Entry(root); entry_num2.pack(pady=5)

operation_var = tk.StringVar(value="Add")
for op in ["Add", "Subtract", "Multiply", "Divide"]:
    tk.Radiobutton(root, text=op, variable=operation_var, value=op).pack(pady=2)

tk.Button(root, text="Calculate", command=calculate).pack(pady=10)
result_label = tk.Label(root, text="Result: "); result_label.pack(pady=10)

root.mainloop()
