# di python ada yang namanya fungsi, yaitu blok kode yang digunakan untuk melakukan tugas tertentu.
# Fungsi dapat digunakan kembali di berbagai bagian dari program.
# Fungsi di python didefinisikan menggunakan kata kunci def.
# di bawah ini adalah contoh penggunaan fungsi di python.

# def adalah kata kunci yang digunakan untuk mendefinisikan fungsi
def kalkulator(): # kalkulator adalah nama fungsi
    print("Kalkulator Sederhana")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Keluar")
    pilihan = input("Masukkan pilihan: ")
    if pilihan == '1':
        a = int(input("Masukkan angka pertama: "))
        b = int(input("Masukkan angka kedua: "))
        print("Hasil: ", a+b)
    elif pilihan == '2':
        a = int(input("Masukkan angka pertama: "))
        b = int(input("Masukkan angka kedua: "))
        print("Hasil: ", a-b)
    elif pilihan == '3':
        a = int(input("Masukkan angka pertama: "))
        b = int(input("Masukkan angka kedua: "))
        print("Hasil: ", a*b)
    elif pilihan == '4':
        a = int(input("Masukkan angka pertama: "))
        b = int(input("Masukkan angka kedua: "))
        print("Hasil: ", a/b)
    elif pilihan == '5':
        print("Terima kasih")
    else:
        print("Pilihan tidak valid")
        kalkulator()

# untuk memanggil fungsi kalkulator, kita bisa menggunakan nama fungsi diikuti dengan tanda kurung
print(kalkulator())