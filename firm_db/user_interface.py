import read_add_db

def user_choise():
    print('''Your choise:
    1. Add new information
    2. Delete a row
    3. See the database''')
    choise = int(input())
    if choise == 1:
        return read_add_db.add_new_line()
    elif choise == 2:
        return read_add_db.del_row()
    elif choise == 3:
        return read_add_db.read_db()
    else:
        print('Error input')