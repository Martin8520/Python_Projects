import tkinter as tk
from tkinter import messagebox
import math

def calculate_costs():
    try:
        driver_pay = float(entry_driver_pay.get())
        fuel_surcharge = float(entry_fuel_surcharge.get())
        line_haul = float(entry_line_haul.get())
        number_of_containers = int(entry_num_containers.get())

        if number_of_containers <= 0:
            messagebox.showerror("Error", "Number of containers must be greater than 0.")
            return

        def round_down(value):
            return math.floor(value * 100) / 100

        dp_per = round_down(driver_pay / number_of_containers)
        fs_per = round_down(fuel_surcharge / number_of_containers)
        lh_per = round_down(line_haul / number_of_containers)

        dp_total_1_to_n_minus_1 = dp_per * (number_of_containers - 1)
        fs_total_1_to_n_minus_1 = fs_per * (number_of_containers - 1)
        lh_total_1_to_n_minus_1 = lh_per * (number_of_containers - 1)

        dp_remainder = round(driver_pay - dp_total_1_to_n_minus_1 - dp_per, 2)
        fs_remainder = round(fuel_surcharge - fs_total_1_to_n_minus_1 - fs_per, 2)
        lh_remainder = round(line_haul - lh_total_1_to_n_minus_1 - lh_per, 2)

        if dp_remainder == 0 and fs_remainder == 0 and lh_remainder == 0:
            result = (
                f"All {number_of_containers} containers:\n"
                f"  Driver Pay: ${dp_per:.2f}\n"
                f"  Fuel Surcharge: ${fs_per:.2f}\n"
                f"  Line Haul: ${lh_per:.2f}"
            )
        else:
            dp_last = round_down(dp_per + dp_remainder + fs_remainder)
            lh_last = round_down(lh_per + lh_remainder + fs_remainder)
            fs_last = fs_per

            result = (
                f"Containers 1 to {number_of_containers - 1}:\n"
                f"  Driver Pay: ${dp_per:.2f}\n"
                f"  Fuel Surcharge: ${fs_per:.2f}\n"
                f"  Line Haul: ${lh_per:.2f}\n\n"
                f"Container {number_of_containers} (with remainders):\n"
                f"  Driver Pay: ${dp_last:.2f}\n"
                f"  Fuel Surcharge: ${fs_last:.2f} (unchanged)\n"
                f"  Line Haul: ${lh_last:.2f}"
            )

        result_text.set(result)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values.")


root = tk.Tk()
root.title("Container Cost Calculator")
root.geometry("450x500")

tk.Label(root, text="Driver Pay (USD):").pack(pady=5)
entry_driver_pay = tk.Entry(root)
entry_driver_pay.pack(pady=5)

tk.Label(root, text="Fuel Surcharge (USD):").pack(pady=5)
entry_fuel_surcharge = tk.Entry(root)
entry_fuel_surcharge.pack(pady=5)

tk.Label(root, text="Line Haul (USD):").pack(pady=5)
entry_line_haul = tk.Entry(root)
entry_line_haul.pack(pady=5)

tk.Label(root, text="Number of Containers:").pack(pady=5)
entry_num_containers = tk.Entry(root)
entry_num_containers.pack(pady=5)

tk.Button(root, text="Calculate", command=calculate_costs).pack(pady=20)

result_text = tk.StringVar()
tk.Label(root, textvariable=result_text, justify="left").pack(pady=10)

root.mainloop()
