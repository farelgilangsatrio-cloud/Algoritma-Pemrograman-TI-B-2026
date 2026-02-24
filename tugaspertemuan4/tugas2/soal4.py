# soal 4
def pangkat_rekursif(a, b):
    if b == 0:
        return 1
    else:
        return a * pangkat_rekursif(a, b - 1)
    
print("Hasil 2 pangkat 5:", pangkat_rekursif(2, 5))