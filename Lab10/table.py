import psycopg2
from config import database

cnf = psycopg2.connect(**database)
current = cnf.cursor()

table = '''
    CREATE TABLE phonebook(
        person_name VARCHAR(255),
        person_surname VARCHAR(255),
        person_number VARCHAR(255)
        )
'''

current.execute(table)

current.close()
cnf.commit()
cnf.close()