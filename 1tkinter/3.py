import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

root.geometry("300x200")

label_username = tk.Label(root, text="Username:")
label_username.pack(pady=10)

userName = tk.Entry(root)
userName.pack(pady=5)

label_password = tk.Label(root, text="Password:")
label_password.pack(pady=10)

entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

login_button = tk.Button(root, text="Login")
login_button.pack(pady=20)

root.mainloop()
