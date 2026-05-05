# =========================================
# BAGIAN A — FUNGSI DAN LOGIKA PROGRAM
# =========================================

def hitung_skor(tebakan, target):
    """Menghitung skor berdasarkan kedekatan tebakan dengan target"""
    if tebakan == target:
        return 100
    elif abs(tebakan - target) <= 5:
        return 50
    else:
        return 0


def mainkan_game():
    """Menjalankan satu sesi permainan dan mengembalikan hasil list"""
    hasil = []
    target = 50  # angka tetap (tidak pakai random)

    while True:
        user_input = input("Masukkan angka (atau ketik 'stop'): ")

        if user_input.lower() == "stop":
            break

        tebakan = int(user_input)
        skor = hitung_skor(tebakan, target)

        hasil.append([tebakan, skor])

        print("Skor:", skor)

    return hasil


# =========================================
# BAGIAN B — LIST & MATRIX 2D
# =========================================

def tampilkan_riwayat(data):
    """Menampilkan data riwayat dalam bentuk tabel"""
    if len(data) == 0:
        print("Belum ada data.")
        return

    print("\n=== RIWAYAT PERMAINAN ===")
    print("No | Tebakan | Skor")
    print("----------------------")

    for i in range(len(data)):
        print(i+1, "|", data[i][0], "|", data[i][1])


# =========================================
# BAGIAN C — SELECTION SORT MANUAL
# =========================================

def selection_sort_desc(data):
    """Mengurutkan data berdasarkan skor (descending) tanpa mengubah data asli"""
    hasil = data.copy()

    n = len(hasil)
    for i in range(n):
        max_idx = i
        for j in range(i+1, n):
            if hasil[j][1] > hasil[max_idx][1]:
                max_idx = j

        # tukar
        hasil[i], hasil[max_idx] = hasil[max_idx], hasil[i]

    return hasil


def tampilkan_leaderboard(data):
    """Menampilkan leaderboard dari data yang sudah diurutkan"""
    if len(data) == 0:
        print("Tidak ada leaderboard.")
        return

    print("\n=== LEADERBOARD ===")
    print("Rank | Tebakan | Skor")
    print("-----------------------")

    for i in range(len(data)):
        print(i+1, "|", data[i][0], "|", data[i][1])


# =========================================
# PROGRAM UTAMA
# =========================================

def main():
    """Fungsi utama program"""
    semua_data = []

    while True:
        print("\n=== MENU ===")
        print("1. Main Game")
        print("2. Lihat Riwayat")
        print("3. Lihat Leaderboard")
        print("4. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            hasil_game = mainkan_game()
            semua_data.extend(hasil_game)

        elif pilihan == "2":
            tampilkan_riwayat(semua_data)

        elif pilihan == "3":
            data_urut = selection_sort_desc(semua_data)
            tampilkan_leaderboard(data_urut)

        elif pilihan == "4":
            print("Terima kasih!")
            break

        else:
            print("Pilihan tidak valid.")


# Jalankan program
main()



# ==================== BAGIAN A ====================

def cek_tebakan(tebakan, jawaban):
    if tebakan > jawaban:
        return "Terlalu besar"
    elif tebakan < jawaban:
        return "Terlalu kecil"
    else:
        return "Benar"


def main_game():
    """Menjalankan permainan"""
    jawaban = int(input("Masukkan angka rahasia: "))
    hasil = []

    for i in range(3):  # 3 kali percobaan
        tebakan = int(input("Tebakan kamu: "))
        hasil_tebakan = cek_tebakan(tebakan, jawaban)
        print(hasil_tebakan)
        hasil.append(hasil_tebakan)

    return hasil

# ==================== BAGIAN B ====================

def tampilkan_tabel(data):
    """Menampilkan data dalam bentuk tabel"""
    if not data:
        print("Data kosong!")
        return

    print("Nama\tSkor")
    print("-" * 20)
    
    for baris in data:
        print(f"{baris[0]}\t{baris[1]}")

# data = [
#     ["Farel", 80],
#     ["Budi", 90],
#     ["Siti", 75]
# ]

# tampilkan_tabel(data)

# ==================== BAGIAN C ====================

def selection_sort(data):
    """Mengurutkan data (descending) dengan selection sort"""
    n = len(data)

    for i in range(n):
        max_idx = i
        for j in range(i+1, n):
            if data[j][1] > data[max_idx][1]:
                max_idx = j

        # tukar posisi
        data[i], data[max_idx] = data[max_idx], data[i]

    return data

def tampilkan_leaderboard(data):
    """Menampilkan leaderboard"""
    print("\n=== LEADERBOARD ===")
    for i, item in enumerate(data):
        print(f"{i+1}. {item[0]} - {item[1]}")


# ==================== PROGRAM UTAMA ====================

def main():
    """Program utama"""
    data_pemain = []

    while True:
        nama = input("Masukkan nama pemain: ")
        skor = int(input("Masukkan skor: "))

        data_pemain.append([nama, skor])

        lanjut = input("Tambah data lagi? (y/n): ")
        if lanjut.lower() != 'y':
            break

    tampilkan_tabel(data_pemain)

    sorted_data = selection_sort(data_pemain)

    tampilkan_leaderboard(sorted_data)


main()
