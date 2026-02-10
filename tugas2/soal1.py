# soal 1
def rata_rata(nilai):
    if len(nilai) == 0:
        return "Data kosong"
    total = sum(nilai)
    jumlah_data = len(nilai)
    hasil = total / jumlah_data
    return hasil

data_mahasiswa = [80, 75, 90, 60, 85]
print("Hasil Rata-rata:", rata_rata(data_mahasiswa))