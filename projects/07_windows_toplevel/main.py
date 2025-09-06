# py
# tkinter
from tkinter import Tk, ttk, Toplevel
# third
# own

root = Tk()
root.title("Windows Toplevel")
root.geometry("300x50")

# Variable global para guardar la ventana
top_level = None  

def open_window():
    global top_level
    if top_level is None or not Toplevel.winfo_exists(top_level):
        top_level = Toplevel(root)
        top_level.title("Top Level")
        top_level.geometry("300x50")

        # Cuando el usuario cierra la ventana, ponemos la variable en None
        top_level.protocol("WM_DELETE_WINDOW", on_close)

def on_close():
    global top_level
    if top_level is not None:
        top_level.destroy()
        top_level = None

btn = ttk.Button(root, text="Open Other Window", command=open_window)
btn.pack()

root.mainloop()