# Dictionary adalah sebuah structur data yang bisa menyimpan data dalam bentuknya key atau kunci, value nilai, fear

# user =
"""
    name
    age
    is_admin
"""

print("Hello Dunia")
print("Mencoba lagi")

user = {
    "name" : "M. Ilyas Tri Khaqiqi",
    "Age" : 20,
    "is_admmin" : True
}

name = user["name"]
age = user["Age"]
is_admin = user["is_admmin"]

print(name)
print(age)
print(is_admin)

user["username"] = "Muhammad Ilyas"
user["name"] = "M. Ilyas Tri Khaqiqi, M.T, Ph.D"

temp1 = user.get("username", "ilyassstri")
temp = user.get("name", "Age")

print("")
print(temp1)
print(temp)

# None adalah sebuah type data yang menggambarkan bahwa sesuatu itu tidak ada.