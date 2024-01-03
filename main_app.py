import tkinter as tk  # Mengimpor modul tkinter untuk membuat GUI
from tkinter import *  # Mengimpor semua fungsi dari modul tkinter
from tkinter.font import BOLD  # Mengimpor fungsi BOLD dari modul tkinter.font
from tkinter.messagebox import *  # Mengimpor semua fungsi dari modul tkinter.messagebox

class UIandFunction:
    def __init__(self, root, Basecolor):
        self.sv = StringVar()  # Membuat StringVar untuk menyimpan data Entry 1
        self.sv2 = StringVar()  # Membuat StringVar untuk menyimpan data Entry 2

        # Tampilan frame atas
        self.frameTop(root, Basecolor)

        # Tampilan frame bawah
        self.frameBottom(root, Basecolor)

        # Event untuk Entry waktu keluar
        self.sv.trace("w", lambda name, index, mode, sv=self.sv: self.callback(sv, 1))

        # Event untuk Entry waktu masuk
        self.sv2.trace("w", lambda name, index, mode, sv2=self.sv2: self.callback(sv2, 2))

        # Event untuk tombol simpan data
        self.btn_save.bind("<Button>", lambda e: self.insertData(self.frametable, self.data_list))

        # Event untuk tombol cari data
        self.btn_search.bind("<Button>", lambda e: self.searchTwoD(str(self.s_no_plat.get()), self.data_list))

    # Fungsi untuk frame atas
    def frameTop(self, root, Basecolor):
        frametop = Frame(root, bg=Basecolor)  # Membuat frame atas dengan warna latar Basecolor
        frameleft = Frame(frametop, bg=Basecolor)  # Membuat frame kiri dalam frame atas
        lb_title = Label(frameleft, text="APLIKASI TIKET PARKIR", bg=Basecolor, fg="white")  # Label judul aplikasi
        lb_title.config(font=("Helvetica", 10, BOLD))  # Konfigurasi font label
        lb_title.pack()  # Menampilkan label judul aplikasi
        # Label dan tombol untuk mencari nomor plat
        Label(frameleft, text="Cari NoPol", bg=Basecolor, fg="white").place(x=30, y=40)
        self.s_no_plat = s_no_plat = Entry(frameleft)
        s_no_plat.place(x=115, y=40)
        self.btn_search = btn_search = Button(frameleft, text="Cari", activebackground="green", activeforeground="blue", bg="white", fg="black")
        btn_search.place(x=280, y=40)
        # Label dan entry untuk nomor plat, waktu masuk, waktu keluar, dan biaya
        Label(frameleft, text="No Plat Polisi", bg=Basecolor, fg="white").place(x=30, y=90)
        Label(frameleft, text="Waktu Masuk", bg=Basecolor, fg="white").place(x=30, y=130)
        Label(frameleft, text="Waktu Keluar", bg=Basecolor, fg="white").place(x=30, y=170)
        Label(frameleft, text="Biaya", bg=Basecolor, fg="white").place(x=30, y=210)
        self.btn_save = btn_save = Button(frameleft, text="Simpan", activebackground="green", activeforeground="blue", bg="white", fg="black")
        btn_save.place(x=280, y=208)
        self.i_no_plat = i_no_plat = Entry(frameleft)  # Entry untuk nomor plat
        i_no_plat.place(x=125, y=90)
        self.i_wm = i_wm = Entry(frameleft, textvariable=self.sv2)  # Entry untuk waktu masuk
        i_wm.insert(END, '00:00')
        i_wm.place(x=125, y=130)
        self.i_ws = i_ws = Entry(frameleft, textvariable=self.sv)  # Entry untuk waktu keluar
        i_ws.insert(END, '01:00')
        i_ws.place(x=125, y=170)
        self.i_biaya = i_biaya = Entry(frameleft)  # Entry untuk biaya
        i_biaya.insert(END, '2000')
        i_biaya.place(x=125, y=210)
        # Label untuk tabel list pelanggan urut terakhir keluar
        lb_table1 = Label(frameleft, text="List Pelanggan Urut Terakhir Keluar", bg=Basecolor, fg="white")
        lb_table1.config(font=("Helvetica", 12, BOLD))
        lb_table1.place(x=30, y=255)
        frameleft.pack(fill='both', side='left', expand='True')  # Mengatur tata letak frame kiri
        frameright = Frame(frametop, bg=Basecolor)  # Membuat frame kanan dalam frame atas
        # Label biaya parkir per jam
        Label(frameright, text="Pembatas Tak Terlihat", bg=Basecolor, fg=Basecolor).pack()
        lb_title_bayar = Label(frameright, text="Biaya Parkir Per Jam", fg="red", bg=Basecolor)
        lb_title_bayar.config(font=("Helvetica", 12, BOLD))
        lb_title_bayar.place(x=0, y=70)
        lb_bayar = Label(frameright, text="Rp 2.000", fg="red", bg=Basecolor)
        lb_bayar.config(font=("Helvetica", 42, BOLD))
        lb_bayar.place(x=0, y=90)
        # Label untuk tabel list pelanggan banyak bayar
        lb_table2 = Label(frameright, text="List Pelanggan Banyak Bayar", bg=Basecolor, fg="white")
        lb_table2.config(font=("Helvetica", 12, BOLD))
        lb_table2.place(x=0, y=255)
        frameright.pack(fill='both', side='right', expand='True')  # Mengatur tata letak frame kanan
        frametop.pack(fill='both', side='top', expand='True')  # Mengatur tata letak frame atas

    # Fungsi untuk frame bawah
    def frameBottom(self, root, Basecolor):
        data_list = []  # List untuk menyimpan data pelanggan parkir
        framebottom = Frame(root, bg=Basecolor)  # Membuat frame bawah dengan warna latar Basecolor
        lbframe_left = LabelFrame(framebottom, bd=8, bg=Basecolor)  # Membuat label frame kiri dalam frame bawah
        self.tableGrid(1, lbframe_left, data_list)  # Menampilkan tabel list pelanggan urut terakhir keluar
        lbframe_left.pack(side='left')  # Mengatur tata letak label frame kiri
        lbframe_right = LabelFrame(framebottom, bd=8, bg=Basecolor)  # Membuat label frame kanan dalam frame bawah
        self.tableGrid(2, lbframe_right, data_list)  # Menampilkan tabel list pelanggan banyak bayar
        lbframe_right.pack(side='right')  # Mengatur tata letak label frame kanan
        framebottom.pack(fill='both', side='bottom')  # Mengatur tata letak frame bawah
        self.frametable = [lbframe_left, lbframe_right]  # Menyimpan label frame kiri dan kanan
        self.data_list = data_list  # Menyimpan data list pelanggan parkir

    # Fungsi untuk tabel grid
    def tableGrid(self, indikator, frame, data_list):
        # Fungsi menggunakan indikator untuk menentukan jenis pengurutan apa yang akan dilakukan pada data. Jika indikator sama dengan 1, data akan diurutkan berdasarkan waktu masuk. Jika tidak, data akan diurutkan berdasarkan waktu keluar.
        if indikator == 1:
            data_list_update = self.Sort(data_list, 2)  # Mengurutkan data berdasarkan waktu masuk
        else:
            data_list_update = self.Sort(data_list, 3)  # Mengurutkan data berdasarkan waktu keluar
        title = [['No Plat Polisi', 'Masuk', 'Keluar', 'Biaya']]
        data_list_update = title + data_list_update
        # Melakukan iterasi untuk membuat entri untuk setiap sel di tabel berdasarkan ukuran dari data_list_update.
        for i in range(len(data_list_update)):
            for j in range(len(data_list_update[0])):
                e = Entry(frame, width=12, fg='blue', font=('Arial', 10))
                e.grid(row=i, column=j)
                #  Memasukkan data dari data_list_update ke dalam setiap widget Entry untuk menampilkan isi tabel.
                e.insert(END, data_list_update[i][j])

    # Fungsi untuk mengurutkan data
    def Sort(self, sub_li, index):
        return sorted(sub_li, key=lambda x: x[index], reverse=True)  # Mengurutkan data secara descending

    # Fungsi untuk memasukkan data baru
    def insertData(self, frametable, data_list):
        if str(self.i_no_plat.get()) != '':
            if len(data_list) < 1:
                data_list.append(
                    [str(self.i_no_plat.get()), str(self.i_wm.get()), str(self.i_ws.get()), int(self.i_biaya.get())])
                showinfo(title='Insert Success', message='Data berhasil dimasukkan.')
            else:
                no_data_same = True
                for i in range(len(data_list)):
                    if data_list[i][0] == str(self.i_no_plat.get()):
                        no_data_same = False
                        break
                if no_data_same:
                    data_list.append(
                        [str(self.i_no_plat.get()), str(self.i_wm.get()), str(self.i_ws.get()),
                         int(self.i_biaya.get())])
                    showinfo(title='Insert Success', message='Data berhasil dimasukkan.')
                else:
                    showerror(title='Insert gagal', message='No Plat Polisi tersebut sudah terdapat di dalam data list')
        else:
            showerror(title='Insert gagal', message='No Plat Polisi tersebut tidak boleh kosong')
        for i in range(len(frametable)):
            self.tableGrid(i + 1, frametable[i], data_list)

    # Fungsi callback dari entry
    def callback(self, sv, indicator):
        data = str(sv.get())
        if len(data) == 5:
            if indicator == 1:
                jam = int(data[:2]) - int(str(self.i_wm.get())[:2])
            else:
                jam = int(str(self.i_ws.get())[:2]) - int(data[:2])
            biaya = jam * 2000
            self.i_biaya.delete(0, END)
            self.i_biaya.insert(0, str(biaya))

    # Fungsi pencarian
    def searchTwoD(self, string, list, message=''):
        for i in range(len(list)):
            if list[i][0] == string:
                message = ' Plat NoPol: ' + list[i][0] + ' \n Masuk: ' + list[i][1] + ' \n Keluar: ' + list[i][
                    2] + ' \n Biaya: ' + str(list[i][3])
                self.i_no_plat.delete(0, END)
                self.i_no_plat.insert(END, list[i][0])
                self.i_wm.delete(0, END)
                self.i_wm.insert(END, list[i][1])
                self.i_ws.delete(0, END)
                self.i_ws.insert(END, list[i][2])
                self.i_biaya.delete(0, END)
                self.i_biaya.insert(END, list[i][3])
                break
        if message != '':
            showinfo(title="Data Ditemukan", message=message)
        else:
            message = 'Data yang anda cari tidak ada!'
            showerror(title='Not Found', message=message)
