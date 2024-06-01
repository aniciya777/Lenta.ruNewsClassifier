from typing import override

import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Mapped

from .db_session import SqlAlchemyBase
from models import chapters
from classes.abs_news import AbstractNews


class News(AbstractNews, SqlAlchemyBase):
    """
    Класс для хранения информации о новостях
    """

    __tablename__ = 'news'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    url = sa.Column(sa.String, nullable=False, unique=True, index=True)
    title = sa.Column(sa.String, nullable=True, default="")
    text = sa.Column(sa.String, nullable=True, default="")
    _chapter_id = sa.Column('chapter_id', sa.Integer, sa.ForeignKey("chapters.id"), nullable=False)

    chapter: Mapped[chapters.Chapter] = orm.relationship('Chapter', back_populates='news')

    def __str__(self) -> str:
        return self.title

    @property
    @override
    def chapter_title(self) -> str:
        return self.chapter.name
