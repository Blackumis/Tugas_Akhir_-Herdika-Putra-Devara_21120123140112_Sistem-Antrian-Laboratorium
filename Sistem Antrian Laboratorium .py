import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime


class Pasien:
    def __init__(self, nama, tanggal_lahir, tempat_lahir, tanggal_daftar, jenis_kelamin, nomor_telepon, nomor_ktp, paket, layanan):
        self.nama = nama
        self.tanggal_lahir = tanggal_lahir
        self.tempat_lahir = tempat_lahir
        self.tanggal_daftar = tanggal_daftar
        self.jenis_kelamin = jenis_kelamin
        self.nomor_telepon = nomor_telepon
        self.nomor_ktp = nomor_ktp
        self.paket = paket
        self.layanan = layanan
        self.nomor_antrian = None


class Laboratorium:
    def __init__(self):
        self.antrian_express = []  
        self.antrian_regular = []  
    
    def ambil_nomor_antrian(self, pasien):
        if pasien.paket == "Express":
            pasien.nomor_antrian = len(self.antrian_express) + 1
            self.antrian_express.append(pasien)
            waktu_proses = "hari ini"
        else:
            pasien.nomor_antrian = len(self.antrian_regular) + 1
            self.antrian_regular.append(pasien)
            waktu_proses = "4 hari"
        
        return pasien.nomor_antrian, waktu_proses

    def hapus_antrian(self, nomor_antrian, paket):
        if paket == "Express":
            self.antrian_express = [pasien for pasien in self.antrian_express if pasien.nomor_antrian != nomor_antrian]
            for i, pasien in enumerate(self.antrian_express):
                pasien.nomor_antrian = i + 1
        else:
            self.antrian_regular = [pasien for pasien in self.antrian_regular if pasien.nomor_antrian != nomor_antrian]
            for i, pasien in enumerate(self.antrian_regular):
                pasien.nomor_antrian = i + 1


class LaboratoriumGUI(tk.Tk):
    def __init__(self, laboratorium):
        super().__init__()
        self.laboratorium = laboratorium
        self.title("Sistem Antrian Laboratorium")

       
        self.label_nama = tk.Label(self, text="Nama:")
        self.entry_nama = tk.Entry(self)

        self.label_tanggal_lahir = tk.Label(self, text="Tanggal Lahir (YYYY-MM-DD):")
        self.entry_tanggal_lahir = tk.Entry(self)

        self.label_tempat_lahir = tk.Label(self, text="Tempat Lahir:")
        self.entry_tempat_lahir = tk.Entry(self)

        self.label_tanggal_daftar = tk.Label(self, text="Tanggal Daftar (YYYY-MM-DD):")
        self.entry_tanggal_daftar = tk.Entry(self)

        self.label_jenis_kelamin = tk.Label(self, text="Jenis Kelamin:")
        self.var_jenis_kelamin = tk.StringVar(self)
        self.var_jenis_kelamin.set("Laki-Laki")  
        self.optionmenu_jenis_kelamin = tk.OptionMenu(self, self.var_jenis_kelamin, "Laki-Laki", "Perempuan")

        self.label_nomor_telepon = tk.Label(self, text="Nomor Telepon:")
        self.entry_nomor_telepon = tk.Entry(self)

        self.label_nomor_ktp = tk.Label(self, text="Nomor KTP:")
        self.entry_nomor_ktp = tk.Entry(self)

        self.label_paket = tk.Label(self, text="Paket:")
        self.var_paket = tk.StringVar(self)
        self.var_paket.set("Express")  
        self.optionmenu_paket = tk.OptionMenu(self, self.var_paket, "Express", "Regular")

        self.label_layanan = tk.Label(self, text="Layanan:")
        self.var_layanan = tk.StringVar(self)
        self.var_layanan.set("Ambil Darah")  
        self.optionmenu_layanan = tk.OptionMenu(self, self.var_layanan, "Ambil Darah", "Medical Check-up", "Rontgen", "USG")

        self.button_ambil_nomor_antrian = tk.Button(self, text="Ambil Nomor Antrian", command=self.ambil_nomor_antrian)
        self.button_hapus_antrian = tk.Button(self, text="Hapus Antrian", command=self.hapus_antrian)

        
        self.tree = ttk.Treeview(self, columns=("Nama", "Tanggal Lahir", "Tempat Lahir", "Tanggal Daftar", "Jenis Kelamin", "Nomor Telepon", "Nomor KTP", "Paket", "Layanan", "Nomor Antrian"), show="headings")
        self.tree.heading("Nama", text="Nama")
        self.tree.heading("Tanggal Lahir", text="Tgl Lahir")
        self.tree.heading("Tempat Lahir", text="Tmpt Lahir")
        self.tree.heading("Tanggal Daftar", text="Tgl Daftar")
        self.tree.heading("Jenis Kelamin", text="Jns Kelamin")
        self.tree.heading("Nomor Telepon", text="No Telp")
        self.tree.heading("Nomor KTP", text="No KTP")
        self.tree.heading("Paket", text="Paket")
        self.tree.heading("Layanan", text="Layanan")
        self.tree.heading("Nomor Antrian", text="No Antrian")

        
        self.tree.column("Nama", width=100)
        self.tree.column("Tanggal Lahir", width=80)
        self.tree.column("Tempat Lahir", width=100)
        self.tree.column("Tanggal Daftar", width=80)
        self.tree.column("Jenis Kelamin", width=80)
        self.tree.column("Nomor Telepon", width=80)
        self.tree.column("Nomor KTP", width=100)
        self.tree.column("Paket", width=60)
        self.tree.column("Layanan", width=80)
        self.tree.column("Nomor Antrian", width=80)

        
        self.tree_scroll = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=self.tree_scroll.set)

        
        self.label_nama.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_nama.grid(row=0, column=1, padx=5, pady=5)

        self.label_tanggal_lahir.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_tanggal_lahir.grid(row=1, column=1, padx=5, pady=5)

        self.label_tempat_lahir.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entry_tempat_lahir.grid(row=2, column=1, padx=5, pady=5)

        self.label_tanggal_daftar.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.entry_tanggal_daftar.grid(row=3, column=1, padx=5, pady=5)

        self.label_jenis_kelamin.grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.optionmenu_jenis_kelamin.grid(row=4, column=1, padx=5, pady=5)

        self.label_nomor_telepon.grid(row=5, column=0, padx=5, pady=5, sticky="e")
        self.entry_nomor_telepon.grid(row=5, column=1, padx=5, pady=5)

        self.label_nomor_ktp.grid(row=6, column=0, padx=5, pady=5, sticky="e")
        self.entry_nomor_ktp.grid(row=6, column=1, padx=5, pady=5)

        self.label_paket.grid(row=7, column=0, padx=5, pady=5, sticky="e")
        self.optionmenu_paket.grid(row=7, column=1, padx=5, pady=5)

        self.label_layanan.grid(row=8, column=0, padx=5, pady=5, sticky="e")
        self.optionmenu_layanan.grid(row=8, column=1, padx=5, pady=5)

        self.button_ambil_nomor_antrian.grid(row=9, column=0, columnspan=2, padx=5, pady=5)
        self.button_hapus_antrian.grid(row=10, column=0, columnspan=2, padx=5, pady=5)

        self.tree.grid(row=11, column=0, columnspan=2, padx=5, pady=5)
        self.tree_scroll.grid(row=11, column=2, padx=5, pady=5, sticky="ns")

    def ambil_nomor_antrian(self):
        nama = self.entry_nama.get()
        tanggal_lahir = self.entry_tanggal_lahir.get()
        tempat_lahir = self.entry_tempat_lahir.get()
        tanggal_daftar = self.entry_tanggal_daftar.get()
        jenis_kelamin = self.var_jenis_kelamin.get()
        nomor_telepon = self.entry_nomor_telepon.get()
        nomor_ktp = self.entry_nomor_ktp.get()
        paket = self.var_paket.get()
        layanan = self.var_layanan.get()
        
        if not (nama and tanggal_lahir and tempat_lahir and tanggal_daftar and nomor_telepon and nomor_ktp):
            messagebox.showerror("Error", "Semua field harus diisi!")
            return
        
        try:
            datetime.strptime(tanggal_lahir, "%Y-%m-%d")
            datetime.strptime(tanggal_daftar, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Format tanggal salah. Gunakan format YYYY-MM-DD.")
            return
        
        pasien = Pasien(nama, tanggal_lahir, tempat_lahir, tanggal_daftar, jenis_kelamin, nomor_telepon, nomor_ktp, paket, layanan)
        nomor_antrian, waktu_proses = self.laboratorium.ambil_nomor_antrian(pasien)
        
        self.tree.insert("", "end", values=(pasien.nama, pasien.tanggal_lahir, pasien.tempat_lahir, pasien.tanggal_daftar, pasien.jenis_kelamin, pasien.nomor_telepon, pasien.nomor_ktp, pasien.paket, pasien.layanan, pasien.nomor_antrian))
        
        messagebox.showinfo("Nomor Antrian", f"Nomor Antrian Anda: {nomor_antrian}\n"
                                             f"Paket: {paket}\n"
                                             f"Layanan: {layanan}\n"
                                             f"Waktu Proses: {waktu_proses}")

    def hapus_antrian(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Peringatan", "Pilih pasien yang akan dihapus dari antrian.")
            return
        
        for item in selected_item:
            item_values = self.tree.item(item, "values")
            nomor_antrian = int(item_values[9])
            paket = item_values[7]
            self.laboratorium.hapus_antrian(nomor_antrian, paket)
            self.tree.delete(item)


if __name__ == "__main__":
    laboratorium = Laboratorium()
    app = LaboratoriumGUI(laboratorium)
    app.mainloop()

