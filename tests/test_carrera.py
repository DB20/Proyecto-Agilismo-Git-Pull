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

        '''Consulta todas las carreras'''
        busqueda = self.session.query(Carrera).all()

        '''Borra todas las carreras'''
        for carrera in busqueda:
            self.session.delete(carrera)

        self.session.commit()
        self.session.close() 
   
        
        #Se crea la carrera sin competidores, debe arrojar error pues no permite sin competidores
    def test_agregar_carrera(self):
        resultado = self.eporra.agregar_carrera(nombre='F5',competidores=[])
        self.assertEqual(resultado, False)
    
    #Se prueba la carrera con la creación de un competidor
    def test_agregar_carrera_competidores(self):
        competid1 = self.competidor1 = Competidor(nombre = 'jose',probabilidad=1 )
        compet = [competid1]
        resultado = self.eporra.agregar_carrera(nombre='F2',competidores=compet)

        consulta1 = self.session.query(Carrera).filter(Carrera.nombre == "F2").first()

        self.assertEqual(len(consulta1.competidores), 1)
        self.assertEqual(resultado, True)
     #Se crea carrera con más de un competidor
    def test_agregar_carrera_competid_2 (self):
        competid1 = self.competidor1 = Competidor(nombre = 'jose',probabilidad=0.5 )
        competid2 = self.competidor1 = Competidor(nombre = 'david',probabilidad=0.5 )
        compet = [competid1,competid2]
        resultado = self.eporra.agregar_carrera(nombre='F2',competidores=compet)

        consulta1 = self.session.query(Carrera).filter(Carrera.nombre == "F2").first()

        self.assertEqual(len(consulta1.competidores), 2)
        self.assertEqual(resultado, True)

    #Se valida que se guarde la carrera si el valor da 1
    def test_agregar_carrera_competid_Probabilidad_mal (self):
        competid1 = self.competidor1 = Competidor(nombre = 'jose',probabilidad=0.5 )
        competid2 = self.competidor1 = Competidor(nombre = 'david',probabilidad=0.8 )
        compet = [competid1,competid2]
        resultado = self.eporra.agregar_carrera(nombre='F2',competidores=compet)

        consulta1 = self.session.query(Carrera).filter(Carrera.nombre == "F2").first()

        self.assertEqual(resultado, False) 

             #Comprobar nombre no repetidor
    def test_agregar_carrera_mismo_nombre (self):
        competid1 = self.competidor1 = Competidor(nombre = 'jose',probabilidad=1 )
        competid2 = self.competidor1 = Competidor(nombre = 'david',probabilidad=1 )
        compet = [competid1]
        compet2 = [competid2]
        resultado = self.eporra.agregar_carrera(nombre='F3',competidores=compet)
        result2 = self.eporra.agregar_carrera(nombre='F3',competidores=compet2)
        self.assertEqual(resultado, True)
        self.assertEqual(result2 , False )

        #Método ver lista de carreras
    def test_lista_carreras (self):
        competid1 = self.competidor1 = Competidor(nombre = 'jose',probabilidad=0.5 )
        competid2 = self.competidor1 = Competidor(nombre = 'david',probabilidad=0.5 )
        competid3 = self.competidor1 = Competidor(nombre = 'jose',probabilidad=0.5 )
        competid4 = self.competidor1 = Competidor(nombre = 'david',probabilidad=0.5 )
        compet = [competid1,competid2]
        compet2 = [competid3,competid4]
        
        carrera1 = self.eporra.agregar_carrera(nombre="Ca1", competidores=compet)
        carrera2 = self.eporra.agregar_carrera(nombre="Ca2", competidores=compet2)

        carreras = self.eporra.dar_lista_carreras()
        self.assertEqual(len(carreras),2)

    def test_eliminar_carrera (self):
        return False
    
    
        
    

    
              
        