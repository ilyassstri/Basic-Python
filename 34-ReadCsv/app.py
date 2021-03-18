import csv

users = open("users.csv", "r")
users_csv = csv.reader(users, delimiter=",")
# print(users_csv)

for row in users_csv:
    print(f"Name : {row}. Username : {row[1]}. Role : {row[-1]}")

users.close()