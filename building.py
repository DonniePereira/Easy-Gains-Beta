import sqlite3 
from new import rt

def new_adp(alimento, length, total):
    
    db = sqlite3.connect('app.db')
    cursor = db.cursor()

    dictionary = {'alimento': None}

    query = cursor.execute("SELECT * FROM alimentos WHERE alimento = (?)", (alimento,)).fetchone()

    dictionary['alimento'] = query[1:]

    refeicoes = total / 5

    calories = refeicoes / length

    result_dictionary = rt(dictionary, calories)

    print(result_dictionary)

    return result_dictionary

new_adp('arroz branco', 4, 2588.5593)