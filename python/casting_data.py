# Casting data di python adalah mengubah type data dari suatu type data ke type data lainnya. 
# Misalnya dari integer ke string, dari string ke integer, dan lain sebagainya.
# Contoh:

# String ke Integer, Float, Boolean

a = "123" # ini adalah string
b = int(a) # untuk mengubah string ke integer, kita bisa menggunakan int()
c = float(a) # untuk mengubah string ke float, kita bisa menggunakan float()
d = bool(a) # untuk mengubah string ke boolean, kita bisa menggunakan bool()
print(a, "adalah string", type(a))
print(b, "adalah integer", type(b))
print(c, "adalah float", type(c))
print(d, "adalah boolean", type(d))

# Integer ke String, Float, Boolean

e = 123 # ini adalah integer
f = str(e) # untuk mengubah integer ke string, kita bisa menggunakan str()
g = float(e) # untuk mengubah integer ke float, kita bisa menggunakan float()
h = bool(e) # untuk mengubah integer ke boolean, kita bisa menggunakan bool()
print(e, "adalah integer", type(e))
print(f, "adalah string", type(f))
print(g, "adalah float", type(g))
print(h, "adalah boolean", type(h))

# Float ke String, Integer, Boolean

i = 123.45 # ini adalah float
j = str(i) # untuk mengubah float ke string, kita bisa menggunakan str()
k = int(i) # untuk mengubah float ke integer, kita bisa menggunakan int()
l = bool(i) # untuk mengubah float ke boolean, kita bisa menggunakan bool()
print(i, "adalah float", type(i))
print(j, "adalah string", type(j))
print(k, "adalah integer", type(k))
print(l, "adalah boolean", type(l))

# Boolean ke String, Integer, Float

m = True # ini adalah boolean
n = str(m) # untuk mengubah boolean ke string, kita bisa menggunakan str()
o = int(m) # untuk mengubah boolean ke integer, kita bisa menggunakan int()
p = float(m) # untuk mengubah boolean ke float, kita bisa menggunakan float()
print(m, "adalah boolean", type(m))
print(n, "adalah string", type(n))
print(o, "adalah integer", type(o))
print(p, "adalah float", type(p))
