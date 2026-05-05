data = [59, 40, 36, 40, 30, 26, 97, 8, 23, 31, 2, 40, 99, 70, 64, 36, 43, 20, 1, 9]

def linearSearch(arr, targetVal):
    for i in range(len(arr)):
        if arr[i] == targetVal:
            return i
    return -1

def binarySearch(arr, targetVal):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == targetVal:
            return mid

        if arr[mid] < targetVal:
            left = mid + 1
        else:
            right = mid - 1

    return -1

print("Data:", data)

nilai = int(input("Masukkan angka yang ingin dicari: "))
result_linear = linearSearch(data, nilai)
print("Hasil Linear Search: ")
if result_linear != -1:
    print("Found at index", result_linear)
else:
    print("Not found (-1)")

urutkan_data = sorted(data)
result_binary = binarySearch(urutkan_data, nilai)

print("Data setelah diurutkan:", urutkan_data)
print("Hasil Binary Search:")
if result_binary != -1:
    print("Found at index", result_binary)
else:
    print("Not found (-1)")