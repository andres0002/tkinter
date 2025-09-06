# py
# tkinter
from tkinter import Tk, ttk
# third
from PIL import Image, ImageTk
# own

root = Tk()
root.title("PhotoImage")

imgs = [ImageTk.PhotoImage(Image.open(f"./assets/imgs/img{i + 1}.jpg").resize((300,200))) for i in range(3)]

for i, img in enumerate(imgs):
    label = ttk.Label(root, image=img)
    label.grid(row=0, column=i)

for i, img in enumerate(imgs):
    btn = ttk.Button(root, image=img)
    btn.grid(row=1, column=i)

root.mainloop()