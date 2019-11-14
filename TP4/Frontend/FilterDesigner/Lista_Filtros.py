class Filtros:
    def __init__(self, indice):
        self.lista_filtros = []
        self.indice = indice
        self.seleccionado = 0
        self.label = None

    def agregar_filtro(self, filtro):
        self.lista_filtros.append(filtro)

    def borrar_filtro(self, n):
        self.lista_filtros.pop(n - 1)

    def indice_up(self):
        self.indice += 1

    def indice_down(self):
        self.indice -= 1

    def seleccionar(self, num):
        self.seleccionado = num

    def cambiar_label(self, label):
        self.label = label

    def get_label(self):
        return self.label

listaf = Filtros(0)

