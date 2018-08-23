import sqlalchemy
from sqlalchemy import create_engine

engine = create_engine('sqlite:///:memory:', echo=True)
print(sqlalchemy.__version__ )