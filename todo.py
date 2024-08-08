import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def remove_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)

# Create the main window
root = tk.Tk()
root.title("Simple To-Do List")

# Create an entry widget for entering tasks
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Create a button to add tasks
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

# Create a listbox to display tasks
listbox = tk.Listbox(root, width=30, height=10)
listbox.pack(pady=10)

# Create a button to remove tasks
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack(pady=5)

# Run the application
root.mainloop()
