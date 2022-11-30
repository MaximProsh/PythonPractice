from datetime import datetime as dt


def log_read(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a', newline='') as file:
        file.write('{}; readed database, length is;  {} \n'
                    .format(time, data))

def log_add(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a', newline='') as file:
        file.write('{}; added row; {} \n'
                    .format(time, data))

def log_del(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a', newline='') as file:
        file.write('{}; deleted row; {} \n'
                    .format(time, data))