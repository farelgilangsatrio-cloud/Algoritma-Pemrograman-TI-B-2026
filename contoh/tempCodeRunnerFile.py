def tampilkan_tabel(data):
    """Menampilkan data dalam bentuk tabel"""
    if not data:
        print("Data kosong!")
        return

    print("Nama\tSkor")
    print("-" * 20)
    
    for baris in data:
        print(f"{baris[0]}\t{baris[1]}")
