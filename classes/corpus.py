from collections import defaultdict
import math
from typing import List, Iterator, Iterable, Dict

import joblib
from sklearn.preprocessing import normalize
import numpy as np

from .document import Document
from .state_corpus import StateCorpus


class Corpus:
    """
    Класс для хранения информации о корпусе новостей
    """

    def __init__(self):
        """
        Конструктор корпуса новостей
        """
        self._documents: List[Document] = []
        self._lemmas: List[str] = []
        self._lemmas_freq: Dict[str, int] = defaultdict(int)

    def __len__(self) -> int:
        """
        Возвращает количество документов в корпусе

        :return: количество документов в корпусе
        """
        return len(self._documents)

    def __getitem__(self, index: int) -> Document:
        """
        Возвращает документ по индексу

        :param index: индекс документа
        :return: документ по индексу
        """
        return self._documents[index]

    def __iter__(self) -> Iterator[Document]:
        """
        Возвращает итератор по документам корпуса

        :return: итератор по документам корпуса
        """
        return iter(self._documents)

    def add_document(self, document: Document) -> None:
        """
        Добавляет документ в корпус

        :param document: документ
        """
        self._documents.append(document)
        for lemma in document.lemmas_unique:
            if lemma not in self._lemmas_freq:
                self._lemmas.append(lemma)
            self._lemmas_freq[lemma] += 1

    def add_documents(self, documents: Iterable[Document]) -> None:
        """
        Добавляет документы в корпус

        :param documents: документы
        """
        for document in documents:
            self.add_document(document)

    def filter(self, min_freq: int = 1) -> None:
        """
        Фильтрует леммы корпуса новостей по частоте встречаемости

        :param min_freq: минимальная частота встречаемости
        """
        self._lemmas = [
            lemma
            for lemma in self._lemmas
            if self._lemmas_freq[lemma] >= min_freq
        ]
        self._lemmas_freq = {
            lemma: self._lemmas_freq[lemma]
            for lemma in self._lemmas
        }
        self._documents = [
            document
            for document in self._documents
            if any(
                lemma in document.lemmas_unique
                for lemma in self._lemmas
            )
        ]

    @property
    def lemmas(self) -> List[str]:
        """
        Возвращает леммы корпуса новостей

        :return: леммы корпуса новостей
        """
        return self._lemmas

    @property
    def idf(self) -> np.ndarray:
        """
        Возвращает idf корпуса новостей

        :return: idf корпуса новостей
        """
        return np.array([
            math.log(len(self) / self._lemmas_freq[lemma])
            for lemma in self.lemmas
        ])

    def get_tf_idf(self, is_normalize: bool = True) -> np.ndarray:
        """
        Возвращает tf-idf корпуса новостей

        :param normalize: нормализовать tf-idf
        :return: tf-idf корпуса новостей
        """
        tf_idf = np.array([document.tf_idf for document in self._documents])
        if is_normalize:
            tf_idf = normalize(tf_idf, norm='l2', axis=1)
        return tf_idf

    @property
    def categories(self) -> np.ndarray:
        """
        Возвращает категории корпуса новостей

        :return: категории корпуса новостей
        """
        return np.array([document.category for document in self._documents])

    @property
    def categories_labels(self) -> np.ndarray:
        """
        Возвращает метки категорий корпуса новостей

        :return: метки категорий корпуса новостей
        """
        return np.array([document.category_label for document in self._documents])

    def _load_state(self, state: StateCorpus) -> None:
        """
        Загружает состояние корпуса новостей

        :param state: состояние корпуса новостей
        """
        self._documents = state.documents
        for document in self._documents:
            document.set_corpus(self)
        self._lemmas = state.lemmas
        self._lemmas_freq = state.lemmas_freq

    @property
    def state(self) -> StateCorpus:
        """
        Возвращает состояние корпуса новостей

        :return: состояние корпуса новостей
        """
        return StateCorpus(self)

    def save(self, filename: str) -> None:
        """
        Сохраняет корпус новостей в файл

        :param filename: имя файла
        """
        joblib.dump(self.state, filename)

    def _load(self, filename: str) -> None:
        """
        Загружает корпус новостей из файла

        :param filename: имя файла
        """
        state = joblib.load(filename)
        self._load_state(state)

    @classmethod
    def load(cls, filename: str) -> 'Corpus':
        """
        Загружает корпус новостей из файла

        :param filename: имя файла
        :return: корпус новостей
        """
        corpus = cls()
        corpus._load(filename)
        return corpus
