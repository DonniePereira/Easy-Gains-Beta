from new import new

# Conjuntos

set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Une os conjuntos 
union_set = set1 | set2 
#print(union_set)

# Verifica qual valor está presente nos dois conjuntos
intersection_set = set1 & set2 
#print(intersection_set)

# Obtém apenas os elementos que estão presentes no primeiro conjunto
difference_set = set1 - set2
#print(difference_set)


def generate_meals(total):
    breakfast_array = ['pao frances', 'leite integral', 'banana']

    lanche_manha_array = ['amendoas', 'banana', 'leite integral']

    almoco_array = ['arroz branco', 'feijao carioca', 'carne de vaca', 'batata doce']

    lanche_tarde_array = ['pao de forma', 'leite integral', 'banana']
    # A escolha de alimentos base para o template tem como principal requisito evitar a repetição, ao mesmo tempo que escolhe os alimentos com maior densidade calórica para evitar uma refeição massiva com muitas gramas por alimento
    jantar_array = ['ovo frito', 'macarrao', 'batata doce']

    ceia_array = ['amendoas', 'leite integral']

    from new import new

    #total = 2500

    breakfast_query = new(breakfast_array, total)

    lanche_manha_query = new(lanche_manha_array, total)

    almoco_query = new(almoco_array, total)

    lanche_tarde_query = new(lanche_tarde_array, total)

    jantar_query = new(jantar_array, total)

    #ceia_query = new(ceia_array, total)

    #dictList = [ 
    #    breakfast_query, 
    #    lanche_manha_query, 
    #    almoco_query, 
    #    lanche_tarde_query, 
    #    jantar_query,
        #ceia_query
    #]

    # Essa parte vem da ideia de como eu vou evitar que as chaves se repitam

    # Cria um conjunto e preenche com as chaves do dicionário
    #conjunto = set()

    #for row in dictList:
        #conjunto.update(row.keys())

    #novo = {}

    #for row in conjunto:
        #novo[row] = None


    #cup = ['brakfast', 'lanche_manha', 'almoco', 'lanche_tarde', 'jantar']


    # Pega uma chave de um dicionário e renomeia a chave com breakfast. Ex: 'pao frances' vira ('breakfast pao frances') 
    breakfast_grams = {}

    for a, b in breakfast_query.items():
        breakfast_grams[f'breakfast {a}'] = b

    lanche_manha_grams = {}

    for a, b in lanche_manha_query.items():
        lanche_manha_grams[f'lanche manha {a}'] = b

    almoco_grams = {}

    for a, b in almoco_query.items():
        almoco_grams[f'almoco {a}'] = b

    lanche_tarde_grams = {}

    for a, b in lanche_tarde_query.items():
        lanche_tarde_grams[f'lanche tarde {a}'] = b

    jantar_grams = {}

    for a, b in jantar_query.items():
        jantar_grams[f'jantar {a}'] = b

    #ceia_grams = {}

    #for a, b in ceia_query.items():
     #   ceia_grams[f'ceia {a}'] = b

    #print(breakfast_grams)
    #print(lanche_manha_grams)
    #print(almoco_grams)
    #print(lanche_tarde_grams)
    #print(jantar_grams)

    return_list = [
        breakfast_grams,
        lanche_manha_grams,
        almoco_grams,
        lanche_tarde_grams,
        jantar_grams,
        #ceia_grams
    ]

    #breakfast_grams
    #lanche_manha_grams
    #almoco_grams
    #lanche_tarde_grams
    #jantar_grams


    # list() em Python converte um objeto para uma lista

    # Código adaptado pela IA, minha parte (breakfast_grams)
    first_key = list(breakfast_grams.keys())[0]

    #print(first_key)

    # return só pode ser usado dentro de uma função, eu sei você vai revisar e dizer "óbvio" mas por favor seja humilde, e fala verdade aquela esclarecida literal é sempre bom. 

    return return_list 

generate_meals(2500)