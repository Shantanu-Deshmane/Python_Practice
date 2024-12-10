import tkinter as tk
r=tk.Tk() 

def increaseNum():
    n=int(label.cget("text"))
    n+=1
    label.config(text=n)

def decreaseNum():
    n=int(label.cget("text"))
    n-=1
    label.config(text=n)

label=tk.Label(r,text=0)
label.pack()

incBtn=tk.Button(r,text="Increase",command=increaseNum)
incBtn.pack()
decBtn=tk.Button(r,text="Decresase", command=decreaseNum)
decBtn.pack()
r.mainloop()
