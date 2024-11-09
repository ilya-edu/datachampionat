# BlueFloyd

## Запуск

### Создание окружения

```
// Если нет модуля venv
sudo apt-get install python3-venv

python3 -m venv env
source env/bin/activate
```

### Установка модулей в окружение

```
pip3 install -r requirements.txt
```

### Запуск серверной части

> Не забыть пробросить порты наружу

```
// через screen, чтобы отвязаться от сессии
screen -S SMART python3 server.py
```

либо если просто открыть

```
python3 server.py
```



### Запуск обучалки подготовки файлов и классификаторов

#### Препарация данных

```
python3 dataPreparing.py
```

#### Создание модели

```
python3 createModel.py
```



## Структура проекта

```
.
├── analyse.py
├── createModel.py
├── data
│   ├── criteria.csv
│   └── task.csv
├── dataPreparing.py
├── models
│   ├── clfA.pkl
│   ├── clfEducation.pkl
│   ├── clfS.pkl
│   ├── clfT.pkl
│   └── clfUnambiguity.pkl
├── predictCriteria.py
├── requirements.txt
└── server.py

2 directories, 13 files
```

