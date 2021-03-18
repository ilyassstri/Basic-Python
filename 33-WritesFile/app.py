users = open("users.txt", "w") # w, r, r+ singkatan dari write, read, write and read file
users = open("users2.txt", "w") # bila filenya tidak ada bakalan otomatis langsung membuatkan filenya

# a = append -> untuk menambahkan data ke file yang sudah ada isinya dan menulis otomatisnya ke samping
# w = write -> untuk menulis tapi akan menghapus semua data yang ada di dalam file tersebut.

# print(users.readable()) # function untuk mencek file tersebut bisa diapakan saja
users.write("Link - link")

users.close()