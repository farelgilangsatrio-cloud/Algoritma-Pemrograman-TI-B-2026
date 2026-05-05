struktur = {
    "Skripsi_Aqil": {
        "Bab_1": {
            "pendahuluan.docx": 45,
            "latar_belakang.docx": 62
        },
        "Bab_2": {
            "referensi": {
                "paper_A.pdf": 340,
                "paper_B.pdf": 210
            }
        },
        "Bab_3": {
            "metodologi.docx": 89,
            "diagram": {
                "flowchart.png": 512,
                "erd.png": 278,
                "arsitektur": {
                    "sistem.png": 430
                }
            }
        },
        "sidang": {
            "presentasi.pptx": 2048,
            "catatan_revisi.txt": 15
        },
        "README.txt": 8
    }
}

# soal A
def total_ukuran(folder):
    total = 0
    for item in folder.values():
        if isinstance(item, dict):
            total += total_ukuran(item)
        else:
            total += item
    return total

print("Total ukuran skripsi:", total_ukuran(struktur), "KB")

# soal B
def hitung_file(folder):
    jumlah = 0
    for item in folder.values():
        if isinstance(item, dict):
            jumlah += hitung_file(item)
        else:
            jumlah += 1 
    return jumlah

print("Jumlah file:", hitung_file(struktur), "file")

# soal C
def cari_terbesar(folder):
    nama_terbesar = ""
    ukuran_terbesar = 0

    for nama, item in folder.items():
        if isinstance(item, dict):
            nama_sub, ukuran_sub = cari_terbesar(item)
            if ukuran_sub > ukuran_terbesar:
                nama_terbesar = nama_sub
                ukuran_terbesar = ukuran_sub
        else:
            if item > ukuran_terbesar:
                nama_terbesar = nama
                ukuran_terbesar = item

    return nama_terbesar, ukuran_terbesar


nama, ukuran = cari_terbesar(struktur)
print(f"File terbesar: {nama} ({ukuran} KB)")

# soal D
def tampilkan_tree(folder, nama="root", level=0):
    indent = " " * (level * 2)

    print(f"{indent}📁 {nama}")

    for key, item in folder.items():
        if isinstance(item, dict):
            tampilkan_tree(item, key, level + 1)
        else:
            print(f"{indent}  📄 {key} ({item} KB)")


tampilkan_tree(struktur)