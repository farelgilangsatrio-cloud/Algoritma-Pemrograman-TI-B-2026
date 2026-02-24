from myOOP import ProdukElektronik, ProdukMakanan, Email, SMS, Mahasiswa

#Inheritance
prod1 = ProdukElektronik("TV", 3000000, 2)
prod2 = ProdukMakanan("Roti", 15000, "12-12-2026")
print(prod1.info_produk())
print(prod2.info_produk())

#Polymorphism
notif_email = Email()
notif_sms = SMS()
print(notif_email.kirim())
print(notif_sms.kirim())

#Encapsulation
mhs = Mahasiswa()
mhs.set_nilai(85)
print(f"Nilai Mahasiswa: {mhs.get_nilai()}")
pesan_error = mhs.set_nilai(150)
if pesan_error:
    print(pesan_error)