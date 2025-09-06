# py
# tkinter
from tkinter import Tk, ttk, Text
from tkinter.scrolledtext import ScrolledText

root = Tk()
root.title("Text and ScrolledText")

# Text
text = Text(
    root,
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
text.insert("1.0", "¡Bienvenido a nuestro editor de texto!")
text.insert("2.0", "\n\n")
text.insert("end", "Este es un ejemplo de texto resaltado.", "tag_resaltado")
text.tag_configure("tag_resaltado", background="yellow", foreground="black")
# text_content = text.get("1.0", "end")
# print(text_content)
text.pack()

def action_text_copy():
    text.event_generate("<<Copy>>")

def action_text_cut():
    text.event_generate("<<Cut>>")

def action_text_paste():
    text.event_generate("<<Paste>>")

btn_text_copy = ttk.Button(root, text="Copy", command=action_text_copy)
btn_text_copy.pack()
btn_text_cut = ttk.Button(root, text="Cut", command=action_text_cut)
btn_text_cut.pack()
btn_text_paste = ttk.Button(root, text="Paste", command=action_text_paste)
btn_text_paste.pack()

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
text_desplazable.pack()

def action_scrolledtext_copy():
    text_desplazable.event_generate("<<Copy>>")

def action_scrolledtext_cut():
    text_desplazable.event_generate("<<Cut>>")

def action_scrolledtext_paste():
    text_desplazable.event_generate("<<Paste>>")

btn_scrolledtext_copy = ttk.Button(root, text="Copy", command=action_scrolledtext_copy)
btn_scrolledtext_copy.pack()
btn_scrolledtext_cut = ttk.Button(root, text="Cut", command=action_scrolledtext_cut)
btn_scrolledtext_cut.pack()
btn_scrolledtext_paste = ttk.Button(root, text="Paste", command=action_scrolledtext_paste)
btn_scrolledtext_paste.pack()

root.mainloop()