# py
# tkinter
from tkinter import Tk, ttk, StringVar, IntVar, DoubleVar, BooleanVar
# third
# own

root = Tk()
root.title("Control Variables")
root.geometry("300x200")

# StringVar
text = StringVar()

input = ttk.Entry(root, textvariable=text)
input.pack()

label_text = ttk.Label(root)
label_text.pack()

def update_text(*args):
    # print(args)
    label_text.config(text=text.get())

text.trace_add("write", update_text)

# IntVar
num = IntVar()

rb_one = ttk.Radiobutton(root, text="RB One", variable=num, value=1)
rb_one.pack()

rb_two = ttk.Radiobutton(root, text="RB Two", variable=num, value=2)
rb_two.pack()

label_num = ttk.Label(root)
label_num.pack()

def update_num(*args):
    # print(args)
    label_num.config(text=f"Num: {num.get()}")

num.trace_add("write", update_num)

# DoubleVar
num_float = DoubleVar()

control_deslizante = ttk.Scale(root, variable=num_float, from_=0, to=10, orient="horizontal")
control_deslizante.pack()

label_double = ttk.Label(root)
label_double.pack()

def update_num_float(*args):
    # print(args)
    label_double.config(text=num_float.get())

num_float.trace_add("write", update_num_float)

# BooleanVar
boolean = BooleanVar()

active_check = ttk.Checkbutton(root, text="Activate", variable=boolean)
active_check.pack()

label_boolean = ttk.Label(root)
label_boolean.pack()

def update_boolean(*args):
    # print(args)
    # print(boolean.get())
    label_boolean.config(text=boolean.get())
    if boolean.get():
        active_check.config(text="Deactivate")
        return
    active_check.config(text="Activate")

boolean.trace_add("write", update_boolean)

root.mainloop()