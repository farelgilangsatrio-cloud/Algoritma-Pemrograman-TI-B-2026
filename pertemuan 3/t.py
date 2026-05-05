angka = [3, 8, 10, 15, 22, 7] # Membuat sebuah list bernama angka yang berisi beberapa bilangan

angka_genap = 0  # Variabel untuk menyimpan jumlah angka genap, awalnya bernilai 0

for i in angka: # Melakukan perulangan untuk mengambil setiap nilai yang ada di dalam list angka
    if i % 2 == 0:  # Mengecek apakah angka tersebut habis dibagi 2 (artinya angka genap)
        angka_genap = angka_genap + 1   # Jika genap, maka variabel angka_genap ditambah 1

print(angka_genap)  # Menampilkan jumlah angka genap yang ada di dalam list