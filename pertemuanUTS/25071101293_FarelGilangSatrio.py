# === BAGIAN A ===
DAFTAR_ANGKA = [23, 67, 4, 89, 15, 42, 73, 31, 58, 9]
data_final =[]
def tebak_angka(angka_rahasia, maks_percobaan):
        global sisa_percobaan
        x = maks_percobaan
        for i in range(DAFTAR_ANGKA):
            tebakan = int(input("masukkan angka tebakan"))
        if tebakan > angka_rahasia:
            print("Terlalu besar")
        elif tebakan < angka_rahasia:
            print("Terlalu kecil")
        else:
            print("Benar")
            sisa_percobaan = x
            x = 0
        x -= 1
        sisa_percobaan = 0
        return True

def hitung_skor(berhasil, sisa_percobaan):
    if berhasil:
        sisa_percobaan -= 1
        return sisa_percobaan * 10
    else:
        return 0

def main_satu_ronde(nama, nomor_ronde):
    global angka_rahasia
    global data_final
    angka_rahasia = DAFTAR_ANGKA [(nomor_ronde-1) % len(DAFTAR_ANGKA)]
    print(f"ronde ke-{nomor_ronde}")
    berhasil = tebak_angka(angka_rahasia,7)
    data = []
    data.append(nama)
    data.append(hitung_skor(berhasil, sisa_percobaan))
    data_final.append(data)
    data.clear()


# === BAGIAN B ===
def tampilkan_riwayat(riwayat):
    if not riwayat:
        print("belum ada riwayat")
        return
    
    print("nomor | nama | skor")
    print("-" * 10)
    
    for i in riwayat:
        print(f"{data_final[0]}{data_final[1]}")

# === BAGIAN C ===
def selection_sort_riwayat(riwayat):
    n = len(riwayat)
    for i in range(n):
        max_idx = i
        for j in range(i+1, n):
            if riwayat[j][1] > riwayat[max_idx][1]:
                max_idx = j
        riwayat[i], riwayat[max_idx] = riwayat[max_idx], riwayat[i]

    return riwayat

def tampilkan_leaderboard(riwayat):
    print("=== LEADERBOARD ===")
    for i, data_final in(riwayat):
        print(f"{i+1}. {data_final[0]} - {data_final[1]}")