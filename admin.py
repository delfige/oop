#from miembros import Miembros
from estudiante import Estudiante
from profesor import Profesor
from datetime import date

class Admin():
    def __init__(self,fecha,tema,profesores , estudiantes):
        self.fecha  = date.today()
        self.tema = tema
        self.profesores = profesores
        self.estudiantes = estudiantes

    def agregar(self, persona):
        if persona.__class__.__name__ == 'Profesor':
            self.profesores.append(persona)
        if persona.__class__.__name__ == 'Estudiante':
            self.estudiantes.append(persona)
        
    def detalle(self):
        print(f'Fecha: {self.fecha}\n tema: {self.tema}\n')
        print('Profesores:')
        for i in self.profesores:
            print(f'\n{i.name}\n{i.salario}\n{i.puesto}\n{i.materia}')

        print('\nEstudiantes:')
        for s in self.estudiantes:
            print(f'\n{s.nombre}\n{s.apellido}\n{s.materia}\n{s.condicion}\n{s.id}\n')
    


b = Estudiante("brand" , "nike " ,"oop" , "libre" , id)
test1=Profesor("delfi" , 400.000 , "Profesora" , "logica")
test2=Profesor("delfi" , 500.000 , "Profesora" , "mat")
sei=Admin('12/12/19','REGISTRO',[],[])
sei.agregar(test1)
sei.agregar(test2)
sei.agregar(b)
sei.detalle()