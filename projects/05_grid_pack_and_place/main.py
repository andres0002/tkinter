# py
# tkinter
from tkinter import Tk, ttk
# third
# own

root = Tk()
root.title("Grid, Pack and Place")
root.geometry("320x140")

# label_one_grid = ttk.Label(root, text="Label One Grid")
# label_one_grid.grid(row=0, column=0, padx=10, pady=10)

# label_two_grid = ttk.Label(root, text="Label Two Grid")
# label_two_grid.grid(row=0, column=1, padx=10, pady=10)

# label_three_grid = ttk.Label(root, text="Label Three Grid")
# label_three_grid.grid(row=0, column=2, padx=10, pady=10)

label_one_pack = ttk.Label(root, text="Label One Pack")
label_one_pack.pack(padx=10, pady=10)

label_two_pack = ttk.Label(root, text="Label Two Pack")
label_two_pack.pack(padx=10, pady=10)

label_three_pack = ttk.Label(root, text="Label Three Pack")
label_three_pack.pack(padx=10, pady=10)

label_one_place = ttk.Label(root, text="Label One Place")
label_one_place.place(x=10, y=30)

label_two_place = ttk.Label(root, text="Label Two Place")
label_two_place.place(x=40, y=70)

label_three_place = ttk.Label(root, text="Label Three Place")
label_three_place.place(x=70, y=110)

root.mainloop()