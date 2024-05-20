import tkinter as tk
from tkinter import ttk

def calculate_interest():
    principal = float(principal_entry.get())
    rate = float(rate_entry.get()) / 100
    time = float(time_entry.get())

    if interest_type.get() == "Simple":
        interest = (principal * rate * time) / 100
    else:
        interest = principal * ((1 + rate) ** time - 1)

    interest_scale.set(interest)
    interest_label.config(text=f"Interest: {interest:.2f}")

root = tk.Tk()
root.title("Interest Calculator")

# Principal
principal_label = ttk.Label(root, text="Principal:")
principal_label.grid(row=0, column=0, padx=10, pady=5)
principal_entry = ttk.Entry(root)
principal_entry.grid(row=0, column=1, padx=10, pady=5)

# Rate
rate_label = ttk.Label(root, text="Rate (%):")
rate_label.grid(row=1, column=0, padx=10, pady=5)
rate_entry = ttk.Entry(root)
rate_entry.grid(row=1, column=1, padx=10, pady=5)

# Time
time_label = ttk.Label(root, text="Time (years):")
time_label.grid(row=2, column=0, padx=10, pady=5)
time_entry = ttk.Entry(root)
time_entry.grid(row=2, column=1, padx=10, pady=5)

# Interest Type
interest_type = tk.StringVar()
interest_type.set("Simple")
interest_label = ttk.Label(root, text="Interest Type:")
interest_label.grid(row=3, column=0, padx=10, pady=5)
simple_radio = ttk.Radiobutton(root, text="Simple", variable=interest_type, value="Simple")
simple_radio.grid(row=3, column=1, padx=10, pady=5)
compound_radio = ttk.Radiobutton(root, text="Compound", variable=interest_type, value="Compound")
compound_radio.grid(row=3, column=2, padx=10, pady=5)

# Calculate Button
calculate_button = ttk.Button(root, text="Calculate", command=calculate_interest)
calculate_button.grid(row=4, columnspan=3, padx=10, pady=10)

# Interest Scale
interest_label = ttk.Label(root, text="Interest:")
interest_label.grid(row=5, column=0, padx=10, pady=5)
interest_scale = ttk.Scale(root, from_=0, to=5000, orient=tk.HORIZONTAL)
interest_scale.grid(row=5, column=1, columnspan=2, padx=10, pady=5)

# Interest Result Label
interest_label = ttk.Label(root, text="Interest: 0.00")
interest_label.grid(row=6, column=0, columnspan=3, padx=10, pady=5)

root.mainloop()
