# py
# tkinter
from tkinter import Tk, ttk, Menu

root = Tk()
root.title("Menus")
root.geometry("300x50")

# btns menu
menu_button = ttk.Menubutton(root, text="File")
menu_button.pack()

menu = Menu(menu_button, title="Options Btn Menu")
menu_button.config(menu=menu)

def open_file():
    print("Open File...")

menu.add_command(label="Open", command=open_file)

def save_file():
    print("Save File...")

menu.add_command(label="Save", command=save_file)

# bars menu
menu_bar = Menu(root)
root.config(menu=menu_bar)

menu_file = Menu(menu_bar, title="Options Menu File")
menu_bar.add_cascade(label="File", menu=menu_file)

def new_file():
    print("New File...")

def leave_file():
    print("Leave File...")

menu_file.add_command(label="New", command=new_file)
menu_file.add_command(label="Open", command=open_file)
menu_file.add_separator()
menu_file.add_command(label="Leave", command=leave_file)

menu_edit = Menu(menu_bar, title="Options Menu Edit")
menu_bar.add_cascade(label="Edit", menu=menu_edit)

def other_edit():
    print("other...")

menu_edit.add_command(label="Other", command=other_edit)

# context menu
menu_context = Menu(root, tearoff=0)

def action_cut():
    print("Cut")

menu_context.add_command(label="Cut", command=action_cut)

def action_copy():
    print("Copy")

menu_context.add_command(label="Copy", command=action_copy)

def action_paste():
    print("Paste")

menu_context.add_command(label="Paste", command=action_paste)

def show_menu_context(event):
    menu_context.tk_popup(event.x_root, event.y_root)

# menu_button.bind("<Button-3>", show_menu_context) # asignar a element especifico.
root.bind("<Button-3>", show_menu_context)

root.mainloop()