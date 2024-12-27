import tkinter as tk
from tkinter import messagebox

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def convert_temperature():
    try:
        temp_value = float(entry_temp.get())
        temp_unit = combo_unit.get().upper()

        if temp_unit == 'C':
            fahrenheit = celsius_to_fahrenheit(temp_value)
            kelvin = celsius_to_kelvin(temp_value)
            result_label.config(text=f"{temp_value}C = {fahrenheit:.2f}F and {kelvin:.2f}K")
        elif temp_unit == 'F':
            celsius = fahrenheit_to_celsius(temp_value)
            kelvin = fahrenheit_to_kelvin(temp_value)
            result_label.config(text=f"{temp_value}°F = {celsius:.2f}°C and {kelvin:.2f}K")
        elif temp_unit == 'K':
            celsius = kelvin_to_celsius(temp_value)
            fahrenheit = kelvin_to_fahrenheit(temp_value)
            result_label.config(text=f"{temp_value}K = {celsius:.2f}°C and {fahrenheit:.2f}°F")
        else:
            messagebox.showerror("Invalid Input", "Please use C for Celsius, F for Fahrenheit, or K for Kelvin.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# Set up the main window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("400x300")

# Label for input
input_label = tk.Label(root, text="Enter Temperature Value:")
input_label.pack(pady=10)

# Entry field for temperature value
entry_temp = tk.Entry(root)
entry_temp.pack(pady=10)

# Dropdown for units
combo_unit = tk.StringVar()
unit_options = ['C', 'F', 'K']
combo_unit.set(unit_options[0])  # default to Celsius
unit_menu = tk.OptionMenu(root, combo_unit, *unit_options)
unit_menu.pack(pady=10)

# Button to perform the conversion
convert_button = tk.Button(root, text="Convert", command=convert_temperature)
convert_button.pack(pady=10)

# Label to display result
result_label = tk.Label(root, text="Converted Values will appear here", font=("Helvetica", 12))
result_label.pack(pady=20)

# Start the main loop
root.mainloop()
