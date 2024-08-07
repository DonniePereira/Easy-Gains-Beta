import sqlite3 

# Usar a mesma conexão de um banco de dados com o cursor para várias funções causa um problema de threading então criei um cursor em cada função

# db = sqlite3.connect('app.db')
# cursor = db.cursor()

def breakfast(total):
    
    db = sqlite3.connect('app.db')
    cursor = db.cursor()

    breakfast = {}

    alimentos = ['pao frances', 'leite integral', 'banana']

    # *alimentos isso basicamente desempacota cada item da lista para substituir os pontos de interrogação sem isso alimentos inteiro iria para o primeiro ? e não separadamente
    query = cursor.execute("SELECT * FROM alimentos WHERE alimento IN (?,?,?)", alimentos)

    for row in query:
        breakfast[row[0]] = row[1:]

    refeicoes = total / 5

    calories = refeicoes / len(alimentos)

    # Obtenha a chave na posição atual e obtenha as calorias do valor da chave atual. Ou seja loop.

    # mark 1
    pao_frances = breakfast['pao frances'][1]

    leite_integral = breakfast['leite integral'][1]

    banana = breakfast['banana'][1]

    pao_frances_gramas = round(((calories / pao_frances) * 100),2)

    leite_integral_gramas = round(((calories / leite_integral) * 100),2)

    banana_gramas = round(((calories / banana) * 100),2)

    # mark 2
    array = [pao_frances_gramas, leite_integral_gramas, banana_gramas]

    # Faça um código para obter o nome do alimento em questão, crie o dicionário result de forma automática com a chave sendo esse nome e o valor sendo o resultado do cálculo as gramas, mesma coisa mas de forma menos manual.  
    result = {
        'pao frances': array[0],
        'leite integral': array[1],
        'banana': array[2]
    }

    # return print(result)

    return (result)


def lanche_manha(total):

    db = sqlite3.connect('app.db')
    cursor = db.cursor()   

    lanche_manha = {}

    alimentos = ['amendoas', 'banana']

    query = cursor.execute("SELECT * FROM alimentos WHERE alimento IN (?,?)", alimentos)

    for row in query:
        lanche_manha[row[0]] = row[1:]

    refeicoes = total / 5

    calories = refeicoes / len(alimentos)

    amendoas = lanche_manha['amendoas'][1]

    bananas = lanche_manha['banana'][1]

    
    amendoas_gramas = round(((calories / amendoas) * 100),2)

    bananas_gramas = round(((calories / bananas) * 100),2)

    array = [amendoas_gramas, bananas_gramas]

    result = {
        'amendoas': array[0],
        'banana': array[1]
    }

    # return print(result)

    return (result)

def almoco(total):

    db = sqlite3.connect('app.db')
    cursor = db.cursor()

    almoco = {}

    alimentos = ['arroz branco', 'feijao carioca', 'carne de vaca', 'batata doce']

    query = cursor.execute("SELECT * FROM alimentos WHERE alimento IN (?,?,?,?)", alimentos)

    for row in query:
        almoco[row[0]] = row[1:]

    refeicoes = total / 5

    calories = refeicoes / len(alimentos)

    arroz_branco = almoco['arroz branco'][1]

    feijao_carioca = almoco['feijao carioca'][1]

    carne_vaca = almoco['carne de vaca'][1]

    batata_doce = almoco['batata doce'][1]


    arroz_branco_gramas = round(((calories / arroz_branco) * 100),2)

    feijao_carioca_gramas = round(((calories / feijao_carioca) * 100),2)

    carne_vaca_gramas = round(((calories / carne_vaca) * 100),2)

    batata_doce_gramas = round(((calories / batata_doce) * 100),2)

    array = [arroz_branco_gramas, feijao_carioca_gramas, carne_vaca_gramas, batata_doce_gramas]

    result = {
        'arroz branco': array[0],
        'feijao carioca': array[1],
        'carne de vaca': array[2],
        'batata doce': array[3]
    }

    # return print(result)

    return (result)

def lanche_tarde(total):

    db = sqlite3.connect('app.db')
    cursor = db.cursor()

    lanche_tarde = {}

    alimentos = ['pao de forma', 'leite integral', 'banana']

    query = cursor.execute("SELECT * FROM alimentos WHERE alimento IN (?,?,?)", alimentos)

    for row in query:
        lanche_tarde[row[0]] = row[1:]

    refeicoes = total / 5

    calories = refeicoes / len(alimentos)

    pao_de_forma = lanche_tarde['pao de forma'][1]

    leite_integral = lanche_tarde['leite integral'][1]

    banana = lanche_tarde['banana'][1]

    pao_forma_gramas = round(((calories / pao_de_forma) * 100),2)

    leite_integral_gramas = round(((calories / leite_integral) * 100),2)

    banana_gramas = round(((calories / banana) * 100),2)

    array = [pao_forma_gramas, leite_integral_gramas, banana_gramas]

    result = {
        'pao de forma': array[0],
        'leite integral': array[1],
        'banana': array[2]
    }

    # return print(result)
    return (result)

def jantar(total):

    db = sqlite3.connect('app.db')
    cursor = db.cursor()

    jantar = {}

    alimentos = ['macarrao', 'batata doce', 'ovo frito']

    query = cursor.execute("SELECT * FROM alimentos WHERE alimento IN (?,?,?)", alimentos)

    for row in query:
        jantar[row[0]] = row[1:]

    refeicoes = total / 5

    calories = refeicoes / len(alimentos)

    # 2 ovos 
    # 200 gramas de macarrao
    # 100 gramas de batata doce

    # Multiplique o índice 2 da tupla de cada chave até alcançar as calorias

    # ovo = jantar['ovo frito'][1]

    #macarrao = jantar['macarrao'][1]

    #batata_doce = jantar['macarrao'][1]

    #conta  = [ovo, macarrao, batata_doce]

    #for i in range(len(conta)):
       #while conta[i] < calories:
           #conta[i] += 1

       #while conta[i] > calories:
           #conta[i] -= 1

    ovo = jantar['ovo frito'][1]

    macarrao = jantar['macarrao'][1]

    batata_doce = jantar['batata doce'][1]


    ovo_gramas =  round(((calories / ovo) * 100),2)

    macarrao_gramas = round(((calories / macarrao) * 100),2)

    batata_doce_gramas = round(((calories / batata_doce) * 100),2)

    array = [ovo_gramas, macarrao_gramas, batata_doce_gramas]

    result = {
        'ovo frito': array[0],
        'macarrao': array[1],
        'batata doce': array[2]
    }

    # return print(result)
    return (result)

total = 2555

breakfast(total)
lanche_manha(total)
almoco(total)
lanche_tarde(total)
jantar(total)



# Ex macarrão: 

# 172 / 130 = 1,32

# 1,32 * 100 = 132,307