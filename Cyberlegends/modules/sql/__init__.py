import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from Cyberlegends import DB_URI


def start() -> scoped_session:
engine=create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))
return scoped_session(sessionmaker(bind=engine, autoflush=False))
BASE = declarative_base()
SESSION = start()


#omk
