# py
# tkinter
from tkinter import Tk, ttk
# third
# own

root = Tk()
root.title("Windows Toplevel")
root.geometry("300x80")

frame = ttk.Frame(root)
frame.pack()

for i in range(3):
    ttk.Label(frame, text=f"Label {i + 1}").pack(side="left", expand=1, fill="both", padx=10, pady=10)

frame2 = ttk.Frame(root)
frame2.pack()

for i in range(3):
    ttk.Button(frame2, text=f"BTN {i + 1}").grid(row=0, column=i)

root.mainloop()