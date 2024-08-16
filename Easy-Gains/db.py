import csv
import sqlite3

def create_tb():
    db = sqlite3.connect('app.db')
    cursor = db.cursor()
    with open('alimentos.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
           
        cursor.executemany("INSERT INTO alimentos VALUES (?,?,?,?,?,?)", reader)

        db.commit()

create_tb()