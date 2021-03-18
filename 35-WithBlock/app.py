import csv

with open("users.csv", "r") as users:
    users_csv = csv.reader(users, delimiter=",")

    for row in users_csv:
        print(f"Name : {row}. Username : {row[1]}. Role : {row[-1]}")
