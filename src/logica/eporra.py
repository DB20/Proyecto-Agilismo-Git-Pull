from ast import Return

from sqlalchemy import false, true
from src.modelo.carrera import Carrera
from src.modelo.competidor import Competidor
from src.modelo.apuesta import Apuesta
from src.modelo.apostador import Apostador
from src.modelo.declarative_base import engine, Base, session

class Eporra():
    def __init__(self):
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

    def agregar_carrera(self, nombre, competidores):
        #Se busca si hay una carrera con ese nombre
        busqueda= session.query(Carrera).filter(Carrera.nombre == nombre).all()
        #Si no hay carrera con ese nombre entonces se procede a crear la carrera y si los competidores ingresados son más de uno
        if len(busqueda)==0 and len(competidores)>0:
            #Se calcula la probabilidad total de los competidores
            suma=0
            for x in range (len(competidores)):
                suma = suma + competidores[x].probabilidad

            if suma == 1:
                carrera = Carrera(nombre=nombre, competidores = competidores)
                session.add(carrera)
                session.commit()
                return True
            else:
                return False
        else:
            return False        

    def darCarreras():
        return None

    def agregar_competidor(self, nombre,probabilidad,carreraid):
        #Se busca si hay una carrera con ese nombre
        busqueda= session.query(Competidor).filter(Competidor.nombre == nombre).all()
            #Si no hay carrera con ese nombre entonces se procede a crear la carrera y si los competidores ingresados son más de uno
        if type(probabilidad) == float or type(probabilidad) == int:
            #1 verificar que guarde competidor no creado
            if len(busqueda)==0 and nombre != None and nombre != "" and probabilidad >0 and probabilidad <1 and carreraid > 0:
                competidor= Competidor(nombre=nombre, probabilidad = probabilidad, carrera=carreraid)
                session.add(competidor)
                session.commit()
                return True
            else:
                return False
        else:
            return False


    def darCompetidores():
        return None


    def dar_lista_carreras(self):
        carreras = [elem.__dict__ for elem in session.query(Carrera).all()]
        return carreras

    def eliminar_carrera(self, carrera_id):
        try:
            carrera = session.query(Carrera).filter(Carrera.id == carrera_id).first()
            if carrera is not None:
                session.delete(carrera)
                session.commit()
                return True
            else:
                return False
        except:
            return False