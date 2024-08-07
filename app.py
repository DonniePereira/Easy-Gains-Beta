from flask import Flask, redirect, render_template, request, session, url_for, jsonify
from calc import calc, protein
import sqlite3
from refeicoes import breakfast, lanche_manha, almoco, lanche_tarde, jantar
from api import get_photos
import random
from new import new

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

    breakfast_func = breakfast(total)
    lanche_manha_func = lanche_manha(total)
    almoco_func = almoco(total)
    lanche_tarde_func = lanche_tarde(total)
    jantar_func = jantar(total)

    pao_frances = breakfast_func['pao frances']
    leite_integral = breakfast_func['leite integral']
    banana = breakfast_func['banana']

    amendoas = lanche_manha_func['amendoas']

    arroz_branco = almoco_func['arroz branco']
    feijao_carioca = almoco_func['feijao carioca']
    carne_vaca = almoco_func['carne de vaca']
    batata_doce = almoco_func['batata doce']

    pao_de_forma = lanche_tarde_func['pao de forma']

    ovo_frito = jantar_func['ovo frito']
    macarrao = jantar_func['macarrao']

    data = {
        'pao_frances': pao_frances,
        'leite_integral': leite_integral,
        'banana': banana,
        'amendoas': amendoas,
        'arroz_branco': arroz_branco,
        'feijao_carioca': feijao_carioca,
        'carne_vaca': carne_vaca,
        'batata_doce': batata_doce,
        'pao_de_forma': pao_de_forma,
        'ovo_frito': ovo_frito,
        'macarrao': macarrao,
        'total': format(total, '.2f')
    }

    return render_template('copo.html', **data)

@app.route('/change_photo/<argument>', methods=['GET'])
def change_photo(argument):

    if argument == 'breakfast':
        lista = ['sweet potato', 'almonds'] 

        random_num = random.randint(0, 1)

        photo = get_photos(lista[random_num])

        return jsonify({'url': photo, 'query': lista[random_num]})

    # Como aqui tem menos alimentos crie um algoritmo para selecionar os alimentos mais caloricos que estão dentro do escopo de lanche da manhã
    if argument == 'lanche-manha':
        lista = ['banana', 'sweet potato']

        random_num = random.randint(0, 1)

        photo = get_photos(lista[random_num])

        return jsonify({'url':photo, 'query': lista[random_num]})
        
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