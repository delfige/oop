import random

class Estudiante:
    def __init__(self,nombre,apellido,materia,condicion,id):
        self.nombre = nombre
        self.apellido = apellido
        self.materia = materia
        self.condicion = condicion
        self.id = random.randint (0,2000)
    
   
    def __str__(self):
        return 'Nombre: {} apellido: {}  materia: {} estado: {} id: {} '.format(self.nombre, self.apellido, self.materia ,self.condicion,self.id)

b = Estudiante("brand" , "nike " ,"oop" , "libre" , id)
print(b)