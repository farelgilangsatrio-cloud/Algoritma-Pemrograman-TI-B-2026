# soal 
def bilangan_prima(n):
    hasil_prima = []
    for angka in range(2, n + 1): 
        adalah_prima = True
        for pembagi in range(2, angka):
            if angka % pembagi == 0:
                adalah_prima = False
                break
        if adalah_prima:
            hasil_prima.append(angka)        
    return hasil_prima
print("Daftar Prima sampai 50:", bilangan_prima(50))