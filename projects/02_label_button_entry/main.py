# py
# import time
# tkinter
from tkinter import Tk, ttk
# third
# own

root = Tk()
root.title("Label, Button and Entry")
root.geometry("300x74")

# Fondo oscuro en la ventana principal
# root.configure(bg="black")

style = ttk.Style()

# Todos los widgets
# style.configure(".", background="black", foreground="white")

label = ttk.Label(root, text="Hello, I'm Label")
label.config(foreground="blue", background="yellow", font=("Arial", 12, "bold"))
label.pack()

# def update_hour():
#     label.config(text=time.strftime("%H:%M:%S"))
#     root.after(1000, update_hour)

# update_hour()

entry = ttk.Entry(root)
entry.config(foreground="blue", background="black", font=("Arial", 12, "bold"))
entry.pack()

def handle_btn_update_text():
    label.config(text=entry.get())

style.configure(
    "BTN.TButton"
)

btn = ttk.Button(root, text="Update Text Label", style="BTN.TButton", command=handle_btn_update_text)
btn.pack()

root.mainloop()