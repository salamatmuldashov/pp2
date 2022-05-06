import psycopg2
from config import database
import csv
config = psycopg2.connect(**database)
current = config.cursor()

def insert():
    insert_table = '''
        INSERT INTO phonebook VALUES(%s,%s,%s);
    '''
    count = int(input('1 если хотите ввести через терминал, 2 иначе: '))
    if count == 1:
        name = str(input("Введите имя: "))
        surname = str(input("Введите фамилию: "))
        number = str(input("Введите номер телефона: "))
        current.execute(insert_table, (name,surname,number))

    if count == 2:
        with open("example.csv", "r") as file:
            f = csv.reader(file, delimiter=",")
            for row in f:
                current.execute(insert_table,row)

        config.commit()

def delete():
    delete = """
    DELETE FROM PhoneBook WHERE name = %s;
    """
    name = str(input("Введите имя: "))
    current.execute(delete,[name])

def update():
    update = """
    UPDATE PhoneBook SET number = %s WHERE name = %s;
    """
    name = input("Введите имя:")
    number = input("Введите номер:")
    current.execute(update, (number,name))
    config.commit()


def select():
    select = """
    SELECT * FROM PhoneBook;
    """
    current.execute(select)
    print(current.fetchall(), sep='\n')
    config.commit()

while True:
    command = str(input("insert,update,delete,select,exit: \n"))
    if command == 'insert':
        insert()
    if command == 'delete':
        delete()
    if command == 'update':
        update()
    if command == 'select':
        select()
    if command == 'exit':
        break

current.close()
config.commit()
config.close()

    


