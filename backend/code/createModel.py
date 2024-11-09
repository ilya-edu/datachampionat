# Модуль обучения классификатора
# Автор: Денис К., Milling Team, 2020

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn import preprocessing
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score, classification_report, confusion_matrix
from sklearn import metrics
import numpy as np

import joblib

import dataPreparing
import analyse


def getPredicts(clf, listText):
    """
    Получение результатов предикта с модельки по всему набору данных
    """
    retList = [clf.predict([analyse.prepare(text)])[0] for text in listText]
    return retList

def getTestY(cr):
    """
    Получение двоичных цифровых значений по данным из таблицы
    """
    retList = []
    for c in cr:
        if cr[c][0] == 'Да' or cr[c][0] == 'Не следует из формулировки, но можно предположить':
            retList.append(1)
        else:
            retList.append(0)
    return retList

def getTestYSmart(cr):
    """
    Получение двоичных цифровых значений по данным из таблицы для критериев SMART
    """
    retList = []
    for c in cr:
        if cr[c][0] == '1':
            retList.append(1)
        else:
            retList.append(0)
    return retList

def scaleData(test, labels):
    """
    Временная функция для провередения замеров скорости работы на большом количестве данных
    (Bruh..)
    """
    nTest, nLabels = [], []
    nTest.extend(test)
    nLabels.extend(labels)
    for i in range(len(test)):
        if labels[i] == 0:
            for _ in range(10):
                nTest.append(test[i])
                nLabels.append(labels[i])
    return nTest, nLabels

def startFit():
    """
    Создание архитектуры классификатора, обучение и сбор скорингов
    """
    tr = dataPreparing.task_reader()
    cr = dataPreparing.criteria_reader()
    testY = getTestYSmart(cr)
    useFilter = dataPreparing.check(tr, cr)
    test, test_labels = dataPreparing.checkC(tr, cr, useFilter)
    test, testY = scaleData(test, testY)
    print(len(test), len(testY))
    ready_test = []
    for t in range(len(test)):
        ready_test.append(analyse.prepare(test[t]))

    text_clf = Pipeline([
                        ('vect', CountVectorizer(ngram_range=(2,4), min_df=1, analyzer='word')),
                        ('tfidf', TfidfTransformer()),
                        #  ('tfidf', TfidfVectorizer(ngram_range=(1,6), sublinear_tf=True, min_df=1, analyzer='word')),
                        ('clf', SGDClassifier(loss='perceptron', alpha=1e-3, random_state=2020, max_iter=5, n_jobs=4))
                        ])

    text_clf.fit(ready_test, testY)

    # print(f'result: {text_clf.score(ready_test, test_labels)*100}%')

    predY = getPredicts(text_clf, ready_test)

    print(classification_report(testY, predY))

    print(confusion_matrix(testY, predY))

    # joblib.dump(text_clf, 'models/clfUnambiguity.pkl', compress=1) 


if __name__ == '__main__':
    startFit()
