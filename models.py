from datetime import datetime

from sqlalchemy import create_engine, Integer, String, DateTime, func
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column

POSTGRES_DSN = f"postgresql://adv:secret@127.0.0.1:5431/adv"
engine = create_engine(POSTGRES_DSN)

Session = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


class UserBase(Base):

    __tablename__ = 'app_user'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)
    email: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(nullable=False)


class AdvBase(Base):

    __tablename__ = 'app_adv'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200), unique=False, index=True, nullable=False)
    description: Mapped[str] = mapped_column(index=True,nullable=False)
    creation_date: Mapped[datetime] = mapped_column(DateTime)
    owner: Mapped[str] = mapped_column(foreign_key=UserBase.id)



