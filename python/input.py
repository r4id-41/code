# Di python kita bisa menginput data dari user, caranya adalah dengan menggunakan command input().
# Contoh:

nama = input("Masukkan nama anda: ") # ini akan meminta user untuk memasukkan nama
print("Nama saya adalah", nama) # ini akan menampilkan Nama saya adalah [nama yang diinput user]

umur = input("Masukkan umur anda: ") # ini akan meminta user untuk memasukkan umur
print("Umur saya adalah", umur) # ini akan menampilkan Umur saya adalah [umur yang diinput user]

alamat = input("Masukkan alamat anda: ") # ini akan meminta user untuk memasukkan alamat
print("Alamat saya adalah", alamat) # ini akan menampilkan Alamat saya adalah [alamat yang diinput user]

# Dengan input() kita bisa meminta user untuk memasukkan data, dan data tersebut akan disimpan
# dalam variable yang kita tentukan.

# Kita juga bisa menggabungkan input() dengan variable, misalnya kita ingin menggabungkan
# nama, umur, dan alamat yang diinput user dalam satu kalimat.
# Contoh:

nama = input("\nMasukkan nama anda: ") # ini akan meminta user untuk memasukkan nama
umur = input("Masukkan umur anda: ") # ini akan meminta user untuk memasukkan umur
alamat = input("Masukkan alamat anda: ") # ini akan meminta user untuk memasukkan alamat
Biodata = "Nama saya " + nama + ", umur saya " + umur + " tahun, dan alamat saya di " + alamat
print(Biodata) 
# ini akan menampilkan Nama saya [nama yang diinput user], umur saya [umur yang diinput user] tahun, 
# dan alamat saya di [alamat yang diinput user]