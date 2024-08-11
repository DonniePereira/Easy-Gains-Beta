import sqlite3
import csv

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

inserir_csv()