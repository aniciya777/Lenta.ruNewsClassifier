from typing import List

import nltk
import nltk.corpus as nltk_corpus
from pymystem3 import Mystem


class Vectorizer:
    """
    Класс для векторизации текста
    """
    _mystem = Mystem()
    nltk.download('stopwords', quiet=True)
    stopwords = set(nltk_corpus.stopwords.words())

    @staticmethod
    def __call__(text: str) -> List[str]:
        """
        Векторизация текста

        :param text: текст для векторизации
        :return: список лемм
        """
        lemmas = Vectorizer._mystem.lemmatize(text)
        lemmas = list(filter(Vectorizer._filter, lemmas))
        return lemmas

    @classmethod
    def _filter(cls, lemma: str) -> bool:
        """
        Фильтрация леммы

        :param lemma: лемма
        :return: True, если лемма является словом
        """
        return lemma.isalpha() and lemma not in cls.stopwords
