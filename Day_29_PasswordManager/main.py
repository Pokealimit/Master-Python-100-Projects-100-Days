from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_entry():
    save_website = website_entry.get()
    save_email = email_username_entry.get()
    save_password = password_entry.get()
    # entry = save_website + " | " + save_email + " | " + save_password + "\n"
    with open("Entries.txt", "a") as entries:
        entries.write(f"{save_website} | {save_email} | {save_password}\n")
    clear_entry()

def clear_entry():
    website_entry.delete(0,END)
    # email_username_entry.delete(0,END)
    password_entry.delete(0,END)
    website_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


# Create MyPass Logo
canvas = Canvas(width=200, height=200, highlightthickness=0)
MyPass_logo = PhotoImage(file="logo.png")
# To make logo be in center of canvas (half the coordinates in canvas)
canvas.create_image(100, 100, image=MyPass_logo)
canvas.grid(column=1, row=0)

# Labels
website = Label(text="Website:")
website.grid(column=0, row=1)
email_usrname = Label(text="Email/Username:")
email_usrname.grid(column=0, row=2)
password = Label(text="Password:")
password.grid(column=0, row=3)

# Entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_username_entry = Entry(width=35)
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(0, "pokealimit@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Button
generate_btn = Button(text="Generate Password")
generate_btn.grid(column=2, row=3)
add_btn = Button(text="Add", width=36, command=save_entry)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()