import tkinter as tk

root = tk.Tk()
root.title("Matrix with Dots")

rows, cols = 4, 4  # taille de la matrice
entries = []

for i in range(rows):
    row_entries = []
    for j in range(cols):
        e.grid(row=i, column=j, padx=8, pady=4)
        e.insert(0, ".")  # <<< هنا نحط النقطة داخل الخلية
        row_entries.append(e)
    entries.append(row_entries)

root.mainloop()
