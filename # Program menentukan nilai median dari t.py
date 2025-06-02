# Program menentukan nilai median dari tiga bilangan
# Input tiga bilangan dari pengguna
a = int(input("Masukkan bilangan pertama: "))
b = int(input("Masukkan bilangan kedua: "))
c = int(input("Masukkan bilangan ketiga: "))

# Masukkan ke dalam list dan urutkan
bilangan = [a, b, c]
bilangan.sort()

# Median adalah elemen di tengah setelah diurutkan
median = bilangan[1]

print("Bilangan setelah diurutkan:", bilangan)
print("Nilai median:", median)
