import pandas as pd
import csv

def add_phone():
    with open('phone_book.csv', 'a', newline='') as file:
        data = csv.reader(file, delimiter=' ', quotechar='|')
        for row in spamreader:
            print(', '.join(row))
add_phone


