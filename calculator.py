import tkinter as tk
import math

def on_button_click(char):
    if char == '=':
        try:
            result = eval(display.get())
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    elif char == 'C':
        display.delete(0, tk.END)
    elif char == '√':
        try:
            result = math.sqrt(eval(display.get()))
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    elif char == '^':
        display.insert(tk.END, '**')
    elif char == 'pi':
        display.insert(tk.END, str(math.pi))
    elif char in ['sin', 'cos', 'tan']:
        try:
            result = eval('math.' + char + '(' + display.get() + ')')
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    else:
        display.insert(tk.END, char)

root = tk.Tk()
root.title("Advanced Calculator")

display = tk.Entry(root, width=30, font=('Arial', 14))
display.grid(row=0, column=0, columnspan=5)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('C', 1, 4),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('(', 2, 4),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), (')', 3, 4),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3), ('√', 4, 4),
    ('^', 5, 0), ('pi', 5, 1), ('sin', 5, 2), ('cos', 5, 3), ('tan', 5, 4)
]

for (text, row, col) in buttons:
    b = tk.Button(root, text=text, width=5, height=2, font=('Arial', 12), command=lambda t=text: on_button_click(t))
    b.grid(row=row, column=col)

root.mainloop()
