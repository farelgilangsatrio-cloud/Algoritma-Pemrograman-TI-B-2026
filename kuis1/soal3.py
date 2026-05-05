total_bayar = 350000

while True:
    uang_masuk = int(input(f"total uang yang harus di bayar Rp{total_bayar}"))

    if uang_masuk >= total_bayar:
        break
    else:
        print('uang tidak cukup')

kembalian = uang_masuk - total_bayar

print("total bayar: Rp", total_bayar)
print("uang masuk: Rp", uang_masuk)

if kembalian == 0:
    print('uang pas')
else:
    print('kembalian anda adalah', {kembalian})
