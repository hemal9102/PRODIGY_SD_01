import tkinter as tk
from tkinter import messagebox

def cel_to_fah(cel):
    return (cel * 9/5)+32

def cel_to_kel(cel):
    return cel + 273.15
def fah_to_cel(fah):
    return (fah - 32) * 5/9

def fah_to_kel(fah):
    return (fah - 32) * 5/9 + 273.15

def kel_to_cel(kel):
    return kelvin - 273.15

def kel_to_fah(kel):
    return (kel - 273.15) * 9/5 +32

def temp_converter():
    try:
        temp_value = float(entry_temp.get())
        temp_unit = combo_unit.get().upper()

        if temp_unit == 'C':
            fahrenheit = cel_to_fah(temp_value)
            kelvin = cel_to_kel(temp_value)
            result_label.config(text=f"{temp_value}C = {fahrenheit:.2f}F and {kelvin:.2f}K")
        elif temp_unit == 'F':
            celcius = fah_to_cel(temp_value)
            kelvin = fah_to_kel(temp_value)
            result_label.config(text=f"{temp_value}F = {celcius:.2f}C and {kelvin:.2f}K")
        elif temp_unit == 'K':
            celcius = kel_to_cel(temp_value)
            fahrenheit = kel_to_fah(temp_value)
            result_label.config(text=f"{temp_value}K = {celcius:.2f}C and {fahrenheit:.2f}F")
        else:
            messagebox.showerror("Invalid input","Please use C for Celsius, F for Fahrenheit, or K for Kelvin.")
    except ValueError:
        messagebox.showerror("Invalid Input","Please use this input 273.15K,0C,0F ")

root = tk.Tk()
root.title("Temprature Converter")
root.geometry("400x300")

#label
input_label = tk.Label(root,text="Enter Temperature Value:")
input_label.pack(pady=15)

entry_temp = tk.Entry(root)
entry_temp.pack(pady=12)

combo_unit = tk.StringVar()
unit_options = ['C','F','K']
combo_unit.set(unit_options[0])#defualt is celcius
unit_menu = tk.OptionMenu(root, combo_unit,*unit_options)
unit_menu.pack(pady=10)

convert_button = tk.Button(root, text="Convert", command=temp_converter)
convert_button.pack(pady=10)

# Label to display result
result_label = tk.Label(root, text="Converted Values will appear here", font=("Helvetica", 12))
result_label.pack(pady=20)

# Start the main loop
root.mainloop()