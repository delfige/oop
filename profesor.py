import logging
from miembro import Miembro
class Profesor(Miembro):
    def __init__(self, nombre, apellido, puesto,materia): 
        super().__init__(nombre, apellido, puesto)
        self.__materia = materia

    @property
    def materia(self):
        return self.__materia
    @materia.setter
    def materia(self, materia):
        self.__materia = materia


    
    def __str__(self):
        a = super().__str__()
        return  '{} Especializacion : {} '.format(a,self.materia)
    
    def asistir(self):
        logging.INFO("Dar el presente en el libro de profesores")

    
    def cumplir(self):
        logging.INFO("Cumplir los determinados dias en las determinadas aulas")


    def corregir(self):
        logging.INFO("Corregir examenes")
    

    def evaluar(self):
        """Evaluar a los alumnos"""
        logging.INFO("Tomar evaluacion")

    def ausentarse(self):
        logging.info("No asistir a la institucion")


    

