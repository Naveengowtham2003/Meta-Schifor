import tkinter as tk
from tkinter import messagebox


class Student:
    def __init__(self, roll_no, name, age):
        self.roll_no = roll_no
        self.name = name
        self.age = age

    def __str__(self):
        return f"Roll No: {self.roll_no}, Name: {self.name}, Age: {self.age}"


class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, roll_no, name, age):
        student = Student(roll_no, name, age)
        self.students.append(student)

    def display_students(self):
        if not self.students:
            messagebox.showinfo("Info", "No students registered yet.")
            return
        student_info = "\n".join(str(student) for student in self.students)
        messagebox.showinfo("Student Details", student_info)

    def search_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                messagebox.showinfo("Student Details", str(student))
                return
        messagebox.showinfo("Info", "Student not found.")

    def delete_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                self.students.remove(student)
                messagebox.showinfo("Info", "Student deleted successfully.")
                return
        messagebox.showinfo("Info", "Student not found.")

    def update_student(self, roll_no, name, age):
        for student in self.students:
            if student.roll_no == roll_no:
                student.name = name
                student.age = age
                messagebox.showinfo("Info", "Student details updated successfully.")
                return
        messagebox.showinfo("Info", "Student not found.")


def add_student_details():
    roll_no = int(entry_roll_no.get())
    name = entry_name.get()
    age = int(entry_age.get())
    sms.add_student(roll_no, name, age)


def display_student_details():
    sms.display_students()


def search_student_details():
    roll_no = int(entry_roll_no.get())
    sms.search_student(roll_no)


def delete_student_details():
    roll_no = int(entry_roll_no.get())
    sms.delete_student(roll_no)


def update_student_details():
    roll_no = int(entry_roll_no.get())
    name = entry_name.get()
    age = int(entry_age.get())
    sms.update_student(roll_no, name, age)


def clear_fields():
    entry_roll_no.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)


def exit_app():
    root.destroy()


root = tk.Tk()
root.title("Student Management System")

sms = StudentManagementSystem()

label_roll_no = tk.Label(root, text="Roll No:")
label_roll_no.grid(row=0, column=0, padx=5, pady=5)
entry_roll_no = tk.Entry(root)
entry_roll_no.grid(row=0, column=1, padx=5, pady=5)

label_name = tk.Label(root, text="Name:")
label_name.grid(row=1, column=0, padx=5, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=1, column=1, padx=5, pady=5)

label_age = tk.Label(root, text="Age:")
label_age.grid(row=2, column=0, padx=5, pady=5)
entry_age = tk.Entry(root)
entry_age.grid(row=2, column=1, padx=5, pady=5)

button_add = tk.Button(root, text="Add Student", command=add_student_details)
button_add.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="WE")

button_display = tk.Button(root, text="Display Students", command=display_student_details)
button_display.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="WE")

button_search = tk.Button(root, text="Search Student", command=search_student_details)
button_search.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="WE")

button_delete = tk.Button(root, text="Delete Student", command=delete_student_details)
button_delete.grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky="WE")

button_update = tk.Button(root, text="Update Student", command=update_student_details)
button_update.grid(row=7, column=0, columnspan=2, padx=5, pady=5, sticky="WE")

button_clear = tk.Button(root, text="Clear Fields", command=clear_fields)
button_clear.grid(row=8, column=0, columnspan=2, padx=5, pady=5, sticky="WE")

button_exit = tk.Button(root, text="Exit", command=exit_app)
button_exit.grid(row=9, column=0, columnspan=2, padx=5, pady=5, sticky="WE")

root.mainloop()
