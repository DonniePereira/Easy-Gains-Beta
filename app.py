from flask import Flask, redirect, render_template, request, session, url_for, jsonify
from calc import calc, protein
import sqlite3
from refeicoes import breakfast, lanche_manha, almoco, lanche_tarde, jantar
from api import get_photos
import random
# from new import new
from lab import lab
from building import new_adp

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
    
    lista_de_dicionarios = lab(total)

    return render_template('copo.html', lista_de_dicionarios=lista_de_dicionarios, total=total)

@app.route('/change_photo/<argument>/<total>', methods=['GET']) #<total>'
def change_photo(argument, total): #total

    total = float(total)

    if argument == 'breakfast':
        lista = ['sweet potato', 'almonds'] 

        lista_br = ['batata doce', 'amendoas']

        random_num = random.randint(0, 1)

        photo = get_photos(lista[random_num])

        # Nota essa parte de código se repete para todas as refeições nos ifs então a ideia é a mesma

        # A ideia é que eu sei quantos alimentos tem em ada refeição, mas se no futuro eu for usar um método mais sofisticado ou melhor desenhado, a length seria com base em algo mais dinâmico, e baseado em algoritmo

        debug = lista_br[random_num]

        length = 3

        print(debug)

        att_grams_info = new_adp(debug, length, total)

        return jsonify({'url': photo, 'query': lista[random_num], 'att': att_grams_info['alimento']}) #'att': att_grams_info}

    # Como aqui tem menos alimentos crie um algoritmo para selecionar os alimentos mais caloricos que estão dentro do escopo de lanche da manhã
    if argument == 'lanche-manha':
        lista = ['banana', 'sweet potato']

        random_num = random.randint(0, 1)

        photo = get_photos(lista[random_num])

        return jsonify({'url': photo, 'query': lista[random_num]})
        
    if argument == 'almoco':
        lista = ['pasta', 'eggs']

        random_num = random.randint(0, 1)

        photo = get_photos(lista[random_num])

        return jsonify({'url': photo, 'query': lista[random_num]})

    if argument == 'lanche-tarde':
        lista = ['eggs', 'almonds', 'sweet potato']

        random_num = random.randint(0, 2)

        photo = get_photos(lista[random_num])

        return jsonify({'url': photo, 'query': lista[random_num]})

    if argument == 'jantar':
        lista = ['bean', 'meat']

        random_num = random.randint(0, 1)

        photo = get_photos(lista[random_num])

        return jsonify({'url': photo, 'query': lista[random_num]})

    #photo = get_photos('nature')
    #return jsonify({'url': photo})


if __name__ == '__main__':
    app.run(debug=True)