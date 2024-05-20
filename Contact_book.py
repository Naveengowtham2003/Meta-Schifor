import tkinter as tk
from tkinter import messagebox

def get_selected_contact():
    selected_name = name_entry.get()
    selected_number = number_entry.get()
    if selected_name and selected_number:
        messagebox.showinfo("Selected Contact", f"Name: {selected_name}\nNumber: {selected_number}")
    else:
        messagebox.showwarning("No Contact Selected", "Please enter a name and number first.")

def add_contact():
    contact_name = name_entry.get()
    contact_number = number_entry.get()
    if contact_name and contact_number:
        contacts.append((contact_name, contact_number))
        messagebox.showinfo("Contact Added", f"Contact '{contact_name}' added successfully.")
    else:
        messagebox.showwarning("Incomplete Information", "Please enter both name and number.")


def view_contact():
    if not contacts:
        messagebox.showinfo("No Contacts", "No contacts added yet.")
    else:
        contact_list = "\n".join([f"Name: {name}, Number: {number}" for name, number in contacts])
        messagebox.showinfo("All Contacts", contact_list)


def edit_contact():
    selected_name = name_entry.get()
    selected_number = number_entry.get()
    if selected_name and selected_number:
        for i, (name, number) in enumerate(contacts):
            if name == selected_name:
                contacts[i] = (selected_name, selected_number)
                messagebox.showinfo("Contact Edited", f"Contact '{selected_name}' edited successfully.")
                return
        messagebox.showwarning("Contact Not Found", f"Contact '{selected_name}' not found.")
    else:
        messagebox.showwarning("Incomplete Information", "Please enter both name and number.")

def reset_fields():
    name_entry.delete(0, tk.END)
    number_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Address/Contact Book")

contacts = []
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, sticky=tk.E)

name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

number_label = tk.Label(root, text="Number:")
number_label.grid(row=1, column=0, sticky=tk.E)
number_entry = tk.Entry(root)
number_entry.grid(row=1, column=1)
get_selected_btn = tk.Button(root, text="Get Selected Contact", command=get_selected_contact)
get_selected_btn.grid(row=2, column=0, columnspan=2, pady=5)
add_btn = tk.Button(root, text="Add a contact", command=add_contact)
add_btn.grid(row=3, column=0, columnspan=2, pady=5)
edit_btn = tk.Button(root, text="Edit a contact", command=edit_contact)
edit_btn.grid(row=4, column=0, columnspan=2, pady=5)
view_btn = tk.Button(root, text="View a contact", command=view_contact)
view_btn.grid(row=5, column=0, columnspan=2, pady=5)
exit_btn = tk.Button(root, text="Exit", command=root.quit)
exit_btn.grid(row=6, column=0, columnspan=2, pady=5)
reset_btn = tk.Button(root, text="Reset", command=reset_fields)
reset_btn.grid(row=7, column=0, columnspan=2, pady=5)
root.mainloop()
