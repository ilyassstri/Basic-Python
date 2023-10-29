# Tuple / Array bisa memakai unpack
numbers = (1, 2, 3)

# x = numbers[0]
# y = numbers[1]
# z = numbers[2]

# print(x)

# Unpack syntax/Memakai cara unpack
x, y, z = numbers
print(z)

_, y, _ = numbers
print(y)

x, _, _ = numbers
print(x)

x, *a = numbers

print("")
print(x)
print(a)



campurans = (1, "dua", 3, "empat")

a, b, c, d = campurans
print(d)