# Модуль подготовки данных и их анализа для передачи классификатору, а также при получении с фронта
# Автор: Денис К., Milling Team, 2020

from natasha import (
    Segmenter,
    MorphVocab,
    
    NewsEmbedding,
    NewsMorphTagger,
    Doc
)
import nltk
import string

# !! Если до этого не устанавливались сеты из nltk
# !! Можно запустить просто nltk_install.py
# nltk.download('punkt')

from nltk.corpus import stopwords

import pymorphy2


# Инициализация токенизатора и т.п.
segmenter = Segmenter()
morph_vocab = MorphVocab()

emb = NewsEmbedding()
morph_tagger = NewsMorphTagger(emb)

morph = pymorphy2.MorphAnalyzer()


def normalise(doc):
    """
    Получаем леммы токенов
    """
    return [_.lemma for _ in doc.tokens]

def deleteStopWords(tokens):
    """
    Редьюсим стопворды, плюс делаем их расширение
    """
    stop_words = stopwords.words('russian')
    stop_words.extend(['что', 'это', 'так', 'вот', 'быть', 'как', 'в', '—', 'к', 'на', ',',
    'я', 'а', 'да', 'но', 'тебе', 'мне', 'ты', 'и', 'у', 'на', 'ща', 'ага', ' ', '`', 'кек',
    'так', 'там', 'какие', 'который', 'какая', 'туда', 'давай', 'короче', 'кажется', 'вообще',
    'ну', 'не', 'чет', 'неа', 'свои', 'наше', 'хотя', 'такое', 'например', 'кароч', 'как-то',
    'нам', 'хм', 'всем', 'нет', 'да', 'оно', 'своем', 'про', 'вы', 'м', 'тд',
    'вся', 'кто-то', 'что-то', 'вам', 'это', 'эта', 'эти', 'этот', 'прям', 'либо', 'как', 'мы',
    'просто', 'блин', 'очень', 'самые', 'твоем', 'ваша', 'кстати', 'вроде', 'типа', 'пока', 'ок'])
    tokens = [i for i in tokens if ( i not in stop_words )]

    return tokens

# Подсчитает слова
def wordCount(cleanTokens):
    """
    Смотрим длину токенов внутри дока (таска)
    """
    return {word: cleanTokens.count(word) for word in set(cleanTokens)}

def concat(tokens):
    """
    Обычная конкатенация токенов через спейс
    """
    return ' '.join(i for i in tokens)

def prepare(text: str):
    """
    Процедура препарации и подготовки таска к обработке или передачи в обучалку
    """
    text = text.lower()
    doc = Doc(text)
    doc.segment(segmenter)
    doc.tag_morph(morph_tagger)
    for token in doc.tokens:
        token.lemmatize(morph_vocab)
    tokens = normalise(doc)
    tokens = deleteStopWords(tokens)

    return concat(tokens)
