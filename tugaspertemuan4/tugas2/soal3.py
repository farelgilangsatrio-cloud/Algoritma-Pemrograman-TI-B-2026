# soal 3
def jumlah_digit(n):
    if n == 0: 
        return 0
    else:
        angka_terakhir = n % 10
        sisa_angka = n // 10
        return angka_terakhir + jumlah_digit(sisa_angka)
    
print("Hasil jumlah digit 1234:", jumlah_digit(1234))