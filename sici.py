import tkinter as tk
from tkinter import ttk

def calculate_interest():
    principal = principal_scale.get()
    rate = rate_scale.get() / 100
    time = time_scale.get()

    if interest_type.get() == "Simple":
        interest = (principal * rate * time) / 100
    else:
        interest = principal * ((1 + rate) ** time - 1)

    interest_scale.set(interest)

root = tk.Tk()
root.title("Interest Calculator")

# Principal
principal_label = ttk.Label(root, text="Principal:")
principal_label.grid(row=0, column=0, padx=10, pady=5)
principal_scale = ttk.Scale(root, from_=0, to=10000, orient=tk.HORIZONTAL, length=200)
principal_scale.grid(row=0, column=1, padx=10, pady=5)
principal_scale.set(5000)
principal_scale.set(1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000)

# Rate
rate_label = ttk.Label(root, text="Rate (%):")
rate_label.grid(row=1, column=0, padx=10, pady=5)
rate_scale = ttk.Scale(root, from_=0, to=20, orient=tk.HORIZONTAL, length=200)
rate_scale.grid(row=1, column=1, padx=10, pady=5)
rate_scale.set(10)
rate_scale.set(5, 10, 15, 20)

# Time
time_label = ttk.Label(root, text="Time (years):")
time_label.grid(row=2, column=0, padx=10, pady=5)
time_scale = ttk.Scale(root, from_=0, to=50, orient=tk.HORIZONTAL, length=200)
time_scale.grid(row=2, column=1, padx=10, pady=5)
time_scale.set(20)
time_scale.set(10, 20, 30, 40, 50)

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
interest_scale = ttk.Scale(root, from_=0, to=5000, orient=tk.HORIZONTAL, length=200)
interest_scale.grid(row=5, column=1, columnspan=2, padx=10, pady=5)
interest_scale.set(2500)
interest_scale.set(1000, 2000, 3000, 4000, 5000)

root.mainloop()
