# py
# tkinter
from tkinter import Tk, Canvas
# third
# own

root = Tk()
root.title("Canvas")

canvas = Canvas(root, width=500, height=300, background="black")

rectangle = canvas.create_rectangle(50,50,200,150, fill="green", outline="white", width=2, tags="rectangle")
oval = canvas.create_oval(250,50,350,150, fill="green", outline="white", width=2, tags="oval")
polygon = canvas.create_polygon(380,50,450,100,380,150,450,50, fill="green", outline="white", width=2, tags="polygon")
line = canvas.create_line(50,200,450,200, fill="white", width=2, dash=(10, 2), capstyle="round", tags="line")

text = canvas.create_text(50, 250, text="XD", fill="green", font=("Italic", 12, "italic"), justify="center", tags="text")

canvas.pack(expand=1, fill="both")

object_selected = None

def start_drag(event):
    global object_selected
    object_selected = canvas.find_closest(event.x, event.y)

canvas.tag_bind("rectangle", "<ButtonPress-1>", start_drag)
canvas.tag_bind("oval", "<ButtonPress-1>", start_drag)
canvas.tag_bind("polygon", "<ButtonPress-1>", start_drag)
canvas.tag_bind("line", "<ButtonPress-1>", start_drag)
canvas.tag_bind("text", "<ButtonPress-1>", start_drag)

def end_drop(event):
    global object_selected
    if object_selected:
        x, y = event.x, event.y
        canvas.move(object_selected, x - canvas.coords(object_selected)[0], y - canvas.coords(object_selected)[1])
        object_selected = None

canvas.tag_bind("rectangle", "<ButtonRelease-1>", end_drop)
canvas.tag_bind("oval", "<ButtonRelease-1>", end_drop)
canvas.tag_bind("polygon", "<ButtonRelease-1>", end_drop)
canvas.tag_bind("line", "<ButtonRelease-1>", end_drop)
canvas.tag_bind("text", "<ButtonRelease-1>", end_drop)

root.mainloop()