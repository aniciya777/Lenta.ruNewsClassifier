from functools import cached_property


class AbstractNews:
    """
    Абстрактный класс для хранения информации о новости
    """
    __slots__ = ('id', 'url', 'title', 'text', '_chapter_id', 'chapter')

    @cached_property
    def full_text(self) -> str:
        return self.title + " " + self.text

    @property
    def chapter_title(self) -> str:
        raise NotImplementedError

    @property
    def chapter_id(self) -> int:
        return self._chapter_id
