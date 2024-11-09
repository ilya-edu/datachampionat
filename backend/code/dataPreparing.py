# Модуль подготовки данных из CSV к обработке и отправке на вход классификатору
# Автор: Денис К., Milling Team, 2020

from random import randint, seed
seed(42)

task_path = 'data/task.csv'
criteria_path = 'data/criteria.csv'

def check(data, criteria):
    """
    Проверка строк, совпадающих в обеих таблицах
    """
    temp = []
    for d in data:
        if d in criteria:
            temp.append(d)
    return temp


def checkC(tasks, criterias, useFilter):
    """
    Сортировка и однозначное соответствие элементов входа и выхода
    """
    sortUseTasks = sorted(useFilter)
    sortTasks = []
    sortCrit = []
    for task in sortUseTasks:
        sortTasks.append(tasks[task][0])
        sortCrit.append(criterias[task][0]) # magic!
    return sortTasks, sortCrit

def getUsefulValFromDict(dataDict, dataFilter):
    """
    Извлечение значений из словаря по фильтру
    """
    temp = []
    for k in dataDict:
        if k in dataFilter:
            temp.append(dataDict[k][0]) # magic!
    return temp

def getVal(csvDict):
    """
    Получение значений из словаря
    """
    return list(csvDict.values())

def task_reader():
    """
    Чтение 'task.csv'
    """
    csvTasks = {}
    with open(task_path, "r") as reader:
        lines = reader.readlines()
        for x, line in enumerate(lines):
            if x == 0: continue
            tmp = line.split(';')
            if tmp[0] == '0': continue
            csvTasks[tmp[0]] = [tmp[1]]
            # print(tmp[0],'=', csvTasks[tmp[0]])
    # print(len(csvTasks))
    return csvTasks

def criteria_reader():
    """
    Чтение 'criteria.csv'
    """
    csvCriteria = {}
    with open(criteria_path, "r") as reader:
        lines = reader.readlines()
        for x, line in enumerate(lines):
            if x == 0: continue
            tmp = line.split(';')
            if tmp[3] == '0': continue
            if tmp[3] in csvCriteria:
                # csvCriteria[tmp[3]].append(tmp[7])
                continue
            else:
                # csvCriteria[tmp[3]] = [tmp[5], tmp[6], tmp[7]]
                csvCriteria[tmp[3]] = [tmp[9]]
    return csvCriteria
