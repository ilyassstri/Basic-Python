""" Contoh 1 """

Name = "M. Ilyas Tri Khaqiqi"
by_pass_validation = False

if len(Name) > 3 or by_pass_validation : # memakai logika or
    print("welcome")
else:
    print("Nama terlalu pendek")

if len(Name) > 3 and by_pass_validation : # memakai logika and
    print("welcome")
else:
    print("Nama terlalu pendek")

""" Contoh 2 """

motivasi = "Saya ingin menjadi seorang programmer dan dosen"
tantangan_berat = False

if len(motivasi) > 3 or tantangan_berat:
    print("Aku akan menjadi orang sukses")
else:
    print("Saya pasti sukses!")

""" Contoh 3 """

gajihan = "Ilyas hari rabu gajihan di kantornya"
tanggal_muda = True

if len(gajihan) > 10 and tanggal_muda:
    print("Ilyas akan membeli persediaan makan dan pakaian")
else:
    print("Ilyas masih belum punya uang")

"""
    False or True = True
    True or False = True
    True and False = False
    False and True = Flase
    True and True = True
"""