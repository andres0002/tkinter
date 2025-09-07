# py
import os
# tkinter
from tkinter import Tk, ttk, Listbox, END
from tkinter.filedialog import askdirectory
# third
# own

root = Tk()
root.title("Handle Files -> Browser Files")
root.geometry("500x240")

# list files.
def select_folder():
    folder_path = askdirectory()
    if folder_path:
        listbox.delete(0, END)
        for file in os.listdir(folder_path):
            full_path = os.path.join(folder_path, file)  # ruta completa
            if os.path.isfile(full_path):
                listbox.insert(END, file)

listbox = Listbox(root, background="black", foreground="white", font=("Italic", 12, "italic"))
listbox.pack(expand=1, fill="both")

btn_select_folder = ttk.Button(root, text="Select Folder", command=select_folder)
btn_select_folder.pack(expand=1, fill="both")

root.mainloop()