from datetime import date

from sqlalchemy import ForeignKey, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from config import DB_HOST, DB_PORT, DB_USER, DB_PASS, DB_NAME

url = f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
engine = create_engine(url, echo=True)  # echo=True
Session = sessionmaker(engine)
session = Session()


class Base(DeclarativeBase):
    pass


class DocumentsORM(Base):
    __tablename__ = 'documents'

    id: Mapped[int] = mapped_column(primary_key=True)
    psth: Mapped[str]
    date: Mapped[date]


class Documents_textORM(Base):
    __tablename__ = 'documents_text'

    id: Mapped[int] = mapped_column(primary_key=True)
    id_doc: Mapped[int] = mapped_column(ForeignKey('documents.id', ondelete='CASCADE'))
    text: Mapped[str]


def create_table():
    with session.begin():
        Base.metadata.drop_all(engine)
    # with session.begin():
    #     Base.metadata.create_all(engine)


# create_table()
