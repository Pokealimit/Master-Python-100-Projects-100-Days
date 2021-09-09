from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

# Entry input for Miles
miles_entry = Entry(width=10, justify="center")
miles_entry.grid(column=1, row=0)

# Labels
miles_label = Label(text="Miles", font=("Arial",18,"normal"))
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to", font=("Arial",18,"normal"))
equal_label.grid(column=0, row=1)

km_output = Label(text="0", font=("Arial",18,"normal"))
km_output.grid(column=1, row=1)

km_label = Label(text="Km", font=("Arial",18,"normal"))
km_label.grid(column=2, row=1)


# Calculate Button
def convert_miles_to_km():
    miles = miles_entry.get()
    km = float(miles) * 1.609
    km_output.config(text=str(km))

calculate_btn = Button(text="Calculate", command=convert_miles_to_km)
calculate_btn.grid(column=1, row=2)


window.mainloop()