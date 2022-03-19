from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project

def password_generator():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for char in range(randint(8, 10))]

    password_symbol = [choice(symbols) for char in range(randint(2, 4))]

    password_number = [choice(numbers)for char in range(randint(2, 4))]

    password_list = password_letter + password_symbol + password_number
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(END, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    website_detail = {

            website: {
                "email": email,
                "password": password
            }

    }





    if len(website) == 0 and len(password) == 0:
        messagebox.showwarning(title="Error ", message=f"please you left Website and Password Boxes empty please review ")
    elif len(website) == 0:
        messagebox.showwarning(title="Error ", message=f"please you left Website Box  empty please review ")
    elif len(password) == 0:
        messagebox.showwarning(title="Error ", message=f"please you left Password Box empty please review ")
    else:
        # is_ok = messagebox.askyesno(title="Add Password ", message=f"Your Website: {website}\n Email : {email}\n Password : {password}\n")
        # with open("data.json", "w") as data_file:
        #     json.dump(website_detail, data_file, indent=4)

        # with open("data.json", "r") as data_file:
        #     data = json.load(data_file)
        #     print(data)
        try:
            with open("data.json", "r") as data_file:
                # Read the old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(website_detail, data_file, indent=4)

        else:
            # Update the old data with the new one
            data.update(website_detail)
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- Find Password ------------------------------- #

def search():

    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            fetch_data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showwarning(title="Warning ", message="Data File Is Not Found ")

    else:
        if website in fetch_data:
            Email = fetch_data[website]["email"]
            Password = fetch_data[website]["password"]
            messagebox.showinfo(title=f"Password for {website}", message=f" Email : {Email}\n Password : {Password}\n")

        else:
            messagebox.showwarning(title="oops ", message=f"The {website} has not been Saved \n\n Generate a new one. \n")



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator ")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=1, column=2)

website_label = Label(text="Website")
website_label.grid(row=2, column=1)

email_label = Label(text="Email/ Username")
email_label.grid(row=3, column=1)


password_label = Label(text="Password ")
password_label.grid(row=4, column=1)

# Entry
website_entry = Entry(width=35)
website_entry.grid(row=2, column=2, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.insert(END, "yonni@hotmail.com")
email_entry.grid(row=3, column=2, columnspan=2)
password_entry = Entry(width=35)
password_entry.grid(row=4, column=2, columnspan=2)

# buttons
search_button = Button(text="Search", width=15, command=search)
search_button.grid(row=2, column=3)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=5, column=2, columnspan=2)
password_generator = Button(text="Generate Password", width=15, command=password_generator)
password_generator.grid(row=4, column=3)


























window.mainloop()

