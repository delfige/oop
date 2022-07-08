#from miembros import Miembros
from estudiante import Alumno
from profesor import Profesor
from datetime import date

class Admin():

    def __init__(self, tema):
        self.fecha  = date.today()
        self.tema = tema
        self.profesores = []
        self.estudiantes = []

    def agregar(self, persona):
        '''
        Agrega una persona
        '''
        if persona.__class__.__name__ == 'Profesor':
            self.profesores.append(persona)
        if persona.__class__.__name__ == 'Estudiante':
            self.estudiantes.append(persona)
        
    def __str__(self):
        '''
        Imprime lista de profesores y alumnos
        ''' 
        print(f'\nFecha: {self.fecha}\nSeccion: {self.tema}\n')
        print('Profesores:')
        for i in self.profesores:
            print(f'\n~Nombre completo:{i.name}\nSueldo:{i.salario}\n{i.puesto}\nMateria:{i.materia}')

        print('\nEstudiantes:')
        for s in self.estudiantes:
            print(f'\n~Nombre completo:{s.nombre} {s.apellido}\nMateria:{s.materia}\nConducion de cursada:{s.condicion}\nID de estudiante: {s.id}\n')
    



test1=Profesor("Delfi" , int(4000000) , "Profesora" , "Logica")
test2=Profesor("Andrea Gomez" , 5000.00 , "Profesora" , "Matematica")
sei=Admin('REGISTRO')
sei.agregar(test1)
sei.agregar(test2)
