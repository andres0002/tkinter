# py
# tkinter
from tkinter import Tk, ttk
# third
# own

root = Tk()
# title
root.title("Config and Organize UI")
# width x height
root.geometry("300x90")
# width x height + left + top
# root.geometry("300x50+200+200")
# min (width, height)
# root.minsize(300, 50)
# # max (width, height)
# root.maxsize(800, 600)
# # icon.ico
root.iconbitmap("./assets/imgs/icon.ico")
# config
root.configure(bg="gray1")
# resizable (width, height)
# root.resizable(False, False)
# opacida
# root.attributes("-alpha", 0.5)

# Crear estilo personalizado
style = ttk.Style()
style.configure(
    "Blue.TLabelframe",       # nombre del estilo
    background="blue",   # color de fondo
    borderwidth=8,      # ancho del borde
    relief="sunken"     # estilo del borde
)

labelfrm = ttk.Labelframe(root, text="Label Frame", style="Blue.TLabelframe", width=300, height=200)
labelfrm.pack(padx=20, pady=20)

# Crear estilo personalizado
style = ttk.Style()
style.configure(
    "Red.TFrame",       # nombre del estilo
    background="red",   # color de fondo
    borderwidth=8,      # ancho del borde
    relief="sunken"     # estilo del borde
)

frm = ttk.Frame(root, style="Red.TFrame", width=200, height=100)
frm.pack(padx=20, pady=20)

ttk.Label(frm, text="Hello World!").grid(column=0, row=0, padx=10, pady=10)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0, padx=10, pady=10)

root.mainloop()