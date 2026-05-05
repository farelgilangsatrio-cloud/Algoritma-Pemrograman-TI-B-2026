def transpose(matriks):
    baris = len(matriks)
    kolom = len(matriks[0])
 # Buat matriks hasil berukuran kolom x baris (dimensi terbalik)
    hasil = [[0 for i in range(baris)] for j in range(kolom)]
    for i in range(baris):
        for j in range(kolom):
            hasil[j][i] = matriks[i][j]
    return hasil
A = [[1, 2, 3],
 [4, 5, 6]] # Ukuran 2x3
print('Matriks A (2x3):')
for baris in A:
 print(baris)
T = transpose(A)
print('Transpose A (3x2):')
for baris in T:
 print(baris)

# determinan
def determinan_2x2(matriks):
 a, b = matriks[0][0], matriks[0][1]
 c, d = matriks[1][0], matriks[1][1]
 return (a * d) - (b * c)
# Contoh 1
A = [[3, 8], [4, 6]]
print('det(A):', determinan_2x2(A))
# Perhitungan: (3x6) - (8x4) = 18 - 32 = -14
# Output: det(A): -14
# Contoh 2: matriks singular (det = 0)
C = [[2, 4], [1, 2]]
print('det(C):', determinan_2x2(C))
# Perhitungan: (2x2) - (4x1) = 4 - 4 = 0

def determinan_3x3(M):
 # Diagonal utama: dijumlahkan
 d1 = M[0][0] * M[1][1] * M[2][2]
 d2 = M[0][1] * M[1][2] * M[2][0]
 d3 = M[0][2] * M[1][0] * M[2][1]
 # Diagonal sekunder: dikurangkan
 d4 = M[0][2] * M[1][1] * M[2][0]
 d5 = M[0][0] * M[1][2] * M[2][1]
 d6 = M[0][1] * M[1][0] * M[2][2]
 return (d1 + d2 + d3) - (d4 + d5 + d6)
B = [[1, 2, 3],
 [4, 5, 6],
 [7, 2, 9]]
print('det(B):', determinan_3x3(B))
# Langkah: (45 + 84 + 24) - (105 + 12 + 72) = 153 - 189 = -36
# Output: det(B): -36
# Verifikasi dengan NumPy

# invers
def determinan_2x2(m):
    return m[0][0]*m[1][1] - m[0][1]*m[1][0]
def inverse_2x2(matriks):
    det = determinan_2x2(matriks)
    if det == 0:
     print('Matriks singular: inverse tidak ada (det = 0)')
    return None
    a, b = matriks[0][0], matriks[0][1]
    c, d = matriks[1][0], matriks[1][1]
    return [[ d/det, -b/det],[-c/det, a/det]]
A = [[4, 7],[2, 6]]
inv = inverse_2x2(A)
print('Inverse A:')
for baris in inv:
 print([round(x, 4) for x in baris])

# perkalian
def kali_matriks(A, B):
  baris_A, kolom_A = len(A), len(A[0])
  baris_B, kolom_B = len(B), len(B[0])
  if kolom_A != baris_B:
    print('Error: kolom A harus sama dengan baris B')
    return None
    hasil = [[0]*kolom_B for _ in range(baris_A)]
    for i in range(baris_A):
        for j in range(kolom_B):
            for k in range(kolom_A):
                hasil[i][j] += A[i][k] * B[k][j]
    return hasil
A = [[1, 2], [3, 4], [5, 6]] # Ukuran 3x2
B = [[7, 8, 9], [10, 11, 12]] # Ukuran 2x3
C = kali_matriks(A, B) # Hasil ukuran 3x3
for baris in C:
 print(baris)

#  pembagian
def bagi_matriks_elementwise(A, B):
    baris, kolom = len(A), len(A[0])
    hasil = [[0.0]*kolom for _ in range(baris)]
    for i in range(baris):
        for j in range(kolom):
                if B[i][j] == 0:
                    print(f'Error: pembagi 0 pada posisi [{i}][{j}]')
    return None
    hasil[i][j] = A[i][j] / B[i][j]
    return hasil
A = [[10, 20, 30], [40, 50, 60]]
B = [[2, 4, 5], [8, 10, 12]]
E = bagi_matriks_elementwise(A, B)
for baris in E:
 print(baris)