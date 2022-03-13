from xmlrpc.client import Boolean
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from .declarative_base import Base, engine


class Carrera(Base):
    __tablename__ = 'carrera'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    abierta = Column(Boolean)
    competidores = relationship('Competidor', cascade='all, delete, delete-orphan')
    apuestas = relationship('Apuesta', cascade='all, delete, delete-orphan')
    #Base.metadata.drop_all(bind=engine)

