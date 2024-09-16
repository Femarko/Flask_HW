import sqlalchemy

from app import config
from app.db import db_models
from app.db.db_repository import DBRepository

POSTGRES_DSN = f"postgresql://{config.POSTGRES_USER}:{config.POSTGRES_PASSWORD}@{config.POSTGRES_HOST}:" \
               f"{config.POSTGRES_PORT}/{config.POSTGRES_DB}"

engine = sqlalchemy.create_engine(POSTGRES_DSN)

# Session = sqlalchemy.orm.sessionmaker(bind=engine)

db_models.Base.metadata.create_all(bind=engine)

# storage_interface = DBRepository(session=Session())
