# py
import re
# tkinter
from tkinter import Tk, ttk
# third
# own

root = Tk()
root.title("Calculator")

def validate_expression(expr: str) -> bool:
    expr = expr.strip()

    # 1. Solo caracteres válidos
    if not re.fullmatch(r"[0-9+\-*/(). ]+", expr):
        return False

    # 2. Debe contener al menos un número
    if not re.search(r"\d", expr):
        return False

    # 3. No empezar con operador inválido
    if expr[0] in "*/+":
        return False

    # 4. No terminar en operador
    if expr[-1] in "+-*/":
        return False

    # 5. No operadores duplicados tipo "++", "**", "*/", "..", etc.
    if re.search(r"[\+\-*./]{2,}", expr.replace(" ", "")):
        return False

    return True

def handle_click(value):
    if value == "=":
        operation = entry.get()
        if not validate_expression(operation):
            entry.config(state="normal")
            entry.delete(0, "end")
            entry.insert(0, "Error")
            entry.config(state="readonly")
            return
        if operation:
            entry.config(state="normal")
            entry.delete(0, "end")
            entry.insert(0, round(eval(operation, {"__builtins__": None}, {}), 2))
            entry.config(state="readonly")
        return
    elif value.lower() == "clean":
        entry.config(state="normal")
        entry.delete(0, "end")
        entry.insert(0, "")
        entry.config(state="readonly")
        return
    entry.config(state="normal")   # desbloquear
    entry.insert("end", value)     # agregar texto
    entry.config(state="readonly") # volver a solo lectura

entry = ttk.Entry(root, font=("Arial", 12, "italic"), justify="right", style="Entry.TEntry", state="readonly")
entry.grid(row=0, column=0, columnspan=4, sticky="ew")

btns = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['.', '0', '=', '+']
]

for row_i, row in enumerate(btns, 1):
    for col_j, value in enumerate(row):
        ttk.Button(
            root,
            text=value,
            command=lambda v=value: handle_click(v)
        ).grid(
            row=row_i,
            column=col_j
        )

# btn_7 = ttk.Button(root, text="7", command=lambda: handle_click("7"))
# btn_7.grid(row=1, column=0)
# btn_8 = ttk.Button(root, text="8", command=lambda: handle_click("8"))
# btn_8.grid(row=1, column=1)
# btn_9 = ttk.Button(root, text="9", command=lambda: handle_click("9"))
# btn_9.grid(row=1, column=2)
# btn_div = ttk.Button(root, text="/", command=lambda: handle_click("/"))
# btn_div.grid(row=1, column=3)

# btn_4 = ttk.Button(root, text="4", command=lambda: handle_click("4"))
# btn_4.grid(row=2, column=0)
# btn_5 = ttk.Button(root, text="5", command=lambda: handle_click("5"))
# btn_5.grid(row=2, column=1)
# btn_6 = ttk.Button(root, text="6", command=lambda: handle_click("6"))
# btn_6.grid(row=2, column=2)
# btn_mult = ttk.Button(root, text="*", command=lambda: handle_click("*"))
# btn_mult.grid(row=2, column=3)

# btn_1 = ttk.Button(root, text="1", command=lambda: handle_click("1"))
# btn_1.grid(row=3, column=0)
# btn_2 = ttk.Button(root, text="2", command=lambda: handle_click("2"))
# btn_2.grid(row=3, column=1)
# btn_3 = ttk.Button(root, text="3", command=lambda: handle_click("3"))
# btn_3.grid(row=3, column=2)
# btn_res = ttk.Button(root, text="-", command=lambda: handle_click("-"))
# btn_res.grid(row=3, column=3)

# btn_point = ttk.Button(root, text=".", command=lambda: handle_click("."))
# btn_point.grid(row=4, column=0)
# btn_0 = ttk.Button(root, text="0", command=lambda: handle_click("0"))
# btn_0.grid(row=4, column=1)
# btn_equal = ttk.Button(root, text="=", command=lambda: handle_click("="))
# btn_equal.grid(row=4, column=2)
# btn_sum = ttk.Button(root, text="+", command=lambda: handle_click("+"))
# btn_sum.grid(row=4, column=3)

btn_clean = ttk.Button(root, text="Clean", command=lambda: handle_click("clean"))
btn_clean.grid(row=5, column=0, columnspan=4, sticky="ew")

root.mainloop()