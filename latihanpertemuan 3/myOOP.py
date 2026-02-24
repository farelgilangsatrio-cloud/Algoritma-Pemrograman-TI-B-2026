#INHERITANCE
class Produk:
    def __init__(self, nama_produk, harga):
        self.nama_produk = nama_produk
        self.harga = harga

    def info_produk(self):
        return f"{self.nama_produk} seharga {self.harga:,}"

class ProdukElektronik(Produk):
    def __init__(self, nama_produk, harga, garansi):
        super().__init__(nama_produk, harga)
        self.garansi = garansi

    def info_produk(self):
        return f"{super().info_produk()} dengan garansi {self.garansi} tahun"

class ProdukMakanan(Produk):
    def __init__(self, nama_produk, harga, tanggal_kadaluarsa):
        super().__init__(nama_produk, harga)
        self.tanggal_kadaluarsa = tanggal_kadaluarsa

    def info_produk(self):
        return f"{super().info_produk()} kadaluarsa {self.tanggal_kadaluarsa}"


#POLYMORPHISM
class Notifikasi:
    def kirim(self):
        return "Mengirim pesan umum"

class Email(Notifikasi):
    def kirim(self):
        return "Mengirim notifikasi melalui Email"

class SMS(Notifikasi):
    def kirim(self):
        return "Mengirim notifikasi melalui SMS"


#ENCAPSULATION
class Mahasiswa:
    def __init__(self):
        self.__nilai = 0

    def set_nilai(self, nilai):
        if 0 <= nilai <= 100:
            self.__nilai = nilai
        else:
            return "Nilai tidak valid"

    def get_nilai(self):
        return self.__nilai
