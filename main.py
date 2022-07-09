from miembro import Miembro
from profesor import Profesor
from Alumno import Alumno
import logging

logging.basicConfig(filename="logs/miPrograma.log", level=logging.INFO)

Alumno1=Alumno("delfi" , "gerea", "Estudiante" , "Libre",str(id), str(8))
print(Alumno1)
Alumno1.asistir()
Alumno1.cumplir()
       