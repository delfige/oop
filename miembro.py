from abc import ABC ,abstractmethod
import logging


class Miembro(ABC):
    def __init__(self, nombre, apellido ,puesto):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__puesto = puesto 


    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def quote(self, nombre):
        self.__nombre = nombre

    @property
    def apellido(self):
        return self.__apellido
    @apellido.setter
    def apellido(self, apellido):
        self.__apellido = apellido
    
    @property
    def puesto(self):
        return self.__puesto
    
    @puesto.setter
    def apellido(self, puesto):
        self.__puesto = puesto



    @abstractmethod
    def asistir(self):
        """Define si asistir"""
        pass

    @abstractmethod
    def cumplir(self):
        """Dias a cumplir en la institucion"""
        pass

    @abstractmethod
    def corregir(self):
        """Corregir determinad actividad"""
        pass
    
    
    @abstractmethod
    def ausentarse(self):
        """Funcion de ausentarse"""
        pass

    @abstractmethod
    def __str__(self) :
        return  'Nombre:{} Apellido:{}  Puesto:{}'.format(self.nombre, self.apellido, self.puesto)




