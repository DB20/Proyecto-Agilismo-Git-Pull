from sqlalchemy import Column, Integer, String, ForeignKey,Float
from sqlalchemy.orm import relationship

from .declarative_base import Base

class Apostador(Base):
    __tablename__ = 'apostador'

    id = Column(Integer, primary_key=True)
    nombreApostador = Column(String)
    apuestas = relationship('Apuesta')
