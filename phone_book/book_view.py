import book_generator

def call_choice():
    print('I want:\n1. Add a new record\n2. Read the phone book')
    record = input()
    if record == '1':
        book_generator.add_phone()
    elif record == '2':
        book_generator.read_phone()
    else:
        print('Wrong input. Type 1 or 2')