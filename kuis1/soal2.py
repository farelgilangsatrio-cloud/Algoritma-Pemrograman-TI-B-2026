judul_film = [["kafir", 50000 ],
              ["evenger", 45000 ],
              ["doraemon", 35000],
              ["ultraman", 30000],
              ["Danur", 55000]]

nomor_film_yang_dipilih = []
total_semua_film = 0

while True:
    total_semua_film = int(input('pilih nomor film: '))

    if nomor_film_yang_dipilih == 0:
        break
    if 1 <= judul_film <= len(daftar_film):
        daftar_film = int(input('masukkan nomor film: '))
        nama_film = judul_film[daftar_film-1]

        nomor_film_yang_dipilih.append([nama_film[0], daftar_film, nama_film[1] * daftar_film])
        total_semua_film += nama_film[1] * daftar_film
    else:
        print("error : nomor film tidak valid")

    for item in nomor_film_yang_dipilih :
        print(f"{item [0]} x {item[1]} = harga {item [2]}")

print(f"total harga : Rp {total_semua_film}")