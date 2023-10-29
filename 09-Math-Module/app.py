import math

# angka asli
number = 5.8
number = round(number)
print(number)

# pembulatan ke atas
number2 = 5.4
number2 = math.ceil(number2)
print(number2)

# pembulatan ke bawah
number3 = 5.4
number3 = math.floor(number3)
print(number3)

# math.ceil = pembulatan ke atas
# math.floor = pembulatan ke bawah
number4 = 6.2
number4 = math.ceil(number4)
print(number4)

# cara mengatahui nilai tan 
nilai = 90
nilai = math.tan(nilai)
print(nilai)

"""
Catatan penting
kalau ingin memanggil fungsi dari library di python :
namalibrari.panggilfungsinya lalu masukkan nilai yang akan dipanggilnya -> contohnya : nilai = math.tan(nilai)
"""