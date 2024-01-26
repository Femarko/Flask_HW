from datetime import datetime
from typing import List
from config import postgres_dsn

from sqlalchemy import create_engine, Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column, relationship

POSTGRES_DSN = postgres_dsn
engine = create_engine(POSTGRES_DSN, echo=True)

Session = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


class Adv(Base):

    __tablename__ = 'adv'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200), unique=False, index=True, nullable=False)
    description: Mapped[str] = mapped_column(index=True, unique=False, nullable=False)
    creation_date: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    author: Mapped[str] = mapped_column(String(200))

# Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

