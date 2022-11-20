import csv

def add_phone():
    with open('phone_book.csv', 'a', newline='') as file:
        name_records = ('id', 'name', 'surname', 'birth', 'employment', 'phone')
        new_record = []
        for i in range(len(name_records)):
            print(f'Enter {name_records[i]}: ', end='')
            rec = input()
            new_record.append(rec)
        writer = csv.writer(file)
        writer.writerow(new_record)

def read_phone():
    with open('phone_book.csv', "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)