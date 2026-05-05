judul_film = [["kafir", 50000 ],
              ["evenger", 45000 ],
              ["doraemon", 35000],
              ["ultraman", 30000],
              ["Danur", 55000]]

for i in range(len(judul_film)):
    print(f"{i +1}. {judul_film[i][0]} harga film Rp.{judul_film[i][1]}")

daftar_film = int(input('masukkan nomor film: '))
if 1 <= daftar_film <= len(judul_film):
    nama_film = judul_film[daftar_film-1]
    print("film yang di pilih", nama_film [0])
    print("harga film", nama_film[1])
else:
    print("error : nomor film tidak valid")