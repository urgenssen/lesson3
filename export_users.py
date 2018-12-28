import csv


user_list = [
{'first_name':'Anry', 'last_name':'Bolt', 'email':'anry@yandex.ru', 'gender':'male', 'age':'34'},
{'first_name':'Vilthor', 'last_name':'Simmon', 'email':'si_87@google.com', 'gender':'male', 'age':'39'}
]

with open('export.csv', 'w', encoding='utf-8', newline='') as f:
    fields = ['first_name', 'last_name', 'email', 'gender', 'age']
    writer = csv.DictWriter(f, fields, delimiter=';')
    writer.writeheader()
    for user in user_list:
        writer.writerow(user)