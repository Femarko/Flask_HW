import sqlalchemy

from app.db import engine


class UnitOfWork:
    def __init__(self):
        self.session_maker = sqlalchemy.orm.sessionmaker(bind=engine)

    def __enter__(self):
        self.session = self.session_maker()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.rollback()
            self.session.close()
        self.session.close()

    def rollback(self):
        self.session.rollback()

    def commit(self):
        self.session.commit()
