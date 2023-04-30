
import sqlite3
import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Construction Site Management")
root.geometry("400x300")

# Create a database connection and cursor
conn = sqlite3.connect("construction.db")
cursor = conn.cursor()

# Create a table for workers if it does not exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS workers (
    id INTEGER PRIMARY KEY,
    name TEXT,
    position TEXT,
    phone TEXT
)
""")

# Create a table for materials if it does not exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS materials (
    id INTEGER PRIMARY KEY,
    name TEXT,
    quantity INTEGER
)
""")

# Function to add a worker to the database
def add_worker():
    # Get the values from the form
    name = name_var.get()
    position = position_var.get()
    phone = phone_var.get()

    # Insert the values into the workers table
    cursor.execute("INSERT INTO workers (name, position, phone) VALUES (?, ?, ?)", (name, position, phone))
    conn.commit()

    # Clear the form and show a success message
    name_var.set("")
    position_var.set("")
    phone_var.set("")
    messagebox.showinfo("Success", "Worker added to the database")

# Function to add a material to the database
def add_material():
    # Get the values from the form
    name = material_var.get()
    quantity = quantity_var.get()

    # Insert the values into the materials table
    cursor.execute("INSERT INTO materials (name, quantity) VALUES (?, ?)", (name, quantity))
    conn.commit()

    # Clear the form and show a success message
    material_var.set("")
    quantity_var.set("")
    messagebox.showinfo("Success", "Material added to the database")

# Function to view workers in the database
def view_workers():
    # Create a new window
    view_window = tk.Toplevel(root)
    view_window.title("Workers")

    # Create a listbox to display the workers
    listbox = tk.Listbox(view_window)
    listbox.pack()

    # Get the workers from the database and add them to the listbox
    cursor.execute("SELECT * FROM workers")
    workers = cursor.fetchall()
    for worker in workers:
        listbox.insert(tk.END, f"{worker[0]} - {worker[1]} - {worker[2]} - {worker[3]}")

# Function to view materials in the database
def view_materials():
    # Create a new window
    view_window = tk.Toplevel(root)
    view_window.title("Materials")

    # Create a listbox to display the materials
    listbox = tk.Listbox(view_window)
    listbox.pack()

    # Get the materials from the database and add them to the listbox
    cursor.execute("SELECT * FROM materials")
    materials = cursor.fetchall()
    for material in materials:
        listbox.insert(tk.END, f"{material[0]} - {material[1]} - {material[2]}")

# Create the form to add a worker
name_label = tk.Label(root, text="Name")
name_label.pack()
name_var = tk.StringVar()
name_entry = tk.Entry(root, textvariable=name_var)
name_entry.pack()

position_label = tk.Label(root, text="Position")
position_label.pack()
position_var = tk.StringVar()
position_entry = tk.Entry(root, textvariable=position_var)
position_entry.pack()

phone_label = tk.Label(root, text="Phone")
phone_label.pack()
phone_var = tk.StringVar()
phone_entry = tk.Entry
