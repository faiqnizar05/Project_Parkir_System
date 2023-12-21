import tkinter as tk
from datetime import datetime

def get_entry_time():
    now = datetime.now()
    entry_time = now.strftime("%H:%M:%S")
    return entry_time

def generate_ticket():
    plate_number = plate_entry.get()
    entry_time = get_entry_time()
    jenis_kendaraan = jenis_entry.get()

    # Display plate number and entry time
    ticket_info = f"Nomor Plat: {plate_number}\nJenis Kendaraan: {jenis_kendaraan}\nWaktu Masuk: {entry_time}"
    ticket_display.config(state=tk.NORMAL)
    ticket_display.delete("1.0", tk.END)
    ticket_display.insert(tk.END, ticket_info)
    ticket_display.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Aplikasi Tiket Parkir")

plate_label = tk.Label(root, text="Masukkan Nomor Plat:")
plate_label.pack()

plate_entry = tk.Entry(root)
plate_entry.pack()

jenis_label = tk.Label(root, text="Masukkan Jenis Kendaraan:")
jenis_label.pack()

jenis_entry = tk.Entry(root)  # Fixing variable name
jenis_entry.pack()

generate_button = tk.Button(root, text="Buat Tiket", command=generate_ticket)
generate_button.pack()

ticket_display = tk.Text(root, height=6, width=30)
ticket_display.config(state=tk.DISABLED)
ticket_display.pack()

root.geometry("400x300")
root.mainloop()
