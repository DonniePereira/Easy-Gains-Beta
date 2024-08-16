from flask import Flask, redirect, render_template, request, session, url_for, jsonify
from calc import calc, protein
import sqlite3
from api import get_photos
import random
# from new import new
from meals import generate_meals
from generate_food_grams import generate_food_grams

app = Flask(__name__)

db = sqlite3.connect('app.db')
cursor = db.cursor()

@app.route('/', methods=['GET'])
def index():
    return redirect('/form')

@app.route('/form', methods=['GET', 'POST'])
def form():
 if request.method == "POST": 
    
      genero = request.form['genero']
      idade = int(request.form['idade'])
      altura = int(request.form['altura'])
      peso = int(request.form['peso'])
      naf = request.form['naf']
      superavit = int(request.form['superavit'])

      # Corrigido resultado trocando a ordem
      # total = calc(genero, idade, altura, peso, naf)
      total = calc(genero, peso, altura, idade, naf, superavit)

      # return render_template('batata.html', total=total)

      return redirect(url_for('dieta', total=total))

 return render_template('teste.html')


@app.route('/dieta/<total>', methods=['GET'])
def dieta(total):
    total = float(total)
    
    # A escolha de alimentos base para o template tem como principal requisito evitar a repetição, ao mesmo tempo que escolhe os alimentos com maior densidade calórica para evitar uma refeição massiva com muitas gramas por alimento
    
    lista_de_dicionarios = generate_meals(total)

    total = round(total, 2)

    return render_template('copo.html', lista_de_dicionarios=lista_de_dicionarios, total=total)

ultimo_num1 = None
ultimo_num2 = None
ultimo_num3 = None
ultimo_num4 = None
ultimo_num5 = None

@app.route('/change_food_item/<argument>/<total>', methods=['GET']) #<total>'
def change_food_item(argument, total): #total

    total = float(total)

    if argument == 'breakfast':
        lista = ['sweet potato', 'Almonds'] 

        #lista_br = ['batata doce', 'amendoas']

        global ultimo_num1

        random_num = random.randint(0, 1)

        while random_num == ultimo_num1:
            random_num = random.randint(0, 1)

        ultimo_num1 = random_num

        photo = get_photos(lista[ultimo_num1])

        # Nota essa parte de código se repete para todas as refeições nos ifs então a ideia é a mesma

        # A ideia é que eu sei quantos alimentos tem em cada refeição, mas se no futuro eu for usar um método mais sofisticado ou melhor desenhado, a length seria com base em algo mais dinâmico, e baseado em algoritmo.

        lista_br = ['batata doce', 'amendoas']

        debug = lista_br[ultimo_num1]

        length = 3

        att_grams_info = generate_food_grams(debug, length, total)

        return jsonify({'url': photo, 'query': lista[ultimo_num1], 'att': att_grams_info['alimento']}) #'att': att_grams_info}

    # Como aqui tem menos alimentos crie um algoritmo para selecionar os alimentos mais caloricos que estão dentro do escopo de lanche da manhã
    if argument == 'lanche-manha':
        lista = ['Banana', 'Sweet potato']

        global ultimo_num2

        #print(ultimo_num2)

        random_num = random.randint(0, 1)

        while random_num == ultimo_num2:
            random_num = random.randint(0, 1)

        #print(ultimo_num2)

        ultimo_num2 = random_num

        photo = get_photos(lista[ultimo_num2])

        lista_br = ['banana', 'batata doce']
        
        food_item = lista_br[ultimo_num2]

        length = 3

        #print(debug)

        att_grams_info = generate_food_grams(food_item, length, total)

        return jsonify({'url': photo, 'query': lista[ultimo_num2], 'att': att_grams_info['alimento']}) #'att': att_grams_info}
        
    if argument == 'almoco':
        lista = ['Noodle', 'Eggs']

        global ultimo_num3

        random_num = random.randint(0, 1)

        while random_num == ultimo_num3:
            random_num = random.randint(0, 1)

        ultimo_num3 = random_num

        photo = get_photos(lista[ultimo_num3])

        lista_br = ['macarrao', 'ovo frito']
        
        debug = lista_br[ultimo_num3]

        length = 4

        att_grams_info = generate_food_grams(debug, length, total)

        return jsonify({'url': photo, 'query': lista[ultimo_num3], 'att': att_grams_info['alimento']}) #'att': att_grams_info}

    if argument == 'lanche-tarde':
        lista = ['Eggs', 'Almonds', 'Sweet potato']

        global ultimo_num4

        random_num = random.randint(0, 2)

        while random_num == ultimo_num4:
            random_num = random.randint(0, 2)

        ultimo_num4 = random_num

        photo = get_photos(lista[ultimo_num4])

        lista_br = ['ovo frito', 'amendoas', 'batata doce']
        
        debug = lista_br[ultimo_num4]

        length = 3

        att_grams_info = generate_food_grams(debug, length, total)

        return jsonify({'url': photo, 'query': lista[ultimo_num4], 'att': att_grams_info['alimento']}) #'att': att_grams_info}

    if argument == 'jantar':
        lista = ['Beans', 'Meat']

        global ultimo_num5

        random_num = random.randint(0, 1)

        while random_num == ultimo_num5:
            random_num = random.randint(0, 1)

        ultimo_num5 = random_num

        photo = get_photos(lista[ultimo_num5])

        lista_br = ['feijao carioca', 'carne de vaca']
        
        debug = lista_br[ultimo_num5]

        length = 3

        att_grams_info = generate_food_grams(debug, length, total)

        return jsonify({'url': photo, 'query': lista[ultimo_num5], 'att': att_grams_info['alimento']}) #'att': att_grams_info}

    #photo = get_photos('nature')
    #return jsonify({'url': photo})


if __name__ == '__main__':
    app.run(debug=True)