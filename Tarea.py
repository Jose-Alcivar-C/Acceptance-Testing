class Tarea:

    def __init__(self, nombre):
        self.nombre = nombre
        self.estado = "incompleto"

    def getNombre(self):
        return self.nombre
    
    def getEstado(self):
        return self.estado

    def setNombre(self, nombre):
        self.nombre = nombre

    def setEstado(self, estado):
        self.estado = estado

    def mostrarTarea(self):
        return f'nombre: {self.nombre}, estado: {self.estado}'
    