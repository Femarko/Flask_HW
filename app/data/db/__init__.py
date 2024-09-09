import sqlalchemy

from app import config
from app.data.db import db_models
from app.data.db.db_interface import StorageInterface

POSTGRES_DSN = f"postgresql://{config.POSTGRES_USER}:{config.POSTGRES_PASSWORD}@{config.POSTGRES_HOST}:" \
               f"{config.POSTGRES_PORT}/{config.POSTGRES_DB}"

engine = sqlalchemy.create_engine(POSTGRES_DSN)

Session = sqlalchemy.orm.sessionmaker(bind=engine)

db_models.Base.metadata.create_all(bind=engine)

storage_interface = StorageInterface(session=Session())
