"""
HARUS DIINGAT OPERATOR PERBANDINGAN :
==          : sama dengan
===         : identik
!=          : tidak sama
!==         : tidak identik
<>          : tidak sama --> ini tidak bisa dilakukan di kodingan boy
>           : lebih besar dari
<           : lebih kecil dari
>=          : lebih besar dari sama dengan
<=          : lebih kecil dari sama dengan
"""

print(""" Contoh 1 """)

result = 4 > 3
print(result)

result = 4 < 3
print(result)

result = 4 >= 3
print(result)

result = 4 <= 3
print(result)

result = 4 == 3
print(result)

result = 4 != 3
print(result)

print(""" Contoh 2 """)

grade = 5

if grade >= 8:
    print("Nilai kamu A")
elif grade >= 7:
    print("nilai kamu B")
elif grade >= 6:
    print("nilai kamu C")
else:
    print("Kamu harus mengulang kelas")


print(""" Contoh 3 """)

IPK = 2

if IPK >= 3.5:
    print("Selamat kamu cumlaude")
elif IPK >= 3:
    print("Selamat nilai kamu lumayan bagus")
elif IPK >= 2:
    print("Selamat kamu belum lulus")


