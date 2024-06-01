from typing import Optional, override

from .abs_news import AbstractNews


class StateNews(AbstractNews):
    """
    Класс для хранения состояния новости
    """

    def __init__(self,
                 text: str,
                 id_: Optional[int] = None,
                 title: Optional[str] = None,
                 url: Optional[str] = None,
                 chapter_id: Optional[int] = None,
                 chapter_title: Optional[str] = None):
        """
        Конструктор состояния новости

        :param id_:
        :param title:
        :param text:
        :param url:
        :param chapter_id:
        :param chapter_title:
        """
        super().__init__()
        self.id = id_
        self.title = title
        self.text = text
        self.url = url
        self._chapter_id = chapter_id
        self._chapter_title = chapter_title

    @override
    def chapter_id(self) -> Optional[int]:
        """
        Возвращает идентификатор главы, в которой находится новость
        """
        return self._chapter_id

    @override
    def chapter_title(self) -> Optional[str]:
        """
        Возвращает название главы, в которой находится новость
        """
        return self._chapter_title
