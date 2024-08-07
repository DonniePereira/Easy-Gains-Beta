import csv
import sqlite3

def create_tb():
    db = sqlite3.connect('app.db')
    cursor = db.cursor()
    with open('alimentos.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
           
        cursor.executemany("INSERT INTO alimentos VALUES (?,?,?,?,?,?)", reader)

        db.commit()

def inserir_csv():
    db = sqlite3.connect('app.db')
    cursor = db.cursor()
    with open('alimentos.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)

        linha_recente = None

        for row in reader:
            linha_recente = row

        
        cursor.execute("INSERT INTO alimentos VALUES (?,?,?,?,?,?)", linha_recente)

        db.commit()

    return linha_recente[0]

