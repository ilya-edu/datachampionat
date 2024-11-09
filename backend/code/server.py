# Модуль для серва API предикта для фронта
# Автор: Денис К., Milling Team, 2020

import json
from flask import Flask
from flask import request
app = Flask(__name__)

# Если не поставили сети для nltk)
# import nltk_install

import predictCriteria

@app.route('/api/req/')
def predictSmart():
    """
    Роутим такой url с запросом сюда, предиким и в респонс льем предикт по критериям
    """
    target = request.args.get('q', '')
    response = {
        "S" : predictCriteria.getS(target),
        "A" : predictCriteria.getA(target),
        "T" : predictCriteria.getT(target),
        "education" : predictCriteria.getEducation(target),
        "unambiguity" : predictCriteria.getUnambiguity(target)
    }
    return json.dumps(response, indent=4)


if __name__ == '__main__':
    """
    'Точка входа'
    """
    app.debug = True # Рубим для прода в !True
    app.run(port='80') # для dev - 8082
