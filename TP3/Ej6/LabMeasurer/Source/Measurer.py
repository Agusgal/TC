import visa
import logging
import time
import numpy as np
from Source import Resources
import matplotlib.pyplot as plt

OSC_RESOURC = 0
GEN_RESOURC = 1

BODE = 'B'
EXIT = 'E'
TRAN = 'T'

class Measurer():
    def __init__(self):
        self.chan1 = 1          #Primer canal de medicion
        self.chan2 = 1          #Segundo canal de medicion
        self.f = []             #Frecuencias a evaluar
        self.voltage = 0        #Tension del generador a usar
        self.frequency = 0      #Frecuencia del generador a usar
        self.openResources=[]   #Recursos abiertos
        logging.info("Creando resource manager.")
        #self.resourceManager = visa.ResourceManager('@sim') #Para simular un instrumento
        self.resourceManager = visa.ResourceManager()
        if(len(self.resourceManager.list_resources()) != 0): #Me fijo si hay instrumentos disponibles
            print("Conectarse al osciloscopio.")
            if(self.connect(OSC_RESOURC)):          #Se realiza la coneccion al osciloscopio
                pass
                print("Conectar el generador de funciones.")
                if(self.connect(GEN_RESOURC)):      #Se realiza la coneccion al generador de funciones

                    user_exit = False
                    while(not user_exit):
                        measurement = self.ask_which_measurement()
                        if(measurement == EXIT):
                            user_exit = True
                        elif(measurement == BODE):
                            self.bode()  # Se realiza la medicion de bode
                        elif(measurement == TRAN):
                            self.tran()  # Se realiza la medicion del transitorio
                else:
                    print("Error con el generador de funciones.")
            else:
                print("Error con el osciloscopio.")
        else:
            print("No hay instrumentos disponibles para realizar la conexion.")


    #Esta clase realiza la coneccion a un instrumento. El parametro resource solamente
    #indica la posicion en la que se guardara el intrumento en el array de open resources.
    def connect(self, resource):
        self.resources = self.resourceManager.list_resources()  #Se pide al resource manager que muestre los intrumentos disponibles para la conexion
        print("Lista de resources disponibles: ", self.resources)
        print("Seleccionar el resource al que se quiere conectar con un numero empezando desde 0.")
        self.conected = False
        while (not self.conected):          #Este bloque while se repite hasta que la entrada del usuario sea valida.
            self.chosenResource = input()   #La entrada debe ser numerica y no ser mayor a la cantidad de instrumentos disponibles.
            if (self.chosenResource.isnumeric()):
                if (int(self.chosenResource) < len(self.resources)):
                    logging.info("Intentando abrir el resource: ")
                    logging.info(self.resources[(int(self.chosenResource))])
                    try:
                        res = self.resourceManager.open_resource(self.resources[int(self.chosenResource)], read_termination='\n', write_termination='\n') #Se conecta al instrumento
                        if(resource == OSC_RESOURC):                        #Se asigna el instrumento a la posicion elegida
                            self.resource = Resources.Oscilloscope(res)
                        elif(resource == GEN_RESOURC):
                            self.resource = Resources.Generator(res)
                        self.openResources.append(self.resource) #Se anade el instrumento a la lista
                        self.conected = True
                        return True
                    except visa.VisaIOError:
                        logging.critical("Error con el instrumento abierto.")
                        return False
                else:
                    print("Entrada mayor a la cantidad de resources disponibles. Intentar de nuevo.")
            else:
                print("La entrada debe ser numerica. Intentar de nuevo.")


    #Esta clase se encarga de pedirle al usuario la informacion sobre como se quiere realizar el bode.
    def bode_input_gathering(self):
        start_freq = 0
        stop_freq = 0
        point_per_decade_quantity = 0

        #Se pide la frecuencia de arranque y se valida
        good_input = False
        print("Ingresar el exponente decimal de la frecuencia de arranque. Debe ser entre 1 y 7.")
        while (not good_input):
            start_freq = input()
            if (start_freq.isnumeric()):
                start_freq = float(start_freq)
                if (start_freq >= 1 and start_freq <= 7):
                    good_input = True
                else:
                    print("Intente nuevamente con una entrada numerica entre 1 y 7.")
            else:
                print("Intente nuevamente con una entrada numerica entre 1 y 7.")

        #Se pide la frecuencia final y se valida
        good_input = False
        print("Ingresar el exponente decimal de la frecuencia final. Debe ser entre 1 y 7.")
        while (not good_input):
            stop_freq = input()
            if (stop_freq.isnumeric()):
                stop_freq = float(stop_freq)
                if (stop_freq >= 1 and stop_freq <= 7):
                    if (stop_freq >= start_freq):
                        good_input = True
                    else:
                        print("La frecuencia final debe ser mayor o igual a la de arranque")
                else:
                    print("Intente nuevamente con una entrada numerica entre 1 y 7.")
            else:
                print("Intente nuevamente con una entrada numerica entre 1 y 7.")

        #Se piden la cantidad de puntos por decada y se valida
        good_input = False
        print("Cantidad de puntos por decada:")
        while (not good_input):
            point_per_decade_quantity = input()
            if (point_per_decade_quantity.isnumeric()):
                point_per_decade_quantity = float(point_per_decade_quantity)
                if (point_per_decade_quantity >= 1 and point_per_decade_quantity <= 1000):
                    good_input = True
                else:
                    print("Intente nuevamente con una entrada numerica entre 1 y 1000.")
            else:
                print("Intente nuevamente con una entrada numerica entre 1 y 1000.")

        #Se calcula la cantidad de puntos total y se realiza el array con todas las frecuencias a las que se va a medir
        if (start_freq == stop_freq):
            self.f = [10 ** start_freq]
        else:
            self.f = np.logspace(start_freq, stop_freq, point_per_decade_quantity * (stop_freq - start_freq))

        for ff in self.f:
            ff = int(ff)

        #Se pide la tension del generador y se valida
        good_input = False
        print("Ingresar tension para el generador de funciones en volts pico a pico:")
        while (not good_input):
            self.voltage = input()
            if (self.voltage.isnumeric()):
                self.voltage = float(self.voltage)
                if (self.voltage >= 0.001 and self.voltage <= 5):
                    good_input = True
                else:
                    print("Intente nuevamente con una entrada numerica entre 0.001 y 5.")
            else:
                print("Intente nuevamente con una entrada numerica entre 0.001 y 5.")

        #Se pide el primer canal a medir y se valida
        good_input = False
        print("Ingresar primer canal para medir. Ingresar 0 si se quiere seleccionar el canal MATH.")
        while (not good_input):
            self.chan1 = input()
            if (self.chan1.isnumeric()):
                self.chan1 = int(self.chan1)
                if (self.chan1 == 1 or self.chan1 == 2 or self.chan1 == 3 or self.chan1 == 4 or self.chan1 == 0):
                    good_input = True
                else:
                    print("Intente nuevamente con una entrada numerica entre 0 y 5.")
            else:
                print("Intente nuevamente con una entrada numerica entre 0 y 5.")

        #Se pide el segundo canal para medir y se valida
        good_input = False
        print("Ingresar segundo canal para medir. Ingresar 0 si se quiere seleccionar el canal MATH.")
        while (not good_input):
            self.chan2 = input()
            if (self.chan2.isnumeric()):
                self.chan2 = int(self.chan2)
                if (self.chan2 == 1 or self.chan2 == 2 or self.chan2 == 3 or self.chan2 == 4 or self.chan2 == 0 and self.chan2 != self.chan1):
                    good_input = True
                else:
                    print("Intente nuevamente con una entrada numerica entre 0 y 5 y que sea distinta del primer canal.")
            else:
                print("Intente nuevamente con una entrada numerica entre 0 y 5 y que sea distinta del primer canal.")

    #Esta clase es el algoritmo que setea al generador y osciloscopio en las configuraciones necesarias para cada punto en el que se va a medir
    def bode(self):
        self.oscilloscope = self.openResources[OSC_RESOURC]
        self.generator = self.openResources[GEN_RESOURC]

        self.bode_input_gathering() #Se pide informacion sobre como se quiere realizar el bode

        self.oscilloscope.set_bode_meas(self.chan1, self.chan2) #Se configura al osciloscopio para realizar un bode, mediciones de ratio, phase, etc.
        self.generator.set_voltage(self.voltage) #Se configura al generador con la tension elegida

        self.ratio=[]
        self.phase=[]

        #Algoritmo que se corre para cada punto en el que se va a querer medir.
        for ff in (self.f):
            self.generator.set_frequency(ff)                        #Se setea la frecuencia en el generador
            self.oscilloscope.tim_div(Resources.SET, 1/ff)           #Se setea la frecuencia del osciloscopio
            good_chan_div=False
            div_start = 0.001

            while(not good_chan_div):                               #Este bloque while setea la division del rango en lo minimo posible
                for i in [1, 2, 5]:                                                             #Las divisiones se prueban por decada, en 1, 2 y 5.
                    self.oscilloscope.chan_div(Resources.SET, self.chan1, div_start*i)           #Se setea la division
                    #time.sleep(0.5)
                    if(self.oscilloscope.is_clipping(self.chan1)):                              #Si esta clippeando
                        pass                                                                    #No hace nada, se multiplicara div_start por otra decada si ya sale del for
                    else:                                                                       #Si no esta clippeando
                        good_chan_div = True                                                    #Saldra del while
                        break                                                                   #Y sale del for
                div_start *= 10                 #Si esta clippeando la senal y la division por 1, 2 o 5 clippean igual, se avanza a la siguiente decada


            good_chan_div = False
            div_start = 0.001
            while (not good_chan_div):  # Este bloque while setea la division del rango en lo minimo posible
                for i in [1, 2, 5]:  # Las divisiones se prueban por decada, en 1, 2 y 5.
                    self.oscilloscope.chan_div(Resources.SET, self.chan2, div_start * i)  # Se setea la division
                    #time.sleep(0.5)
                    if (self.oscilloscope.is_clipping(self.chan2)):  # Si esta clippeando
                        pass # No hace nada, se multiplicara div_start por otra decada si ya sale del for
                    else:  # Si no esta clippeando
                        good_chan_div = True  # Saldra del while
                        break  # Y sale del for
                div_start *= 10  # Si esta clippeando la senal y la division por 1, 2 o 5 clippean igual, se avanza a la siguiente decada

            med=self.oscilloscope.measure_stats()  #Se le pide al osciloscopio las mediciones
            med = med.split(',')
            self.ratio.append(med[0])
            self.phase.append(med[1])
            print("Ratio:",med[0])
            print("Phase:", med[1])
        #plt.plot(self.f, self.ratio)
        #plt.plot(self.f, self.phase)

        #plt.show()


    def tran(self):
        self.oscilloscope = self.openResources[OSC_RESOURC]
        self.generator = self.openResources[GEN_RESOURC]

        self.tran_input_gathering()  # Se pide informacion sobre como se quiere realizar el bode

        self.generator.set_voltage(self.voltage)  # Se configura al generador con la tension elegida
        self.generator.set_frequency(self.frequency)



    def ask_which_measurement(self):
        print("Elegir que se quiere hacer: [E]xit, [B]ode o [T]ransitorio.")
        bad_input = True
        while(bad_input):
            inp = input()
            if(inp == 'E'):
                return EXIT
            elif(inp == 'B'):
                return BODE
            elif(inp == 'T'):
                return TRAN
            else:
                print("Ingresar nuevamente una entrada alfabetica igual a E, B o T.")

    def tran_input_gathering(self):

        good_input = False
        print("Ingresar la tension a la que se desea el generador de funciones.")
        while (not good_input):
            self.voltage = input()
            if (self.voltage.isnumeric()):
                self.voltage = float(self.voltage)
                if (self.voltage >= 0.001 and self.voltage <= 5):
                    good_input = True
                else:
                    print("Intente nuevamente con una entrada numerica entre 0.001 y 5.")
            else:
                print("Intente nuevamente con una entrada numerica entre 0.001 y 5.")

        good_input = False
        print("Ingresar la tension a la que se desea el generador de funciones.")
        while (not good_input):
            self.frequency = input()
            if (self.frequency.isnumeric()):
                self.frequency = float(self.frequency)
                if (self.frequency >= 10 and self.frequency <= 15*10**6):
                    good_input = True
                else:
                    print("Intente nuevamente con una entrada numerica entre 10 y 15 000 000")
            else:
                print("Intente nuevamente con una entrada numerica entre 0.001 y 15 000 000.")

                # Se pide el primer canal a medir y se valida
                good_input = False
                print("Ingresar primer canal para medir. Ingresar 0 si se quiere seleccionar el canal MATH.")
                while (not good_input):
                    self.chan1 = input()
                    if (self.chan1.isnumeric()):
                        self.chan1 = int(self.chan1)
                        if (
                                self.chan1 == 1 or self.chan1 == 2 or self.chan1 == 3 or self.chan1 == 4 or self.chan1 == 0):
                            good_input = True
                        else:
                            print("Intente nuevamente con una entrada numerica entre 0 y 5.")
                    else:
                        print("Intente nuevamente con una entrada numerica entre 0 y 5.")

                # Se pide el segundo canal para medir y se valida
                good_input = False
                print("Ingresar segundo canal para medir. Ingresar 0 si se quiere seleccionar el canal MATH.")
                while (not good_input):
                    self.chan2 = input()
                    if (self.chan2.isnumeric()):
                        self.chan2 = int(self.chan2)
                        if (
                                self.chan2 == 1 or self.chan2 == 2 or self.chan2 == 3 or self.chan2 == 4 or self.chan2 == 0 and self.chan2 != self.chan1):
                            good_input = True
                        else:
                            print(
                                "Intente nuevamente con una entrada numerica entre 0 y 5 y que sea distinta del primer canal.")
                    else:
                        print(
                            "Intente nuevamente con una entrada numerica entre 0 y 5 y que sea distinta del primer canal.")