import sqlite3

def new(alimentos, total):

    db = sqlite3.connect('app.db')
    cursor = db.cursor()

    almoco = {}
    
    placeholders = ['?'] * len(alimentos)

    placeholder_string = ', '.join(placeholders)

    query = cursor.execute(f"SELECT * FROM alimentos WHERE alimento IN ({placeholder_string})", alimentos)

    for row in query:
        almoco[row[0]] = row[1:]

    #print(almoco)

    db.close()

#new(['tomate', 'banana', 'abacate'])

    #total = 2588.56

    refeicoes = total / 5

    calories = refeicoes / len(alimentos)

    #print(rt(almoco, calories))

    dicionario = rt(almoco, calories)

    #print (dicionario)

    return dicionario

def rt(dictionary, calories):
    for key, value in dictionary.items():
     
        new_value = (round(((calories / value[1]) * value[0]), 2))

        dictionary[key] = new_value
    return dictionary


#new(['arroz branco', 'feijao carioca', 'carne de vaca',
#'batata doce'])

new(['arroz branco', 'ovo frito', 'macarrao'], 2550)

    

    


