import tkinter as tk
from tkinter import messagebox
import math

# Toggle state for degrees and radians
is_degrees = True

def calculate():
    """Evaluate the expression in the entry field."""
    global is_degrees
    try:
        expression = entry.get()
        # Replace constants and adapt for degrees/radians
        expression = expression.replace("π", str(math.pi))
        expression = expression.replace("e", str(math.e))
        if is_degrees:
            expression = expression.replace("sin(", "math.sin(math.radians(")
            expression = expression.replace("cos(", "math.cos(math.radians(")
            expression = expression.replace("tan(", "math.tan(math.radians(")
            expression = expression.replace("asin(", "math.degrees(math.asin(")
            expression = expression.replace("acos(", "math.degrees(math.acos(")
            expression = expression.replace("atan(", "math.degrees(math.atan(")
        else:
            expression = expression.replace("sin(", "math.sin(")
            expression = expression.replace("cos(", "math.cos(")
            expression = expression.replace("tan(", "math.tan(")
            expression = expression.replace("asin(", "math.asin(")
            expression = expression.replace("acos(", "math.acos(")
            expression = expression.replace("atan(", "math.atan(")
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        messagebox.showerror("Error", f"Invalid Expression: {e}")

def add_to_expression(value):
    """Add a value at the current cursor position in the entry field."""
    current_text = entry.get()
    cursor_index = entry.index(tk.INSERT)  # Get current cursor position
    new_text = current_text[:cursor_index] + value + current_text[cursor_index:]
    entry.delete(0, tk.END)
    entry.insert(0, new_text)

def clear_entry():
    """Clear the entry field."""
    entry.delete(0, tk.END)

def backspace():
    """Remove the character before the cursor."""
    current_text = entry.get()
    cursor_index = entry.index(tk.INSERT)
    if cursor_index > 0:  # Ensure there's a character to delete
        new_text = current_text[:cursor_index-1] + current_text[cursor_index:]
        entry.delete(0, tk.END)
        entry.insert(0, new_text)
        entry.icursor(cursor_index-1)  # Move cursor back one step

def toggle_degrees_radians():
    """Toggle between degrees and radians mode."""
    global is_degrees
    is_degrees = not is_degrees
    mode_button.config(text="Degrees" if is_degrees else "Radians")

# Create the main window
root = tk.Tk()
root.title("Advanced Scientific Calculator")
root.geometry("500x850")
root.config(bg="#1a1a1a")  # Background color

# Entry widget for input and output
entry = tk.Entry(root, font=("Arial", 24), borderwidth=2, relief=tk.RIDGE, justify='right', bg="#333333", fg="#ffffff", insertbackground="white")
entry.grid(row=0, column=0, columnspan=6, padx=10, pady=20)

# Button labels
buttons = [
    ('7', '8', '9', '/', 'sqrt', 'log'),
    ('4', '5', '6', '*', '^', 'ln'),
    ('1', '2', '3', '-', '!', '%'),
    ('0', '.', '=', '+', 'π', 'e'),
    ('sin', 'cos', 'tan', 'asin', 'acos', 'atan'),
    ('(', ')', 'clear', 'back', 'deg', 'rad')
]

# Button colors
button_bg = "#2a2a2a"
button_fg = "#ffffff"
button_highlight = "#f39c12"

# Create buttons dynamically
for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        if text == "=":
            btn = tk.Button(root, text=text, width=6, height=2, font=("Arial", 18), bg=button_highlight, fg=button_fg, command=calculate)
        elif text == "clear":
            btn = tk.Button(root, text=text, width=6, height=2, font=("Arial", 18), bg=button_bg, fg=button_fg, command=clear_entry)
        elif text == "back":
            btn = tk.Button(root, text=text, width=6, height=2, font=("Arial", 18), bg=button_bg, fg=button_fg, command=backspace)
        elif text == "deg":
            btn = tk.Button(root, text=text, width=6, height=2, font=("Arial", 18), bg=button_bg, fg=button_fg, command=lambda: add_to_expression("math.degrees("))
        elif text == "rad":
            btn = tk.Button(root, text=text, width=6, height=2, font=("Arial", 18), bg=button_bg, fg=button_fg, command=lambda: add_to_expression("math.radians("))
        elif text == "sqrt":
            btn = tk.Button(root, text=text, width=6, height=2, font=("Arial", 18), bg=button_bg, fg=button_fg, command=lambda: add_to_expression("math.sqrt("))
        elif text == "log":
            btn = tk.Button(root, text=text, width=6, height=2, font=("Arial", 18), bg=button_bg, fg=button_fg, command=lambda: add_to_expression("math.log10("))
        elif text == "ln":
            btn = tk.Button(root, text=text, width=6, height=2, font=("Arial", 18), bg=button_bg, fg=button_fg, command=lambda: add_to_expression("math.log("))
        elif text == "!":
            btn = tk.Button(root, text=text, width=6, height=2, font=("Arial", 18), bg=button_bg, fg=button_fg, command=lambda: add_to_expression("math.factorial("))
        elif text == "^":
            btn = tk.Button(root, text=text, width=6, height=2, font=("Arial", 18), bg=button_bg, fg=button_fg, command=lambda: add_to_expression("**"))
        elif text in ['sin', 'cos', 'tan', 'asin', 'acos', 'atan']:
            btn = tk.Button(root, text=text, width=6, height=2, font=("Arial", 18), bg=button_bg, fg=button_fg,
                            command=lambda t=text: add_to_expression(f"{t}("))
        elif text == 'π' or text == 'e':
            btn = tk.Button(root, text=text, width=6, height=2, font=("Arial", 18), bg=button_bg, fg=button_fg,
                            command=lambda t=text: add_to_expression(t))
        else:
            btn = tk.Button(root, text=text, width=6, height=2, font=("Arial", 18), bg=button_bg, fg=button_fg,
                            command=lambda t=text: add_to_expression(t))
        btn.grid(row=i + 1, column=j, padx=5, pady=5)

# Degrees/Radians mode button
mode_button = tk.Button(root, text="Degrees", width=8, height=2, font=("Arial", 18), bg="#3498db", fg="#ffffff", command=toggle_degrees_radians)
mode_button.grid(row=7, column=5, padx=10, pady=10)

# Start the main event loop
root.mainloop()
