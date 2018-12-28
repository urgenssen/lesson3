import csv

with open('users.csv', 'r', encoding='utf-8') as f:
    fields = ['first_name', 'last_name', 'email', 'gender', 'age']
    reader = csv.DictReader(f, fields, delimiter=';')
    total_age = 0
    for row in reader:
        total_age+=int(row['age'])
    print(total_age)