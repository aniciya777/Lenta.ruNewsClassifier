from typing import List, Dict

import classes
from classes.state_document import StateDocument


class StateCorpus:
    """
    Класс для хранения состояния корпуса новостей

    Паттерн "Состояние"
    """

    def __init__(self, corpus: 'classes.Corpus'):
        """
        Конструктор состояния корпуса новостей

        :param corpus: корпус новостей
        """
        self._lemmas: List[str] = corpus.lemmas
        self._lemmas_freq: Dict[str, int] = corpus._lemmas_freq
        self._documents_states = [document.state for document in corpus]

    @property
    def lemmas(self) -> List[str]:
        """
        Возвращает леммы корпуса новостей

        :return: леммы корпуса новостей
        """
        return self._lemmas

    @property
    def lemmas_freq(self) -> Dict[str, int]:
        """
        Возвращает частоты лемм корпуса новостей

        :return: частоты лемм корпуса новостей
        """
        return self._lemmas_freq


    @property
    def documents(self) -> List['classes.Document']:
        """
        Возвращает документы корпуса новостей

        :return: документы корпуса новостей
        """
        return [
            classes.Document.load_state(document_state)
            for document_state in self._documents_states
        ]
