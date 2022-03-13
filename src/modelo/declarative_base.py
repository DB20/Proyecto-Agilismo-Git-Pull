##from importlib.metadata import metadata
from sqlalchemy import create_engine
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData

engine = create_engine('sqlite:///aplicacion.sqlite')
Session = sessionmaker(bind=engine)

Base = declarative_base()
session = Session()

meta = MetaData()
Base.metadata.drop_all(engine)
meta.create_all(engine)