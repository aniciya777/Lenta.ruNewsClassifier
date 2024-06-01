from collections import Counter
from functools import cached_property
from typing import List, Dict, Optional

import numpy as np

import classes
from .state_document import StateDocument
from classes.abs_news import AbstractNews
from classes.state_news import StateNews


class Document:
    """
    Класс для хранения информации о новостях
    """

    def __init__(self, news: AbstractNews, corpus: Optional['classes.Corpus'], lemmas: List[str]):
        self._news = news
        self._lemmas = lemmas
        self._lemmas_freq: Dict[str, int] = Counter(lemmas)
        self._corpus = corpus

    def __len__(self) -> int:
        """
        Возвращает количество лемм в новости

        :return: количество лемм в новости
        """
        return len(self._lemmas)

    def set_corpus(self, corpus: 'classes.Corpus') -> None:
        """
        Устанавливает корпус новостей

        :param corpus: корпус новостей
        """
        self._corpus = corpus

    @cached_property
    def lemmas(self) -> List[str]:
        """
        Список лемм новости

        :return: список лемм новости
        """
        return self._lemmas

    @cached_property
    def lemmas_unique(self) -> List[str]:
        """
        Список уникальных лемм новости

        :return: список уникальных лемм новости
        """
        return list(self._lemmas_freq.keys())

    def has_lemma(self, lemma: str) -> bool:
        """
        Проверяет, содержит ли новость лемму

        :param lemma: лемма
        :return: True, если новость содержит лемму, иначе False
        """
        return lemma in self._lemmas_freq

    @property
    def tf(self) -> np.ndarray:
        """
        Возвращает tf новости

        :return: tf новости
        """
        return np.array([
            self._lemmas_freq.get(lemma, 0) / len(self)
            for lemma in self._corpus.lemmas
        ])

    @property
    def tf_idf(self) -> np.ndarray:
        """
        Возвращает tf-idf новости

        :return: tf-idf новости
        """
        return self.tf * self._corpus.idf

    @property
    def category(self) -> int:
        """
        Возвращает категорию новости

        :return: категория новости
        """
        return self._news.chapter_id

    @property
    def category_label(self) -> str:
        """
        Возвращает название категории новости

        :return: название категории новости
        """
        return self._news.chapter_title

    @property
    def state(self) -> StateDocument:
        """
        Возвращает состояние новости

        :return: состояние новости
        """
        return StateDocument(self)

    @classmethod
    def load_state(cls, state: StateDocument) -> 'Document':
        """
        Восстанавливает документ из состояния

        :param state: состояние документа
        :return: документ
        """
        return cls(
            news=state.news,
            corpus=None,
            lemmas=state.lemmas
        )
