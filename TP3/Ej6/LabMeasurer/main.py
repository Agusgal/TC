import logging
from Source import Measurer

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)     #Se configura el nivel de informacion dado por el programa
    logging.info("Iniciando programa..")
    measurer = Measurer.Measurer()              #Se instancia la clase suprema1
