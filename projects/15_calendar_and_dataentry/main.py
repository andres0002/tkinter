# py
# tkinter
from tkinter import Tk
# third
from tkcalendar import Calendar, DateEntry # type: ignore
# own

root = Tk()
root.title("Calendar and DataEntry")
root.geometry("500x220")

# calendar
calendar = Calendar(root, selectmode="day", locale="es_ES", year=2025, month=9, day=6, date_pattern="dd-mm-y")
calendar.pack(expand=1, fill="both")

def get_date(date):
    print("Date:", date)

calendar.bind("<<CalendarSelected>>", lambda _: get_date(calendar.get_date()))

# dateentry
date_entry = DateEntry(root, selectmode="day", locale="es_ES", year=2025, month=9, day=6, date_pattern="dd-mm-y")
date_entry.pack(expand=1, fill="both")

date_entry.bind("<<DateEntrySelected>>", lambda _: get_date(date_entry.get_date().strftime("%d-%m-%Y")))

root.mainloop()