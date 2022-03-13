
import unittest

from sqlalchemy import true
from src.modelo.carrera import Carrera
from src.modelo.competidor import Competidor
from src.modelo.declarative_base import Session
from src.logica.eporra import Eporra

class CarreraTestCase(unittest.TestCase):

    def setUp(self):
        self.session = Session()
        self.eporra = Eporra()
        self.competidor1 = Competidor(nombre = 'jose',probabilidad=0.5 )
        self.session.add(self.competidor1)
        self.session.commit()

    def tearDown(self):
        '''Abre la sesión'''
        self.session = Session()

        '''Consulta todos los competidores'''
        busqueda = self.session.query(Competidor).all()

        '''Borra todas las carreras'''
        for competidor in busqueda:
            self.session.delete(competidor)

        self.session.commit()
        self.session.close() 
        
   
    def test_agregar_competidor(self):
        resultado = self.eporra.agregar_competidor(nombre='David', probabilidad=0.5, carreraid= 1)
        self.assertEqual(resultado, True)
    
    def test_agregar_competidor_asociado_carrera(self):
        #No Se crea competidor que no esté asociado a una carrera
        resultado = self.eporra.agregar_competidor(nombre='David', probabilidad=1, carreraid= 0)
        self.assertEqual(resultado, False)
        #Se crea si tiene una carrera asociada
        resultado2 = self.eporra.agregar_competidor(nombre='David', probabilidad=0.5, carreraid= 1)
        self.assertEqual(resultado2, True)

    def test_agregar_competidor_sin_nombre(self):
        #1 revisar que no se crea competidor sin nombre
        resultado = self.eporra.agregar_competidor(nombre='', probabilidad=0.5, carreraid= 1)

        self.assertEqual(resultado, False)
    
    def test_agregar_competidor_proba_menor(self):
        #1 revisar que se crea competidor con nombre
        resultado = self.eporra.agregar_competidor(nombre='David', probabilidad=-0.2, carreraid= 1)
        #consulta1 = self.session.query(Competidor).filter(Competidor.nombre == "David").first()
        self.assertEqual(resultado, False)
    
    def test_agregar_competidor_mayor_proba(self):
        #No se crea competidor proba mayor a 1
        resultado = self.eporra.agregar_competidor(nombre='David', probabilidad=1.2, carreraid= 1)
        self.assertEqual(resultado, False)
        
    def test_agregar_competidor_sin_proba(self):
        #No se crea competidor sin probabilidad
        resultado = self.eporra.agregar_competidor(nombre='David', probabilidad="", carreraid= 1)
        self.assertEqual(resultado, False)
    
    def test_agregar_competidor_proba1(self):
        #No Se crea competidor con proba de 1, no tendría sentido un solo competidor
        resultado = self.eporra.agregar_competidor(nombre='David', probabilidad=1, carreraid= 1)
        self.assertEqual(resultado, False)
