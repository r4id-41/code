# Di python ada yang namanya kondisi.
# Kondisi digunakan untuk mengeksekusi kode jika kondisi yang kita tentukan terpenuhi.
# Ada beberapa kondisi yang bisa digunakan di python, yaitu:
# 1. if
# 2. elif
# 3. else

# if (jika)
# if digunakan untuk mengeksekusi kode jika kondisi yang kita tentukan terpenuhi.
# Contoh:

a = 10
b = 20
if a < b:
    print("a lebih kecil dari b") # ini akan ditampilkan jika a lebih kecil dari b

# elif (jika tidak)
# elif digunakan untuk mengeksekusi kode jika kondisi yang kita tentukan sebelumnya tidak terpenuhi.
# Contoh:

c = 10
d = 20
if c > d:
    print("c lebih besar dari d") # ini akan ditampilkan jika c lebih besar dari d
elif c < d:
    print("c sama dengan d")

# else (kecuali)
# else digunakan untuk mengeksekusi kode jika semua kondisi yang kita tentukan tidak terpenuhi.
# Contoh:

e = 10
f = 20
if e > f:
    print("e lebih besar dari f") # ini akan ditampilkan jika e lebih besar dari f
elif e == f:
    print("e sama dengan f")
else:
    print("e lebih kecil dari f")
