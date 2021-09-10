from tkinter import *
# Need to import messagebox as it is not a class/constant but a module
from tkinter import messagebox
import pyperclip, json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from password_generator import random_password

def generate_password():
    password = random_password()
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_entry():
    save_website = website_entry.get()
    save_email = email_username_entry.get()
    save_password = password_entry.get()

    new_entry = {
        save_website: {
            "email": save_email,
            "password": save_password
        }
    }

    # Check if field empty
    if not save_password or not save_website:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        # Ask user confirmation
        is_ok = messagebox.askokcancel(title=save_website, message=f"These are the details entered: \nEmail: {save_email} "
                                                        f"\nPassword: {save_password} \nIs it ok to save?")
        if is_ok:
            try:
                with open("Entries.json", "r") as entries:
                    # Read old data
                    data = json.load(entries)
                    # Update old data with new data
                    data.update(new_entry)

            except FileNotFoundError:
                with open("Entries.json", "w") as entries:
                    # Writing new file (first time)
                    json.dump(new_entry, entries, indent=4)
            
            else:
                with open("Entries.json", "w") as entries:
                    # Writing updated data
                    json.dump(data, entries, indent=4)

            finally:
                clear_entry()

def clear_entry():
    website_entry.delete(0,END)
    # email_username_entry.delete(0,END)
    password_entry.delete(0,END)
    website_entry.focus()

# ---------------------------- SEARCH ------------------------------- #

def find_password():
    website_query = website_entry.get()
    try:
        with open("Entries.json", "r") as entries:
            data = json.load(entries)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="No Data File Found")
    else:
        if website_query in data:
            password_query = data[website_query]["password"]
            email_query = data[website_query]["email"]
            messagebox.showinfo(title=website_query, message=f"Username/Email: {email_query} \nPassword: {password_query}")
        else:
            messagebox.showinfo(title="Oops", message=f"No details for {website_query} found")


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
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()
email_username_entry = Entry(width=41)
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(0, "123@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Button
generate_btn = Button(text="Generate Password", command=generate_password)
generate_btn.grid(column=2, row=3)
add_btn = Button(text="Add", width=36, command=save_entry)
add_btn.grid(column=1, row=4, columnspan=2)
search_btn = Button(text="Search", width=16, command=find_password)
search_btn.grid(column=2, row=1)

window.mainloop()