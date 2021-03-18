# cara membaca sebuah isi dari file text

users = open("users.txt", "r")
# print(users.read())
# print(users.readline())
array = users.readlines()

# print(array[2])

index = 1
for user in array:
    print(f"{index} - {user}")
    index += 1

users.close()

