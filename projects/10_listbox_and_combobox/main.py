# py
# tkinter
from tkinter import Tk, ttk, Listbox, END
# third
# own

root = Tk()
root.title("Listbox and Combobox")
root.geometry("300x240")

# Listbox
listbox = Listbox(root, background="black", foreground="white", font=("Italic", 12, "bold"), selectmode="multiple")

listbox.insert(END, "Element Listbox 1")
listbox.insert(END, "Element Listbox 2")
listbox.insert(END, "Element Listbox 3")

listbox.pack(expand=1, fill="both")

def on_selected_listbox(_):
    index = listbox.curselection()
    if len(index) == 0:
        return
    elif len(index) > 1:
        for i in index:
            element = listbox.get(i)
            print("Selected:", element)
        return
    element = listbox.get(index)
    print("Selected:", element)

listbox.bind("<<ListboxSelect>>", on_selected_listbox)

def on_clic(_):
    print("Clic in listbox...")

listbox.bind("<Button-1>", on_clic)

def on_double_clic(_):
    print("Double clic in listbox...")

listbox.bind("<Double-Button-1>", on_double_clic)

# Combobox
elements = ["Element Combobox 1", "Element Combobox 2", "Element Combobox 3"]
combobox = ttk.Combobox(root, font=("Italic", 12, "bold"), state="readonly", values=elements)
combobox.set("Select Element...")

combobox.pack(expand=1, fill="both")

def on_selected_combobox(_):
    print("Selected:", combobox.get())

combobox.bind("<<ComboboxSelected>>", on_selected_combobox)

root.mainloop()
