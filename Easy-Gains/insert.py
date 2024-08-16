import sqlite3
import csv

def insert_lines():
    db = sqlite3.connect('app.db')
    cursor = db.cursor()
    with open('alimentos.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)

        rows = list(reader)
       
        consulta = list(cursor.execute("SELECT * FROM alimentos").fetchall())

        #print(consulta)

        array = []

        another_array = []

        dictionary = {}

        for element, row in zip(rows, consulta):
            if element[0] == row[0]:
                array.append(row[0])


        length = len(array)
       
        length2 = len(rows)

        result = length2 - length
       
        another_array.extend(rows[length2 - result:])

        cursor.executemany("INSERT INTO alimentos VALUES (?,?,?,?,?,?)", another_array)

        db.commit()

       
    db.close()

        ##print(dictionary)

    #cursor.execute("INSERT INTO alimentos VALUES (?,?,?,?,?,?)", reader)

        #db.commit()

    

insert_lines()
