from tkinter import Tk
from main_app import *

# Kode utama
if __name__ == "__main__":
    Basecolor = 'black'  # Mengubah warna latar belakang menjadi hitam
    root = Tk()  # Membuat instance Tkinter
    root.geometry("740x600")  # Menentukan ukuran jendela
    root.resizable(False, False)  # Menonaktifkan perubahan ukuran jendela
    root.title('Parking APPS')  # Memberikan judul aplikasi
    UIandFunction(root, Basecolor)  # Membuat instance dari kelas UIandFunction
    root.mainloop()  # Memulai loop utama aplikasi GUI
