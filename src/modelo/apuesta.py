from sqlalchemy import Column, Integer, String, ForeignKey,Float
from sqlalchemy.orm import relationship

from .declarative_base import Base

class Apuesta(Base):
    __tablename__ = 'apuesta'

    id = Column(Integer, primary_key=True)
    valor = Column(Float)
    apuestas_carrera = Column(Integer, ForeignKey('carrera.id'))
    apuestas_competidor = Column(Integer, ForeignKey('competidor.id'))
    apuestas_apostador = Column(Integer, ForeignKey('apostador.id'))

