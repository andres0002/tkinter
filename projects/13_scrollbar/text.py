# py
# tkinter
from tkinter import Tk, ttk, Text
# third
# own

root = Tk()
root.title("Scrollbar")
root.geometry("300x200")

scrollbar_vertical = ttk.Scrollbar(root)
scrollbar_vertical.pack(side="right", fill="y")

text = Text(root, background="black", foreground="white", font=("Italic", 12, "italic"), insertbackground="white")

scrollbar_vertical.config(command=text.yview)

text.config(yscrollcommand=scrollbar_vertical.set)
text.pack(side="left", fill="both", expand=1)

root.mainloop()