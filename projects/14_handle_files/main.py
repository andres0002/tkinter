# py
# tkinter
from tkinter import Tk, ttk, Text
from tkinter.filedialog import askopenfilename, asksaveasfilename
# third
# own

root = Tk()
root.title("Handle Files -> Editor")

# editor
text = Text(root, wrap="word", background="black", foreground="white", insertbackground="white", font=("Italic", 12, "italic"), padx=10, pady=10)
text.pack(expand=1, fill="both")

def open_file():
    file_path = askopenfilename(filetypes=[("Files .txt", "*.txt"), ("All files .*", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            file_content = file.read()
            text.delete(1.0, "end")
            text.insert(1.0, file_content)

btn_open = ttk.Button(root, text="Open File", command=open_file)
btn_open.pack(expand=1, fill="both", side="left")

def copy_text():
    text.event_generate("<<Copy>>")

btn_copy = ttk.Button(root, text="Copy", command=copy_text)
btn_copy.pack(side="left", expand=1, fill="both")

def cut_text():
    text.event_generate("<<Cut>>")

btn_cut = ttk.Button(root, text="Cut", command=cut_text)
btn_cut.pack(side="left", expand=1, fill="both")

def paste_text():
    text.event_generate("<<Paste>>")

btn_paste = ttk.Button(root, text="Paste", command=paste_text)
btn_paste.pack(side="left", expand=1, fill="both")

def save_file():
    file_path = asksaveasfilename(filetypes=[("Files .txt", "*.txt"), ("All files .*", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            file_content = text.get(1.0, "end")
            file.write(file_content)

btn_save = ttk.Button(root, text="Save File", command=save_file)
btn_save.pack(expand=1, fill="both", side="left")

root.mainloop()