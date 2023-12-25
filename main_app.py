# Import modul tkinter untuk membuat aplikasi GUI
import tkinter as tk
# Import modul datetime dari library datetime untuk mengatur tanggal dan waktu
from datetime import datetime

# Fungsi untuk menghasilkan tiket parkir
def generate_ticket():
    # Mengambil tahun, bulan, hari, dan waktu saat ini
    tahun = datetime.now().year
    bulan = datetime.now().month
    hari = datetime.now().day
    waktu = datetime.now().strftime("%H:%M:%p")
    
    # Mengambil jumlah kendaraan motor dari input pengguna
    jumlah_motor = int(entry_motor.get())
    # Jika jumlah kendaraan motor lebih dari atau sama dengan 3, atur pesan kesalahan
    if jumlah_motor >= 3:
        result_text.set("Jumlah maksimal untuk satu tiket 2 kendaraan motor")
        return
    
    # Mengatur harga tiket motor berdasarkan jumlah motor  yang dimasukkan
    harga_tiket_motor = 15000 if jumlah_motor == 1 else 14000
    # Menghitung total harga parkir motor
    total_parkir_motor = harga_tiket_motor * jumlah_motor
    
    # Mengumpulkan nomor plat dan merk motor dari input pengguna
    plat_motor = [entry_plat_motor[i].get() for i in range(jumlah_motor)]
    merk_motor = [entry_merk_motor[i].get() for i in range(jumlah_motor)]
    
    # Variabel untuk menyimpan informasi tiket
    ticket_info = ""
    total_harga = 0  # Inisialisasi variabel total_harga
    
    # Menambahkan informasi ke tiket untuk setiap motor yang dimasukkan
    for i in range(jumlah_motor):
        ticket_info += "----------------------------------------------\n"
        ticket_info += f"Tiket Motor Masuk \n"
        ticket_info += "----------------------------------------------\n"
        ticket_info += f"{hari}/{bulan}/{tahun}\n"
        ticket_info += f"{waktu}\n"
        ticket_info += f"Nomor Kendaraan: {plat_motor[i]}\n"
        ticket_info += f"Merk Motor: {merk_motor[i]}\n"
        ticket_info += "----------------------------------------------\n"
        ticket_info += f"Harga: Rp {harga_tiket_motor}\n"
        ticket_info += f"Terimakasih\n"
        ticket_info += "----------------------------------------------\n"
        total_harga += harga_tiket_motor  # Menambahkan harga_tiket_motor ke total_harga
    
    ticket_info += f"Total Harga: Rp {total_harga}\n"  # Menambahkan total_harga ke ticket_info
    
    # Menetapkan informasi tiket ke label untuk ditampilkan kepada pengguna
    result_text.set(ticket_info)
    add_info.config(state="normal")
    entry_motor.config(state="normal")

# Fungsi untuk menambahkan kolom input nomor plat dan merk motor
def add_info_fields():
    try:
        jumlah_motor = int(entry_motor.get())
        if jumlah_motor >= 1 and jumlah_motor <= 2:
            global entry_plat_motor, entry_merk_motor
            entry_plat_motor = []
            entry_merk_motor = []
            for i in range(jumlah_motor):
                label_plat = tk.Label(frame, text=f"Plat nomor motor {i + 1}:")
                label_plat.pack()
                entry_plat_motor.append(tk.Entry(frame))
                entry_plat_motor[i].pack()

                label_merk = tk.Label(frame, text=f"Merk motor {i + 1}:")
                label_merk.pack()
                entry_merk_motor.append(tk.Entry(frame))
                entry_merk_motor[i].pack()

            generate_ticket_btn = tk.Button(frame, text="Buat Tiket", command=generate_ticket)
            generate_ticket_btn.pack()
            add_info.config(state="disabled")
            entry_motor.config(state="disabled")

        else:
            result_text.set("Jumlah maksimal untuk satu tiket adalah 2 kendaraan motor")
    except ValueError:
        result_text.set("Masukkan angka yang valid untuk jumlah motor")

# Membuat window utama untuk aplikasi
root = tk.Tk()
root.title("Tiket Motor ")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

label_motor = tk.Label(frame, text="Masukkan jumlah kendaraan Motor:")
label_motor.pack()

entry_motor = tk.Entry(frame)
entry_motor.pack()

add_info = tk.Button(frame, text="Masukkan Informasi", command=add_info_fields)
add_info.pack()

result_text = tk.StringVar()
result_label = tk.Label(frame, textvariable=result_text, justify="left")
result_label.pack()

root.mainloop()



