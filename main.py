#from abs import miembros
from distutils.log import INFO
from profesor import Profesor
from admin import Admin

import logging



logging.basicConfig(filename="logs/miPrograma.log", level=INFO)

def main():
    admin = Admin('Registro')
    print(admin)


if __name__ == '__main__':
    main()