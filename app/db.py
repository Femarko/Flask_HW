import sqlalchemy
from sqlalchemy.orm import sessionmaker

from app import models, config

POSTGRES_DSN = f"postgresql://{config.POSTGRES_USER}:{config.POSTGRES_PASSWORD}@{config.POSTGRES_HOST}:" \
               f"{config.POSTGRES_PORT}/{config.POSTGRES_DB}"

engine = sqlalchemy.create_engine(POSTGRES_DSN)

Session = sqlalchemy.orm.sessionmaker(bind=engine)

models.Base.metadata.create_all(bind=engine)
