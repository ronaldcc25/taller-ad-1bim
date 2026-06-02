from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

POSTGRES_URL = "postgresql+psycopg2://user:password@localhost:5434/universidad"
MARIADB_URL = "mysql+pymysql://root:rootpassword@localhost:3308/universidad"

DATABASE_URL = MARIADB_URL


def get_engine(url=DATABASE_URL, echo=False):
    return create_engine(url, echo=echo, future=True)


def get_session_maker(url=DATABASE_URL, echo=False):
    engine = get_engine(url=url, echo=echo)
    return sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)


engine = get_engine()
SessionLocal = get_session_maker()
