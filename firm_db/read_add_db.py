import csv
import pandas as pd
import os
import logger

name_records = ('id', 'name', 'surname', 'birth', 'position', 'address', 'phone', 'add phone')

def read_db():
    df = pd.read_csv('firm_db.csv')
    length = len(df.index)
    logger.log_read(length)
    print(df)

def add_new_line():
    with open('firm_db.csv', 'a', newline='') as file:
        if os.stat("firm_db.csv").st_size == 0:
            writer = csv.writer(file)
            writer.writerow(name_records)
            logger.log_add('header')        
        new_record = []
        for head in name_records:
            print(f'Enter {head}: ', end='')
            rec = input()
            new_record.append(rec)
        writer = csv.writer(file)
        writer.writerow(new_record)
        logger.log_add('body') 

def del_row():
    print('Enter row id that you want to delete: ', end='')
    dele_id = int(input())
    df = pd.read_csv('firm_db.csv')
    df = df.drop(index=[dele_id])
    df = df.reset_index(drop=True)
    df.to_csv('firm_db.csv', index=False)