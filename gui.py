import tkinter as tk
from tkinter import ttk
from src import generator

class PasswordGeneratorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Password Generator")

        # Define color scheme
        self.bg_color = "#2C3E50"  # Dark blue background
        self.fg_color = "#ECF0F1"  # Light text
        self.black = "#000000"
        self.button_color = "#3498DB"  # Blue button color
        self.button_hover_color = "#2980B9"  # Darker blue hover color

        # Configure window style
        master.configure(bg=self.bg_color)
        master.minsize(width=600, height=400)  # Increased minimum height

        # Font customization
        self.font = ("Helvetica", 12)  # Modern font

        # Create style for checkboxes
        self.style = ttk.Style()
        self.style.configure("TCheckbutton", foreground=self.fg_color, background=self.bg_color, font=self.font)

        # Create widgets with styling
        self.length_label = tk.Label(master, text="Password Length:", font=self.font, fg=self.fg_color, bg=self.bg_color)
        self.length_entry = tk.Entry(master, font=self.font, bg=self.bg_color, fg=self.fg_color, highlightthickness=0, highlightbackground=self.fg_color, highlightcolor=self.fg_color)
        self.uppercase_var = tk.IntVar(value=1)  # Pre-select uppercase by default
        self.uppercase_checkbox = ttk.Checkbutton(master, text="Uppercase Letters", variable=self.uppercase_var, style="TCheckbutton")
        self.lowercase_var = tk.IntVar(value=1)  # Pre-select lowercase by default
        self.lowercase_checkbox = ttk.Checkbutton(master, text="Lowercase Letters", variable=self.lowercase_var, style="TCheckbutton")
        self.digits_var = tk.IntVar()
        self.digits_checkbox = ttk.Checkbutton(master, text="Digits", variable=self.digits_var, style="TCheckbutton")
        self.special_var = tk.IntVar()
        self.special_checkbox = ttk.Checkbutton(master, text="Special Characters", variable=self.special_var, style="TCheckbutton")
        self.generate_button = tk.Button(master, text="Generate", command=self.generate_password, font=self.font, bg=self.button_color, fg=self.fg_color, activebackground=self.button_hover_color)
        self.password_label = tk.Label(master, text="Generated Password:", font=self.font, fg=self.fg_color, bg=self.bg_color)
        self.password_entry = tk.Entry(master, font=self.font, bg=self.bg_color, fg=self.black, state="readonly", highlightthickness=0, highlightbackground=self.fg_color, highlightcolor=self.fg_color)

        # Improved widget arrangement using grid with proper spacing
        self.length_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.length_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")
        self.uppercase_checkbox.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.lowercase_checkbox.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.digits_checkbox.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.special_checkbox.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.generate_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
        self.password_label.grid(row=6, column=0, padx=10, pady=10, sticky="w")
        self.password_entry.grid(row=6, column=1, padx=10, pady=10, sticky="ew")

        # Add padding and color variation to the password entry
        self.password_entry.config(highlightbackground=self.bg_color, highlightcolor=self.bg_color)

    def generate_password(self):
        # Get user input and call generator function
        length = int(self.length_entry.get())
        include_uppercase = self.uppercase_var.get()
        include_lowercase = self.lowercase_var.get()
        include_digits = self.digits_var.get()
        include_special_chars = self.special_var.get()

        try:
            password = generator.generate_password(length, include_uppercase, include_lowercase, include_digits, include_special_chars)
            self.password_entry.config(state="normal")  # Enable password display
            self.password_entry.delete(0, tk.END)  # Clear previous password
            self.password_entry.insert(0, password)  # Display generated password
            self.password_entry.config(state="readonly")  # Disable password editing
        except ValueError as e:
            # Handle error (e.g., display error message)
            print(f"Error: {e}")

# Create the main window and run the GUI
root = tk.Tk()
root.resizable(False, False)  # Disable window resizing
gui = PasswordGeneratorGUI(root)
root.mainloop()
