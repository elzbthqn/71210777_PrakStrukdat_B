import json

NKar = int(input("Masukan jumlah karyawan baru: "))
for i in range(NKar):
    with open('karyawan.json','r') as file:
        data = json.load(file)

    LKaryawan = list()
    LKolega = list()
    DAlamat = dict()
    DKolega = dict()

    nama = input("Masukan nama: ")
    alamat = input("Masukan alamat: ")

    NKol = int(input("Masukan jumlah kolega: "))
    for j in range(1, NKol+1):
        kolega = input(f"Masukan nama kolega ke-{j}: ")
        LKolega.append(kolega)
        
    DAlamat["Alamat"] = alamat
    DKolega["Kolega"] = LKolega
    LKaryawan.append(DAlamat)
    LKaryawan.append(DKolega)

    with open('karyawan.json','w') as file:
        data[nama] = LKaryawan
        json.dump(data, file)
        
    print("=== Data berhasil ditambahkan ===")