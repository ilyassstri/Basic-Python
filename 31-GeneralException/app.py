# Exception handling di python menggnunakan try
try:
    level = input("Level kamu :")
    level = int(level)
    level = level / 0
    print(level)
except:
    print("Terjadi kesalahan")