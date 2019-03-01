import tkinter as tk
from tkinter import messagebox

def slapme():
    messagebox.showinfo(message="Get Yeeted")

root = tk.Tk()
root.geometry("500x500")
mainFrame = tk.Frame(root)
mainFrame.pack_propagate(0)
mainFrame.pack()

label1 = tk.Label(mainFrame, text="Name:")
label2 = tk.Label(mainFrame, text="Password:")

label1.grid(row=0)
label2.grid(row=1)

entry1 = tk.Entry(mainFrame)
entry2 = tk.Entry(mainFrame)

entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)




text = tk.Label(mainFrame, text="Yeet")
text.grid(row=10)

button = tk.Button(mainFrame, text="Yeet it!", command=slapme)
button.grid(row=11)


root.mainloop()