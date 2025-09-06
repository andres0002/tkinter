# py
# tkinter
from tkinter import Tk, ttk, Canvas
# third
# own

root = Tk()
root.title("Scrollbar")
root.geometry("500x300")

# --- Canvas con scrollbar ---
canvas = Canvas(root)
scrollbar_vertical = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar_vertical.set)

scrollbar_vertical.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

# --- Frame dentro del Canvas ---
frame = ttk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor="nw")

# --- Agregar muchos labels ---
for i in range(100):
    label = ttk.Label(frame, text=f"Label {i + 1}")
    label.pack(anchor="w", padx=5, pady=2)

# --- Ajustar scroll dinámicamente ---
def update_scroll(_):
    canvas.configure(scrollregion=canvas.bbox("all"))

frame.bind("<Configure>", update_scroll)

# --- Scroll con rueda del mouse ---
def on_mousewheel(event):
    # En Windows el delta viene en múltiplos de 120
    canvas.yview_scroll(-1 * (event.delta // 120), "units")

# Para Windows y Mac
canvas.bind_all("<MouseWheel>", on_mousewheel)

# Para Linux (usa botones 4 y 5 en lugar de delta)
canvas.bind_all("<Button-4>", lambda _: canvas.yview_scroll(-1, "units"))
canvas.bind_all("<Button-5>", lambda _: canvas.yview_scroll(1, "units"))

root.mainloop()

# Claves:

# - Windows / Mac: "<MouseWheel>" → event.delta (en pasos de 120).

# - Linux: se usan eventos "<Button-4>" (rueda arriba) y "<Button-5>" (rueda abajo).

# - Uso canvas.yview_scroll(pasos, "units") para desplazar.