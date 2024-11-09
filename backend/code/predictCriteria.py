# Модуль предикта для фронта
# (Решение чисто в хакатоновском стиле)
# Автор: Денис К., Milling Team, 2020

import joblib

import analyse

# Инит классификаторов
text_clfS = joblib.load('models/clfS.pkl')
text_clfA = joblib.load('models/clfA.pkl')
text_clfT = joblib.load('models/clfT.pkl')
text_clfEducation = joblib.load('models/clfEducation.pkl')
text_clfUnambiguity = joblib.load('models/clfUnambiguity.pkl')


def getS(text):
    """
    Предикт для S критерия SMART
    """
    text = analyse.prepare(text)

    res = text_clfS.predict([text])

    print(text, res)
    if res[0] == 1:
        print('Прогноз: специфично')
        return True
    else:
        print('Прогноз:  не специфично')
        return False

def getA(text):
    """
    Предикт для A критерия SMART
    """
    text = analyse.prepare(text)

    res = text_clfA.predict([text])

    print(text, res)
    if res[0] == 1:
        print('Прогноз: достижимо')
        return True
    else:
        print('Прогноз: не достижимо')
        return False

def getT(text):
    """
    Предикт для T критерия SMART
    """
    text = analyse.prepare(text)

    res = text_clfT.predict([text])

    print(text, res)
    if res[0] == 1:
        print('Прогноз: ограничен во времени')
        return True
    else:
        print('Прогноз: не ограничен во времени')
        return False

def getEducation(text):
    """
    Предикт для edu критерия
    """
    text = analyse.prepare(text)

    res = text_clfEducation.predict([text])

    print(text, res)
    if res[0] == 1:
        print('Прогноз: относится к самообразованию и саморазвитию')
        return True
    else:
        print('Прогноз: не относится к самообразованию и саморазвитию')
        return False

def getUnambiguity(text):
    """
    Предикт для unambiguity критерия
    """
    text = analyse.prepare(text)

    res = text_clfUnambiguity.predict([text])

    print(text, res)
    if res[0] == 1:
        print('Прогноз: немножественность в формулировке')
        return True
    else:
        print('Прогноз: множественность в формулировке')
        return False
