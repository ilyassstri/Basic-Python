""" Contoh 1 """
is_day = False # ciri khas boolean memakai is dan bila dua kata memakan underscorse
is_night = True

if is_day:
    print("Selamat siang bro bro bro")
elif is_night:
    print("Selamat malam")
else:
    print("Selamat bersenang-senang")

""" Contoh 2 """
is_day = False
is_night = False

if is_day:
    print("Belajar dengan semangat pada siang hari!")
elif is_night: 
    print("Saatnya istirahat pada malam hari.")
else:
    print("Saatnya begadang tugas banyakkk cuy!")

# print("Selamat menikmati harimu")
gaji_bulanan = 10
cicilan_motor = 2000000
if gaji_bulanan > cicilan_motor:
    print("motor akan terbeli")
elif gaji_bulanan == 0:
    print("mikir tolol")
elif gaji_bulanan <= cicilan_motor:
    print("harus mencari penghasilan tambahan")


