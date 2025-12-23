from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)


def miles_to_km():
    miles = float(entry.get())
    km = miles * 1.609
    km_value_label.config(text=f"{km:.0f}")


entry = Entry(width=10)
entry.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(row=1, column=0)

km_value_label = Label(text="0")
km_value_label.grid(row=1, column=1)

km_label = Label(text="km")
km_label.grid(row=1, column=2)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(row=2, column=1)
window.mainloop()
