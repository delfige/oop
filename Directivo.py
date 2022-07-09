import logging
from miembro import Miembro
class Directivo(Miembro):
    def __init__(self, name, apellido, puesto,materia):
        super().__init__(name, apellido, puesto)
        self.__materia = materia

    @property            #SETTER Y GETTER
    def materia(self):
        return self.__materia

    @materia.setter
    def materia(self, materia):
        self.__materia = materia

    def __str__(self):
        a = super().__str__()
        return  '{} Materias a cargo:{} '.format(a,self.materia)
    def asistir(self):
     logging.info("Asistir a la institucion")

    
    def cumplir(self):
     logging.info("Cumplir los dias establecidos")


    def corregir(self):
     logging.info("Corregir")
    

    def evaluar(self):
        pass

    def ausentarse(self):
        logging.info("No asistir a la institucion")


