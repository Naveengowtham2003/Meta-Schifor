import tkinter as tk
from tkinter import ttk


def submit():
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    address = address_text.get("1.0", tk.END)
    email = email_entry.get()
    contact = contact_entry.get()
    country = country_entry.get()
    state = state_entry.get()
    diseases = [disease_var.get() for disease_var in disease_vars if disease_var.get()]

    print("Name:", name)
    print("Age:", age)
    print("Gender:", gender)
    print("Address:", address)
    print("Email:", email)
    print("Contact No:", contact)
    print("Country:", country)
    print("State:", state)
    print("Diseases:", diseases)


root = tk.Tk()
root.title("COVID Vaccine Registration Form")

name_label = ttk.Label(root, text="Name:")
name_label.grid(row=0, column=0, sticky=tk.W)
name_entry = ttk.Entry(root)
name_entry.grid(row=0, column=1)

age_label = ttk.Label(root, text="Age:")
age_label.grid(row=1, column=0, sticky=tk.W)
age_entry = ttk.Entry(root)
age_entry.grid(row=1, column=1)

gender_label = ttk.Label(root, text="Gender:")
gender_label.grid(row=2, column=0, sticky=tk.W)
gender_var = tk.StringVar()
gender_male_radio = ttk.Radiobutton(root, text="Male", variable=gender_var, value="Male")
gender_male_radio.grid(row=2, column=1, sticky=tk.W)
gender_female_radio = ttk.Radiobutton(root, text="Female", variable=gender_var, value="Female")
gender_female_radio.grid(row=2, column=2, sticky=tk.W)

address_label = ttk.Label(root, text="Address:")
address_label.grid(row=3, column=0, sticky=tk.W)
address_text = tk.Text(root, height=5, width=30)
address_text.grid(row=3, column=1, columnspan=2)

email_label = ttk.Label(root, text="Email:")
email_label.grid(row=4, column=0, sticky=tk.W)
email_entry = ttk.Entry(root)
email_entry.grid(row=4, column=1)

contact_label = ttk.Label(root, text="Contact No:")
contact_label.grid(row=5, column=0, sticky=tk.W)
contact_entry = ttk.Entry(root)
contact_entry.grid(row=5, column=1)

country_label = ttk.Label(root, text="Country:")
country_label.grid(row=6, column=0, sticky=tk.W)
country_entry = ttk.Entry(root)
country_entry.grid(row=6, column=1)

state_label = ttk.Label(root, text="State:")
state_label.grid(row=7, column=0, sticky=tk.W)
state_entry = ttk.Entry(root)
state_entry.grid(row=7, column=1)

disease_label = ttk.Label(root, text="Select If you are having any following disease:")
disease_label.grid(row=8, column=0, sticky=tk.W)
disease_vars = [tk.BooleanVar() for _ in range(4)]
disease_checkboxes = [ttk.Checkbutton(root, text=disease, variable=disease_var) for disease, disease_var in
                      zip(["Cold", "Cough", "Fever", "Headache"], disease_vars)]
for i, checkbox in enumerate(disease_checkboxes):
    checkbox.grid(row=8 + i, column=1, columnspan=2, sticky=tk.W)

submit_button = ttk.Button(root, text="Submit", command=submit)
submit_button.grid(row=12, columnspan=3)

root.mainloop()
