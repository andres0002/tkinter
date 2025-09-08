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
        top_level.title("Top Level - Modal")
        top_level.geometry("300x160")
        
        # Hacer que aparezca en el centro de la ventana principal
        top_level.transient(root)
        
        # Bloquear interacción con la ventana principal
        top_level.grab_set()
        
        # Widgets del modal
        ttk.Label(top_level, text="Title", font=("Arial", 24, "bold")).pack(pady=10)
        ttk.Label(top_level, text="Description", font=("Arial", 14, "italic")).pack(pady=10)
        ttk.Button(top_level, text="Ok", command=on_close).pack(pady=10)
        
        # Esperar hasta que se cierre
        # root.wait_window(top_level)
        
        # Cuando el usuario cierra la ventana, ponemos la variable en None
        top_level.protocol("WM_DELETE_WINDOW", on_close)

def on_close():
    global top_level
    if top_level is not None:
        top_level.destroy()
        top_level = None

btn = ttk.Button(root, text="Open Other Window", command=open_window)
btn.pack(pady=10)

root.mainloop()