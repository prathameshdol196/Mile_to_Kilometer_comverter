from tkinter import *

window = Tk()
window.title("mile to kilometer converter")
window.config(padx=20, pady=20)
# window.minsize(height=200, width=300)

# label
miles_label = Label(text="Miles", font=("Arial", 10))
miles_label.grid(column=6, row=2)

kilo_label = Label(text="Kilo", font=("Arial", 10))
kilo_label.grid(column=6, row=3)

equal_to_label = Label(text="is equal to", font=("Arial", 10))
equal_to_label.grid(column=4, row=3)

result_label1 = Label(text="0.00", font=("Arial", 10))
result_label1.grid(column=5, row=3)

# Entry
input1 = Entry()
input1.grid(column=5, row=2)


# calculate function
def convert():
    mile = float(input1.get())
    kilo = round(mile * 1.609)
    result_label1.config(text=kilo)


# Button
calculate = Button(text="calculate", command=convert)
calculate.grid(column=5, row=6)







window.mainloop()
