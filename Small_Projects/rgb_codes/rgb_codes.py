import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import csv
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")])
    if file_path:
        image = Image.open(file_path)
        colors = image.getcolors(image.size[0] * image.size[1])
        color_data = [(rgb, count) for count, rgb in colors]
        color_data.sort(reverse=True)

        # Write to CSV
        csv_filename = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if csv_filename:
            with open(csv_filename, "w", newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(["Color", "Count"])
                for rgb, count in color_data:
                    csv_writer.writerow([rgb, count])

        # Update GUI
        colors_listbox.delete(0, tk.END)
        for rgb, count in color_data:
            colors_listbox.insert(tk.END, f"{rgb}: {count}")


def export_to_pdf():
    try:
        csv_filename = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if csv_filename:
            pdf_filename = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
            if pdf_filename:
                data = []
                with open(csv_filename, "r", newline='') as csvfile:
                    csv_reader = csv.reader(csvfile)
                    for row in csv_reader:
                        data.append(row)

                pdf = canvas.Canvas(pdf_filename, pagesize=letter)
                y = 750
                for row in data:
                    pdf.drawString(100, y, f"{row[0]}: {row[1]}")
                    y -= 20
                    if y <= 50:
                        pdf.showPage()
                        pdf.drawString(100, 750, f"{row[0]}: {row[1]}")
                        y = 750
                pdf.save()
                messagebox.showinfo("Export to PDF", "PDF exported successfully.")
    except FileNotFoundError:
        messagebox.showerror("Export to PDF", "CSV file not found.")


# GUI
root = tk.Tk()
root.title("Color Extractor")

# Buttons
open_button = tk.Button(root, text="Open Image", command=open_image)
open_button.pack(pady=10)

export_button = tk.Button(root, text="Export to PDF", command=export_to_pdf)
export_button.pack(pady=10)

# Listbox to display colors
colors_listbox = tk.Listbox(root, width=40, height=20)
colors_listbox.pack(padx=10, pady=10)

root.mainloop()
