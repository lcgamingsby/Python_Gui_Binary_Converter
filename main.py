import tkinter as tk
from tkinter import messagebox


def convert():
    try:
        # Get the selected input format from the radio button
        input_format = format_var.get()

        # Get the input value from the entry field
        input_value = entry_input.get()

        if not input_value:
            raise ValueError("Input cannot be empty")

        # Convert the input to decimal based on the selected format
        if input_format == "binary":
            decimal_value = int(input_value, 2)
        elif input_format == "decimal":
            decimal_value = int(input_value)
        elif input_format == "hexadecimal":
            decimal_value = int(input_value, 16)
        elif input_format == "octal":
            decimal_value = int(input_value, 8)
        else:
            raise ValueError("Invalid format selected")

        # Convert from decimal to other formats
        entry_binary.delete(0, tk.END)
        entry_binary.insert(0, bin(decimal_value)[2:])

        entry_decimal.delete(0, tk.END)
        entry_decimal.insert(0, str(decimal_value))

        entry_hexadecimal.delete(0, tk.END)
        entry_hexadecimal.insert(0, hex(decimal_value)[2:].upper())

        entry_octal.delete(0, tk.END)
        entry_octal.insert(0, oct(decimal_value)[2:])

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid input values.")


def main():
    global entry_input, entry_binary, entry_decimal, entry_hexadecimal, entry_octal, format_var

    # Create the main window
    root = tk.Tk()
    root.title("Converter")

    # Frame for selecting input format
    frame_format = tk.Frame(root)
    frame_format.pack(pady=10)

    format_var = tk.StringVar(value="decimal")
    tk.Radiobutton(frame_format, text="Binary", variable=format_var, value="binary").pack(anchor=tk.W)
    tk.Radiobutton(frame_format, text="Decimal", variable=format_var, value="decimal").pack(anchor=tk.W)
    tk.Radiobutton(frame_format, text="Hexadecimal", variable=format_var, value="hexadecimal").pack(anchor=tk.W)
    tk.Radiobutton(frame_format, text="Octal", variable=format_var, value="octal").pack(anchor=tk.W)

    # Frame for input
    frame_input = tk.Frame(root)
    frame_input.pack(pady=10)

    tk.Label(frame_input, text="Input:").grid(row=0, column=0, padx=5, pady=5)
    entry_input = tk.Entry(frame_input)
    entry_input.grid(row=0, column=1, padx=5, pady=5)

    # Frame for binary, decimal, hexadecimal, and octal outputs
    frame_output = tk.Frame(root)
    frame_output.pack(pady=10)

    tk.Label(frame_output, text="Binary:").grid(row=0, column=0, padx=5, pady=5)
    entry_binary = tk.Entry(frame_output)
    entry_binary.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(frame_output, text="Decimal:").grid(row=1, column=0, padx=5, pady=5)
    entry_decimal = tk.Entry(frame_output)
    entry_decimal.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(frame_output, text="Hexadecimal:").grid(row=2, column=0, padx=5, pady=5)
    entry_hexadecimal = tk.Entry(frame_output)
    entry_hexadecimal.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(frame_output, text="Octal:").grid(row=3, column=0, padx=5, pady=5)
    entry_octal = tk.Entry(frame_output)
    entry_octal.grid(row=3, column=1, padx=5, pady=5)

    # Conversion button
    btn_convert = tk.Button(root, text="Convert", command=convert)
    btn_convert.pack(pady=20)

    # Run the application
    root.mainloop()


if __name__ == "__main__":
    main()
