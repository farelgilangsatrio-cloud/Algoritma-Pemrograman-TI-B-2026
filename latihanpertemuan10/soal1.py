'''
Buatlah sebuah program Python yang berjalan di terminal dengan ketentuan sebagai berikut:

Program meminta pengguna untuk memasukkan jumlah elemen yang akan dimasukkan ke dalam array.
Selanjutnya, pengguna memasukkan sejumlah bilangan bulat non-negatif sesuai jumlah yang telah ditentukan, satu per satu.
Setelah semua elemen dimasukkan, program akan mengurutkan array tersebut menggunakan dua algoritma pengurutan, yaitu Radix Sort dan Merge Sort, secara terpisah.
Program menampilkan hasil pengurutan dari masing-masing algoritma ke layar terminal.
Input yang diterima hanya bilangan bulat non-negatif (≥ 0). Program harus menangani input yang tidak valid.
Implementasikan fungsi terpisah untuk Radix Sort dan Merge Sort.
Tampilkan array sebelum dan sesudah diurutkan untuk setiap algoritma.
'''

# Radix Sort
def radixSort(arr):
    radixArray = [[], [], [], [], [], [], [], [], [], []]
    maxVal = max(arr)
    exp = 1
    data = arr.copy()

    while maxVal // exp > 0:

        while len(data) > 0:
            val = data.pop()
            radixIndex = (val // exp) % 10
            radixArray[radixIndex].append(val)

        for bucket in radixArray:
         while len(bucket) > 0:
            val = bucket.pop()
            data.append(val)

        exp *= 10

    return data

# merge short
def mergeSort(arr):
  if len(arr) <= 1:
    return arr

  mid = len(arr) // 2
  leftHalf = arr[:mid]
  rightHalf = arr[mid:]

  sortedLeft = mergeSort(leftHalf)
  sortedRight = mergeSort(rightHalf)

  return merge(sortedLeft, sortedRight)

def merge(left, right):
  result = []
  i = j = 0

  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1

  result.extend(left[i:])
  result.extend(right[j:])

  return result

# program utama
n = int(input("Masukkan jumlah elemen: "))
data = []
i = 0

while i < n :
    nilai = int(input(f'masukkan elemen ke-{i+1} : '))
    i+=1
    if n < 0:
        print("Jumlah harus lebih dari 0.")
        i-=1
    else :
        data.append(nilai)
print("data sebelum di urutkan :", data)
print("Radix sort")
radix_sort = radixSort(data)
print("data setelah di urutkan :", radix_sort)

print("merge sort")
merge_sort = mergeSort(data)
print("data setelah di urutkan :", merge_sort)