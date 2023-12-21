# from tkinter import * 
# window =Tk()
# window.mainloop()

import tkinter as tk
from datetime import datetime

# Fungsi untuk mengambil waktu masuk
def get_entry_time():
    now = datetime.now()
    entry_time = now.strftime("%H:%M:%S")
    return entry_time

# Fungsi untuk membuat tiket parkir
def generate_ticket():
    plate_number = plate_entry.get()
    entry_time = get_entry_time()

# plat
    ticket_info = f"Nomor Plat: {plate_number}\nWaktu Masuk: {entry_time}"
    ticket_display.config(state=tk.NORMAL)
    ticket_display.delete("1.0", tk.END)
    ticket_display.insert(tk.END, ticket_info)
    ticket_display.config(state=tk.DISABLED)




# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Tiket Parkir")

# Label dan input nomor plat
plate_label = tk.Label(root, text="Masukkan Nomor Plat:")
plate_label.pack()

plate_entry = tk.Entry(root)
plate_entry.pack()

# Tombol untuk membuat tiket
generate_button = tk.Button(root, text="Buat Tiket", command=generate_ticket)
generate_button.pack()

# Menampilkan tiket parkir
ticket_display = tk.Text(root, height=6, width=30)
ticket_display.config(state=tk.DISABLED)
ticket_display.pack()

# Menjalankan aplikasi
root.mainloop()
