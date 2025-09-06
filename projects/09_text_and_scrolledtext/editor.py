# py
# tkinter
from tkinter import Tk, ttk
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import askopenfilename, asksaveasfilename
# third
# own

root = Tk()
root.title("Editor")

# ScrolledText
text_desplazable = ScrolledText(root)
text_desplazable.config(
    width=40,
    height=5,
    wrap="word",
    background="black",
    foreground="white",
    padx=10,
    pady=10,
    font=("Italic", 12, "bold"),
    insertbackground="white"
)
text_desplazable.insert("1.0", "¡Bienvenido a nuestro editor de texto!")
text_desplazable.insert("2.0", "\n\n")
text_desplazable.insert("end", "Este es un ejemplo de texto resaltado.", "tag_resaltado")
text_desplazable.tag_configure("tag_resaltado", background="yellow", foreground="black")
# text_desplazable_content = text_desplazable.get("1.0", "end")
# print(text_desplazable_content)
text_desplazable.pack(expand=1, fill="both")

def open_file():
    file = askopenfilename()
    if file:
        text_desplazable.delete(1.0, "end")
        with open(file, "r") as file:
            text_desplazable.insert(1.0, file.read())

btn_open = ttk.Button(root, text="Open File", command=open_file)
btn_open.pack(side="left", expand=1, fill="both")

def copy_text():
    text_desplazable.event_generate("<<Copy>>")

btn_copy = ttk.Button(root, text="Copy", command=copy_text)
btn_copy.pack(side="left", expand=1, fill="both")

def cut_text():
    text_desplazable.event_generate("<<Cut>>")

btn_cut = ttk.Button(root, text="Cut", command=cut_text)
btn_cut.pack(side="left", expand=1, fill="both")

def paste_text():
    text_desplazable.event_generate("<<Paste>>")

btn_paste = ttk.Button(root, text="Paste", command=paste_text)
btn_paste.pack(side="left", expand=1, fill="both")

def save_file():
    file = asksaveasfilename()
    if file:
        with open(file, "w") as file:
            file.write(text_desplazable.get(1.0, "end"))

btn_save = ttk.Button(root, text="Save File", command=save_file)
btn_save.pack(side="left", expand=1, fill="both")

root.mainloop()