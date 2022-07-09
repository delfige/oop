
import random
from miembro import Miembro
import logging


class Alumno(Miembro):
    def __init__(self, nombre, apellido, puesto,condicion,id,nota):
       super().__init__(nombre, apellido, puesto)
       self.__condicion = condicion
       self.__id = str(random.randint (0,2000))
       self.__nota = str(nota)

    @property            #SETTER Y GETTER
    def condicion(self):
        return self.__condicion

    @condicion.setter
    def condicion(self, condicion):
        self.__condicion = condicion


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id


    @property
    def nota(self):
        return self.__nota
    
    @nota.setter
    def nota(self, nota):
        self.__nota = nota 
    

    def aprobar(self,nota):
        """metodo para saber si el alumno aprobo o no"""
        if self.__nota > 7:
            return f'Aprobo su nota es {self.__nota}'
        else:
            return f'No aprobo su nota es {self.__nota}'
    
    def asistir(self):
        logging.info("Asistir al aula y dar el presente")

    
    def cumplir(self):
        logging.info("Cumplir de lunes a viernes de 18:00 a 22:00")


    def corregir(self):
        logging.info("Corregir tarea")
    

    def evaluar(self):
        logging.info("La evalucion sera el viernes")

    def ausentarse(self):
        logging.info("No asistir a la institucion")

    def __str__(self):
        a=super().__str__()
        return '{} Condicion:{} \nID de estudiante:{}\nNota:{} '.format(a,self.condicion,self.id,self.nota)
