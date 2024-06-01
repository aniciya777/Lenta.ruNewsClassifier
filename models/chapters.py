import sqlalchemy as sa
from sqlalchemy.orm import Session
import sqlalchemy.orm as orm

from .db_session import SqlAlchemyBase


class Chapter(SqlAlchemyBase):
    """
    Класс для хранения информации о новостных разделах
    """

    __tablename__ = 'chapters'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=False, unique=True, index=True)

    news = orm.relationship('News')

    def __str__(self) -> str:
        return self.name

    @classmethod
    def get_by_name(cls, name: str, db_session: Session) -> 'Chapter':
        """
        Возвращает раздел по его названию
        Если раздела с таким названием не существует, то он создаётся

        :param name: название раздела
        :param db_session: сессия
        :return: раздел
        """
        result = db_session.query(cls).filter(cls.name == name).first()
        if result is None:
            result = cls(name=name)
            db_session.add(result)
            db_session.commit()
        return result

    def __hash__(self) -> int:
        return self.id

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Chapter):
            return False
        return self.id == other.id
