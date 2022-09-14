panjang = input("Masukan range data: ")
panjang = int(panjang)
kamus = dict()

for a in range(panjang):
    if a % 2 ==0:
        n = a
        fact = 1
        for b in range(1, n + 1):
            fact = fact * b
        kamus[a] = fact


print(kamus)
tampil = int(input("Data ditampilkan: "))

if tampil in kamus.keys():
    print(kamus[tampil])
else:
    print("Data tidak ditemukan")