# Pengulangan atau loop di python ada beberapa jenis, yaitu:
# 1. For
# 2. While

# For
# For digunakan untuk mengulangi kode secara berulang.
# For biasanya digunakan untuk mengulangi kode dengan jumlah yang sudah diketahui.
# For ada dua jenis, yaitu:
# 1. For in range
# 2. For in list

# For in range
# For in range digunakan untuk mengulangi kode dengan jumlah yang sudah diketahui.
# For in range biasanya digunakan untuk mengulangi kode dengan jumlah tertentu.
# Contoh:

for i in range(10):
    print(i) # ini akan menampilkan angka dari 0 sampai 9

# For in list
# For in list digunakan untuk mengulangi kode dengan jumlah yang sudah diketahui.
# For in list biasanya digunakan untuk mengulangi kode dengan jumlah tertentu.
# Contoh:

a = ["nanas", "apel", "jeruk", "mangga", "anggur"]
for i in a:
    print(i) # ini akan menampilkan nama buah yang ada di dalam list a

# While
# While digunakan untuk mengulangi kode secara berulang.
# While biasanya digunakan untuk mengulangi kode dengan jumlah yang belum diketahui.
# Contoh:

i = 0
while i < 10:
    print(i) # ini akan menampilkan angka dari 0 sampai 9
    i += 1

# Ada juga yang namanya break dan continue.
# Break digunakan untuk menghentikan perulangan.
# Continue digunakan untuk melanjutkan perulangan ke langkah berikutnya.
# Contoh:

i = 0
while i < 10:
    if i == 5:
        break
    print(i) # ini akan menampilkan angka dari 0 sampai 4
    i += 1

i = 0
while i < 10:
    i += 1
    if i == 5:
        continue
    print(i) # ini akan menampilkan angka dari 1 sampai 10, kecuali angka 5