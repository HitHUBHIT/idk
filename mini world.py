    import tkinter as tk
from tkinter import filedialog, colorchooser, messagebox
from tkinter.font import Font

# License
LICENSE = """
Mini World - A simple text editor
Created by HitHUBHIT
GitHub: https://github.com/HitHUBHIT

Licensed under the MIT License.
"""

def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_editor.get(1.0, tk.END))

def change_text_color():
    color = colorchooser.askcolor(title="Choose Text Color")[1]
    if color:
        text_editor.config(fg=color)

def change_background_color():
    color = colorchooser.askcolor(title="Choose Background Color")[1]
    if color:
        text_editor.config(bg=color)

def toggle_bold():
    current_font = Font(font=text_editor["font"])
    new_font = Font(weight="bold") if current_font["weight"] != "bold" else Font(weight="normal")
    text_editor.configure(font=new_font)

def toggle_italic():
    current_font = Font(font=text_editor["font"])
    new_font = Font(slant="italic") if current_font["slant"] != "italic" else Font(slant="roman")
    text_editor.configure(font=new_font)

def show_about():
    messagebox.showinfo("About Mini World", LICENSE)

# Main application
root = tk.Tk()
root.title("Mini World - Text Editor")

# Menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# Edit menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Bold", command=toggle_bold)
edit_menu.add_command(label="Italic", command=toggle_italic)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Format menu
format_menu = tk.Menu(menu_bar, tearoff=0)
format_menu.add_command(label="Change Text Color", command=change_text_color)
format_menu.add_command(label="Change Background Color", command=change_background_color)
menu_bar.add_cascade(label="Format", menu=format_menu)

# Help menu
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=show_about)
menu_bar.add_cascade(label="Help", menu=help_menu)

# Text editor
text_editor = tk.Text(root, wrap="word", font=("Arial", 12))
text_editor.pack(expand=1, fill="both")

# Run the application
root.mainloop()
