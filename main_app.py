import tkinter as tk
from tkinter import messagebox

class ParkirApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistem Parkir")
        
        self.nomor_plat_label = tk.Label(master, text="Nomor Plat:")
        self.nomor_plat_label.grid(row=0, column=0, padx=10, pady=10)

        self.nomor_plat_entry = tk.Entry(master)
        self.nomor_plat_entry.grid(row=0, column=1, padx=10, pady=10)

        self.jenis_kendaraan_label = tk.Label(master, text="Jenis Kendaraan:")
        self.jenis_kendaraan_label.grid(row=1, column=0, padx=10, pady=10)

        self.jenis_kendaraan_entry = tk.Entry(master)
        self.jenis_kendaraan_entry.grid(row=1, column=1, padx=10, pady=10)

        self.result_label = tk.Label(master, text="")
        self.result_label.grid(row=3, column=0, columnspan=2, pady=10)

        self.parkir_button = tk.Button(master, text="Parkir Kendaraan", command=self.parkirkan_kendaraan)
        self.parkir_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.daftar_button = tk.Button(master, text="Tampilkan Daftar Parkir", command=self.tampilkan_daftar_parkir)
        self.daftar_button.grid(row=4, column=0, columnspan=2, pady=10)

    def parkirkan_kendaraan(self):
        nomor_plat = self.nomor_plat_entry.get()
        jenis_kendaraan = self.jenis_kendaraan_entry.get()

        if nomor_plat and jenis_kendaraan:
            self.result_label.config(text=f"Kendaraan dengan nomor plat {nomor_plat} ({jenis_kendaraan}) berhasil diparkir.")
            self.reset_entry_fields()
        else:
            messagebox.showwarning("Peringatan", "Nomor Plat dan Jenis Kendaraan harus diisi.")

    def tampilkan_daftar_parkir(self):
        daftar_parkir = get_daftar_parkir()
        if not daftar_parkir:
            messagebox.showinfo("Info", "Daftar parkir kosong.")
        else:
            daftar_parkir_str = "\n".join([f"{idx}. Nomor Plat: {kendaraan['Nomor Plat']}, Jenis Kendaraan: {kendaraan['Jenis Kendaraan']}" for idx, kendaraan in enumerate(daftar_parkir, start=1)])
            messagebox.showinfo("Daftar Parkir", daftar_parkir_str)

    def reset_entry_fields(self):
        self.nomor_plat_entry.delete(0, tk.END)
        self.jenis_kendaraan_entry.delete(0, tk.END)

def parkirkan_kendaraan(nomor_plat, jenis_kendaraan):
    # Implementasi fungsi parkirkan_kendaraan sesuai kebutuhan Anda
    # Anda dapat menyimpan data parkir di database atau struktur data lainnya
    pass

def get_daftar_parkir():
    # Implementasi fungsi get_daftar_parkir sesuai kebutuhan Anda
    # Anda dapat mengambil data parkir dari database atau struktur data lainnya
    return []

if __name__ == "__main__":
    root = tk.Tk()
    app = ParkirApp(root)
    root.mainloop()
