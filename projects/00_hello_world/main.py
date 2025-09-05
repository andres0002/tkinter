# py
# tkinter
from tkinter import Tk, ttk
# third
# own

root = Tk()
root.title("TK - First Window")
root.geometry("280x50")

frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)

root.mainloop()