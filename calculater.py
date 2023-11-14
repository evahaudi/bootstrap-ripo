import tkinter as tk

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                result = "Cannot divide by zero!"
            else:
                result = num1 / num2

        result_label.config(text="Result: " + str(result))
    except ValueError:
        result_label.config(text="Please enter valid numbers")

# Create the main window
root = tk.Tk()
root.title("Styled Calculator")

# Styling properties
root.configure(bg="#f8f9fa")  # Background color

# Function to apply common styles to buttons
def apply_button_style(widget):
    widget.config(bg="#007bff", fg="white", font=("Arial", 12), padx=10, pady=5)

# Entry fields
entry1 = tk.Entry(root, font=("Arial", 12))
entry1.pack(pady=5)
entry2 = tk.Entry(root, font=("Arial", 12))
entry2.pack(pady=5)

# Operation selection
operation_var = tk.StringVar(root)
operation_var.set("+")
operations = ["+", "-", "*", "/"]
operation_dropdown = tk.OptionMenu(root, operation_var, *operations)
apply_button_style(operation_dropdown)  # Apply button style
operation_dropdown.pack(pady=5)

# Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
apply_button_style(calculate_button)  # Apply button style
calculate_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="Result: ", bg="#f8f9fa", font=("Arial", 12))
result_label.pack(pady=5)

root.mainloop()
