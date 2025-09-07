# py
# tkinter
from tkinter import Tk, Menu
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import askopenfilename, asksaveasfilename
# third
# own

root = Tk()
root.title("Notepad")
root.geometry("300x350")

menu = Menu(root)
root.config(menu=menu)

# functions callback file

menu_file = Menu(menu)
menu.add_cascade(label="File", menu=menu_file)

def new_file():
    scrolltext.delete(1.0, "end")

menu_file.add_command(label="New", command=new_file)

file_path = None

def open_file():
    global file_path
    file_path = askopenfilename(
        defaultextension=".txt",
        filetypes=[
            ("Files (*.txt)", "*.txt"),
            ("Files (*.py)", "*.py"),
            ("Files (*.*)", "*.*")
        ]
    )
    if file_path:
        scrolltext.delete(1.0, "end")
        with open(file_path, "r") as file:
            scrolltext.insert(1.0, file.read())

menu_file.add_command(label="Open", command=open_file)

def save_file():
    global file_path
    if file_path:
        try:
            with open(file_path, "w") as file:
                file.write(scrolltext.get(1.0, "end"))
        except Exception as _:
            print("Error: Al guardar el file...")

menu_file.add_command(label="Save", command=save_file)

def save_as():
    file_path = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[
            ("Files (*.txt)", "*.txt"),
            ("Files (*.py)", "*.py"),
            ("Files (*.*)", "*.*")
        ]
    )
    if file_path:
        with open(file_path, "w") as file:
            file.write(scrolltext.get(1.0, "end"))

menu_file.add_command(label="Save As", command=save_as)

# functions callback edit

menu_edit = Menu(menu)
menu.add_cascade(label="Edit", menu=menu_edit)

def copy_text():
    scrolltext.event_generate("<<Copy>>")

menu_edit.add_command(label="Copy", command=copy_text)

def cut_text():
    scrolltext.event_generate("<<Cut>>")

menu_edit.add_command(label="Cut", command=cut_text)

def paste_text():
    scrolltext.event_generate("<<Paste>>")

menu_edit.add_command(label="Paste", command=paste_text)

scrolltext = ScrolledText(root, background="black", foreground="white", insertbackground="white", font=("Arial", 12, "italic"), padx=10, pady=10, wrap="word")
scrolltext.pack(expand=1, fill="both")

root.mainloop()