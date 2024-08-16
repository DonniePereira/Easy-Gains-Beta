def calc(genero, peso, altura, idade, naf, superavit):

    Naf = None

    if naf == 'sedentario': 
        Naf = 1.2

    elif naf == 'moderadamente':
        Naf = 1.55

    elif naf == 'muito_ativo':
         Naf = 1.725

    if genero == 'masculino':
        calc_Peso = 13.397 * peso
        calc_Altura = 4.799 * altura
        calc_Idade = 5.677 * idade

        tmb = 88.362 + calc_Peso + calc_Altura - calc_Idade

        # tmb = float(tmb)

        total = float(tmb * Naf)

        total += superavit

        return total
    
    elif genero == 'feminino':
        calc_Peso = 9.247 * peso
        calc_Altura = 3.098 * altura
        calc_Idade = 4.330 * idade

        tmb = 447.593 + calc_Peso + calc_Altura - calc_Idade

        # tmb = float(tmb)

        total = float(tmb * Naf)

        total += superavit

        return total
    
#print (calc('masculino', 55, 174, 21, 'muito_ativo', 200))

def protein(peso):
    
    return peso * 1.6

def carbs():
    calorias_totais = calc('masculino', 55, 174, 21, 'muito_ativo', 200)

    calorias_carboidratos = calorias_totais * 0.50

    gramas_carboidratos = calorias_carboidratos / 4

    #return print(calorias_carboidratos)

def gorduras(peso):
    return peso * 1.2





#carbs()


