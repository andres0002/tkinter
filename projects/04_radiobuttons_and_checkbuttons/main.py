# py
# tkinter
from tkinter import Tk, ttk, IntVar, BooleanVar
# third
# own

root = Tk()
root.title("Radiobuttons and Checkbuttons")
root.geometry("350x200")

variable_control = IntVar()

def change_color():
    color_selected = variable_control.get()
    if color_selected == 1:
        root.config(background="red")
    elif color_selected == 2:
        root.config(background="green")
    elif color_selected == 3:
        root.config(background="blue")
    else:
        root.config(background="black")

rb_red = ttk.Radiobutton(root, text="Red", variable=variable_control, value=1, command=change_color)
rb_red.pack()

rb_green = ttk.Radiobutton(root, text="Green", variable=variable_control, value=2, command=change_color)
rb_green.pack()

rb_blue = ttk.Radiobutton(root, text="Blue", variable=variable_control, value=3, command=change_color)
rb_blue.pack()

def show_selection():
    print("Option selected:", variable_control.get())

btn = ttk.Button(root, text="Show Selected", command=show_selection)
btn.pack()

def on_check_button_change():
    print("Check One:", variable_check_one.get())
    print("Check Two:", variable_check_two.get())
    print("Check Three:", variable_check_three.get())

variable_check_one = BooleanVar()
variable_check_two = BooleanVar()
variable_check_three = BooleanVar()
variable_check_activate = BooleanVar()

check_one = ttk.Checkbutton(root, text="Option One", variable=variable_check_one, command=on_check_button_change)
check_one.pack()

check_two = ttk.Checkbutton(root, text="Option Two", variable=variable_check_two, command=on_check_button_change)
check_two.pack()

check_three = ttk.Checkbutton(root, text="Option Three", variable=variable_check_three, command=on_check_button_change)
check_three.pack()

def activate_or_deactivate_btn2():
    if variable_check_activate.get():
        check_activate.config(text="Btn2 Deactivate")
        btn2.config(state="normal")
    else:
        check_activate.config(text="Btn2 Activate")
        btn2.config(state="disabled")

check_activate = ttk.Checkbutton(root, text="Btn2 Activate", variable=variable_check_activate, command=activate_or_deactivate_btn2)
check_activate.pack()

btn2 = ttk.Button(root, text="Clic", state="disabled")
btn2.pack()

root.mainloop()