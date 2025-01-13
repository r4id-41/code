# Di python ada beberapa type data umum yang sering digunakan, yaitu:
# 1. String
# 2. Integer
# 3. Float
# 4. Boolean

# String (str)
# String adalah type data yang berupa teks atau kumpulan karakter. 
# String bisa berupa huruf, angka, simbol, dll.
# String biasanya diapit oleh tanda kutip, baik kutip satu (') maupun kutip dua (").
# Contoh:

a = "halo bro" # ini adalah string
b = "123" # ini adalah string
c = "!" # ini adalah string
d = "123.45" # ini adalah string
print(type(a))
print(type(b))
print(type(c))
print(type(d))

# Integer (int)
# Integer adalah type data yang berupa bilangan bulat. Integer tidak mengandung desimal atau pecahan.
# Contoh:

x = 10 # ini adalah integer
y = 1000 # ini adalah integer
z = -100 # ini adalah integer
print(type(x))
print(type(y))
print(type(z))

# Float (float)
# Float adalah type data yang berupa bilangan pecahan. Float mengandung desimal.
# Contoh:

e = 10.5 # ini adalah float
f = 1000.0 # ini adalah float
g = -100.5 # ini adalah float
print(type(e))
print(type(f))
print(type(g))

# Boolean (bool)
# Boolean adalah type data yang berupa True atau False ( True = 1, False = 0), 
# biasanya digunakan untuk operasi logika.
# Contoh:

h = True # ini adalah boolean
i = False # ini adalah boolean
print(type(h))
print(type(i))

# Ada juga type data lainnya, seperti:
# 1. List
# 2. Tuple
# 3. Complex
# 4. Dictionary

# List (list)
# List adalah type data yang berupa kumpulan data yang berurutan. 
# List bisa berisi data dengan type yang berbeda.
# List diapit oleh kurung siku [] dan data dipisahkan oleh koma (,).
# Contoh:

j = [1, 2, 3, 4, 5] # ini adalah list
k = ["a", "b", "c", "d", "e"] # ini adalah list
l = [1, "a", 2, "b", 3, "c"] # ini adalah list
print(type(j))
print(type(k))
print(type(l))

# Tuple (tuple)
# Tuple adalah type data yang berupa kumpulan data yang berurutan. 
# Tuple bisa berisi data dengan type yang berbeda.
# Tuple diapit oleh kurung biasa () dan data dipisahkan oleh koma (,).
# Contoh:

m = (1, 2, 3, 4, 5) # ini adalah tuple
n = ("a", "b", "c", "d", "e") # ini adalah tuple
o = (1, "a", 2, "b", 3, "c") # ini adalah tuple
print(type(m))
print(type(n))
print(type(o))

# Complex (complex)
# Complex adalah type data yang berupa bilangan kompleks. 
# Complex terdiri dari bilangan real dan bilangan imajiner.
# Complex diapit oleh kurung kurawal {} dan bilangan real dan imajiner dipisahkan oleh tanda koma (,).
# Contoh:

p = 1 + 2j # ini adalah complex
q = 3 + 4j # ini adalah complex
r = 5 + 6j # ini adalah complex
print(type(p))
print(type(q))
print(type(r))

# Dictionary (dict)
# Dictionary adalah type data yang berupa kumpulan pasangan key dan value. Dictionary tidak berurutan.
# Dictionary diapit oleh kurung kurawal {} dan pasangan key dan value dipisahkan oleh tanda koma (,).
# Contoh:

s = {"nama": "Nico", "umur": 16, "alamat": "Purwosari"} # ini adalah dictionary
t = {"a": 1, "b": 2, "c": 3} # ini adalah dictionary
u = {"1": "a", "2": "b", "3": "c"} # ini adalah dictionary
print(type(s))
print(type(t))
print(type(u))