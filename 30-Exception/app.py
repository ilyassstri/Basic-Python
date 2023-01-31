# Exception handling di python menggnunakan try untuk menyiatasi code yang error
try:
    level = input("Level kamu :")
    level = int(level)
    level = level / 0
    print(level)
except ZeroDivisionError:
    print("Angka yang kamu masukkan tidak bisa dibagi 0")
except ValueError:
    print("Yang kamu masukkan bukan angka!")
