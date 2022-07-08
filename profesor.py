from miembros import Miembro

class Profesor(Miembro):
    def __init__(self, name, salario, puesto,materia):
        super().__init__(name, salario, puesto)
        self.materia = materia
    
    def __str__(self):
        a = super().__str__()
        return  '{} Especializacion : {} '.format(a,self.materia)

    def aguinaldo(self):
        return super().aguinaldo()

    def rendimiento(self):
        print()
        print("El rendimiento sera checkeado por 2 o mas evaluaciones anuales")

    def aumento(self):
        print( "Tu salario aumentara cada 6 meses")
    
    def tareas(self):
         print("debe llevar a cabo 4 clases por semana")
    

test1=Profesor("delfi" , 400.000 , "Profesora" , "logica")
print(test1)
print ("tu aguinaldo sera de $" , test1.aguinaldo())
test1.rendimiento()
test1.aumento()
test1.condiciones()
test1.tareas()