# py
# tkinter
from tkinter import Tk, ttk
# third
# own

root = Tk()
root.title("Events and Callbacks")
root.geometry("300x80")

def on_click(event):
    print(f"BTN '{event.widget['text']}' pressed...")

btns = [ttk.Button(root, text=f"BTN {i + 1}") for i in range(3)]
for btn in btns:
    btn.pack()
    btn.bind("<Button-1>", on_click)

def on_key_press(event):
    if event.char == "a":
        print("Tecla 'a' pressed...")

root.bind("<KeyPress>", on_key_press)

# def on_resize(event):
#     print(f"La ventana ha sido redimensionada a {event.width}x{event.height}...")

# root.bind("<Configure>", on_resize)

# def on_mouse_move(event):
#     print(f"Mouse move to: {event.x}, {event.y}...")

# root.bind("<Motion>", on_mouse_move)

root.mainloop()