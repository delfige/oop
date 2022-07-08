#from abs import miembros

from profesor import Profesor
from admin import Admin
from estudiante import Alumno
import logging




def main(): 
    logging.basicConfig(filename="logs/miPrograma.log", level=logging.INFO)

Alumno1=Alumno("delfi" , "gerea", "Estudiante" , "Libre",str(id), str(8))
logging.INFO(Alumno1)
       