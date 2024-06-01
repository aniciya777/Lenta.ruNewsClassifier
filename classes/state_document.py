import classes
from classes.abs_news import AbstractNews
from classes.state_news import StateNews


class StateDocument:
    """
    Класс для хранения информации о документе

    Паттерн "Состояние"
    """
    def __init__(self, document: 'classes.Document'):
        """
        Конструктор состояния документа

        :param document: документ
        """
        self._lemmas = document.lemmas
        self._news_id = document._news.id
        self._news_title = document._news.title
        self._news_text = document._news.text
        self._news_url = document._news.url
        self._chapter_id = document._news.chapter_id
        self._chapter_title = document._news.chapter.name

    @property
    def lemmas(self) -> list:
        """
        Возвращает список лемм документа

        :return: список лемм документа
        """
        return self._lemmas

    @property
    def news(self) -> AbstractNews:
        """
        Возвращает новость документа

        :return: новость документа
        """
        return StateNews(
            id_=self._news_id,
            title=self._news_title,
            text=self._news_text,
            url=self._news_url,
            chapter_id=self._chapter_id,
            chapter_title=self._chapter_title,
        )
