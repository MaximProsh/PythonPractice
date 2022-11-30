import csv
import pandas as pd
import os
import logger
import user_interface

name_records = ('id', 'name', 'surname', 'birth', 'position', 'address', 'phone', 'add phone')

def read_db():
    with open('firm_db.csv', 'a', newline='') as file:
        if os.stat("firm_db.csv").st_size == 0:
            writer = csv.writer(file)
            writer.writerow(name_records)
            logger.log_add('header')
    df = pd.read_csv('firm_db.csv')
    length = len(df.index)
    logger.log_read(length)
    print(df)

def add_new_line():
    with open('firm_db.csv', 'a', encoding="utf-8", newline='') as file:
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
    flag = 0
    while flag != 1:
        try: 
            print('Enter row id that you want to delete: ', end='')
            del_id = int(input())
            df = pd.read_csv('firm_db.csv')  
            df = df.drop(index=[del_id])
            df = df.reset_index(drop=True)
            df.to_csv('firm_db.csv', index=False)
            flag += 1
        except KeyError:
            print('Wrong index\n')
            user_interface.user_choise()
            break