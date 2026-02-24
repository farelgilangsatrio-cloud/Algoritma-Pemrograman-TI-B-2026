print("KALKULATOR RATA-RATA UANG JAJAN")
try:
    total_uang = float(input("Masukkan total uang jajan: Rp "))
    jumlah_hari = int(input("Untuk berapa hari uang ini digunakan? "))

    rata_rata = total_uang / jumlah_hari

    print(f"Jatah uang jajan per hari adalah: Rp {rata_rata:,.2f}")

except ValueError:
    print("[Error]: Harap masukkan angka!")

except ZeroDivisionError:
    print("[Error]: Jumlah hari tidak boleh nol!")

finally:
    print("Program selesai")



