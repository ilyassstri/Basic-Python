numbers = [5, 6, 7, 8, 1]

""" Menghitung total """
total = sum(numbers)
print(total)

""" Mengurutkan """
max_number = max(numbers)
print(max_number)

""" Mengurutkan """
numbers.sort()
max_number = numbers[-1]
print(max_number)

""" Mencari nilai terbesar """
max_number = numbers[0]

for number in numbers:
    if number > max_number:
        max_number = number

print(max_number)

