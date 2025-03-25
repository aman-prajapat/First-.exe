import tkinter as tk
from tkinter import ttk, messagebox
import test1
# Dictionary to store employee data (Employee ID -> Employee Details)
employees = {}

# Function to add an employee
def add_employee():
    emp_id = entry_id.get()
    name = entry_name.get()
    email = entry_email.get()
    mobile = entry_mobile.get()
    post = entry_post.get()

    test1.add(emp_id,name,mobile,email,post)
    messagebox.showinfo("Success",f"Employee added")

        # messagebox.showwarning("Error", "All fields are required!")

# Function to remove an employee
def remove_employee():
    emp_id = entry_remove_id.get()
    test1.remove(emp_id)
    messagebox.showinfo("Success", f"Employee {emp_id} removed!")


# Function to promote an employee
def promote_employee():
    emp_id = entry_promote_id.get()
    new_post = entry_new_post.get()

    test1.promote(new_post,emp_id)
    messagebox.showinfo("Success", f"Employee {emp_id} promoted")
   

# Function to display an employee's details
def display_employee():
    emp_id = entry_display_id.get()
    info = test1.display(emp_id)
    if info:
        emp_details = f"ID: {info[0]}\nName: {info[1]}\nMobile: {info[2]}\nEmail: {info[3]}\nPost: {info[4]}"
        messagebox.showinfo("Employee Details", emp_details)
    else:
        messagebox.showwarning("Error", "Employee ID not found!")

    
# Create the main window
root = tk.Tk()
root.title("Employee Management System")
root.geometry("500x450")

# Create a notebook (tab container)
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

### TAB 1: Add Employee ###
tab_add = tk.Frame(notebook, bg="lightblue")
notebook.add(tab_add, text="Add Employee")

tk.Label(tab_add, text="Employee ID:", bg="lightblue").pack(pady=5)
entry_id = tk.Entry(tab_add)
entry_id.pack(pady=5)

tk.Label(tab_add, text="Name:", bg="lightblue").pack(pady=5)
entry_name = tk.Entry(tab_add)
entry_name.pack(pady=5)

tk.Label(tab_add, text="Email:", bg="lightblue").pack(pady=5)
entry_email = tk.Entry(tab_add)
entry_email.pack(pady=5)

tk.Label(tab_add, text="Mobile No:", bg="lightblue").pack(pady=5)
entry_mobile = tk.Entry(tab_add)
entry_mobile.pack(pady=5)

tk.Label(tab_add, text="Post:", bg="lightblue").pack(pady=5)
entry_post = tk.Entry(tab_add)
entry_post.pack(pady=5)

tk.Button(tab_add, text="Add Employee", command=add_employee).pack(pady=10)

### TAB 2: Remove Employee ###
tab_remove = tk.Frame(notebook, bg="lightcoral")
notebook.add(tab_remove, text="Remove Employee")

tk.Label(tab_remove, text="Enter Employee ID to Remove:", bg="lightcoral").pack(pady=5)
entry_remove_id = tk.Entry(tab_remove)
entry_remove_id.pack(pady=5)

tk.Button(tab_remove, text="Remove Employee", command=remove_employee).pack(pady=10)

### TAB 3: Promote Employee ###
tab_promote = tk.Frame(notebook, bg="lightgreen")
notebook.add(tab_promote, text="Promote Employee")

tk.Label(tab_promote, text="Enter Employee ID:", bg="lightgreen").pack(pady=5)
entry_promote_id = tk.Entry(tab_promote)
entry_promote_id.pack(pady=5)

tk.Label(tab_promote, text="New Post:", bg="lightgreen").pack(pady=5)
entry_new_post = tk.Entry(tab_promote)
entry_new_post.pack(pady=5)

tk.Button(tab_promote, text="Promote Employee", command=promote_employee).pack(pady=10)

### TAB 4: Display Employee ###
tab_display = tk.Frame(notebook, bg="lightyellow")
notebook.add(tab_display, text="Display Employee")

tk.Label(tab_display, text="Enter Employee ID to Display:", bg="lightyellow").pack(pady=5)
entry_display_id = tk.Entry(tab_display)
entry_display_id.pack(pady=5)

tk.Button(tab_display, text="Show Details", command=display_employee).pack(pady=10)

# Run the application
root.mainloop()
