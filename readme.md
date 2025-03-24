# Employee Management System (EXE-Based Software)

## 📌 About the Project

This **Employee Management System** is a standalone desktop application built using **Python (Tkinter)** and **MySQL**. The software allows users to **add, remove, promote, and display employee details**.

### 🔹 Key Features

✅ **GUI-Based Application** – No need for command-line interactions.

✅ **Standalone EXE** – Can be run by double-clicking the `.exe` file.

✅ **MySQL Integration** – Data is stored and managed using MySQL.

✅ **CRUD Operations** – Users can **Create, Read, Update, and Delete** employee records.

---

## 🚀 How to Set Up the Project

### 1️⃣ Install Dependencies

Ensure you have Python installed. Then, install the required packages using:

```bash
pip install mysql-connector-python
```

### 2️⃣ Set Up MySQL Database

1. Open MySQL and create a database named **`test`**.
2. Create a table inside the `test` database with the following schema:

```sql
CREATE TABLE emp (
    employeeId VARCHAR(20) PRIMARY KEY,
    empName VARCHAR(50),
    mobile VARCHAR(10),
    email VARCHAR(100),
    post VARCHAR(50)
);
```

3. Ensure MySQL is running on:
   - **Host:** `localhost`
   - **Port:** `3306`
   - **Username:** `root`
   - **Password:** `0000` (Modify as per your configuration)

### 3️⃣ Run the Application

To start the application, run:

```bash
python main.py
```

OR, if using the EXE:

- Simply **double-click the ********************`.exe`******************** file** to launch the GUI.

---

## 🛠️ Usage Guide

### ➤ Add an Employee

1. Open the **"Add Employee"** tab.
2. Enter Employee ID, Name, Email, Mobile, and Post.
3. Click **"Add Employee"** – The data is stored in MySQL.

### ➤ Remove an Employee

1. Open the **"Remove Employee"** tab.
2. Enter the Employee ID to delete.
3. Click **"Remove Employee"** – The record is deleted from MySQL.

### ➤ Promote an Employee

1. Open the **"Promote Employee"** tab.
2. Enter Employee ID and the new post.
3. Click **"Promote Employee"** – The employee's post is updated.

### ➤ Display Employee Details

1. Open the **"Display Employee"** tab.
2. Enter the Employee ID.
3. Click **"Show Details"** – The employee's information is displayed.

---

## 📂 Project Structure

```
📦 Employee Management System
├── code/
     ├── main.py          # GUI and business logic
     ├── test1.py         # MySQL database operations
├── README.md        # Project documentation
├── main.exe # software
```

---

## 🔥 Improvements & Future Enhancements

✅ **Online Database Support** – Currently, MySQL runs locally; adding cloud support will improve accessibility.

✅ **Search & Filter Options** – Add functionality to search employees by name, department, etc.

✅ **Export Data to Excel** – Allow users to export employee details to a CSV/Excel file.

✅ **Improved UI Design** – Enhance the interface with better styling and layouts.

---

## 📌 Author

👤 **Aman Prajapat**\
🚀 **First Standalone EXE-Based Software!**

💡 If you like this project, don't forget to ⭐ the repository!

