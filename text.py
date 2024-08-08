import tkinter as tk
from tkinter import filedialog

def save_file():
    file_content = text_area.get("1.0", tk.END)
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt"),
                                                        ("All files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(file_content)

# Create the main window
root = tk.Tk()
root.title("Simple Text Editor")

# Create a text area
text_area = tk.Text(root, wrap='word', width=50, height=20)
text_area.pack(pady=10, padx=10)

# Create a button to save the text to a file
save_button = tk.Button(root, text="Save", command=save_file)
save_button.pack(pady=5)

# Run the application
root.mainloop()
