# Contoh 1 
numbers = [1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

for item in numbers:
    if item % 3 :
        print(item)

# Contoh 2
for item in range(1, 11):
    print(item)

# Contoh 3
for item in range(1, 11, 2):
    print(item)

# print('Numbers from 1 to 100:')
# for n in range(1, 101):
#     if n % 3 :
#         print(n)
#         if n % 3 and 5 :
#             print(n)
#     print(n, end=' ')

# Take a list of numbers
# my_list = [1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# hasil = []

# use anonymous function to filter
# result = list(filter(lambda x: (x % 3 == 0), my_list))
# result2 = list(filter(lambda x: (x % 5 == 0 and x % 3 == 0), my_list))
# result3 = list(filter(lambda x: (x % 5 != 0 and x % 3 != 0), my_list))

# display the result
# print(my_list)
# print("Numbers divisible by 3 are",result)
# print("Numbers divisible by 3 and 5 are",result2)
# print("Numbers divisible by 3 and 5 are",result3)

# for number in range(1, 10):
#     if(number / 3 == 0):
#         print(number)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Use a list comprehension to create a new list that includes
# "EVEN" for even numbers and "ODD" for odd numbers
# even_or_odd = ["EVEN" if n % 3 == 0 else "Harusnya angka" for n in numbers]

# print(even_or_odd)
# Output: ["ODD", "EVEN", "ODD", "EVEN", "ODD", "EVEN", "ODD", "EVEN", "ODD", "EVEN"]


my_list = []

for i in range(1, 100):
    my_list.append(i)

# print(my_list) # 👉️ [1 s/d 100]

kosong = []
for number in my_list:
    if number % 3 == 0 and number % 5 == 0:
        kosong.append("ApaBole")
    elif number % 3 == 0:
        # print("even")
        kosong.append("Apa")
    elif number % 5 == 0:
        kosong.append("Bole")
    else:
        # print(number)
        kosong.append(number)

print(kosong)

print("ini contoh lainnya")
# print('Numbers from 1 to 100:')
for n in range(1, 101):
    # if n % 3 :
    #     print(n)
    #     if n % 3 and 5 :
    #         print(n)
    print(n, end=' ')

for n in range(1000, 3000):
    print(n, end=" ")