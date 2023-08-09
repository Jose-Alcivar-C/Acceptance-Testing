from Tarea import Tarea

listaDeTareas = []

def agregarTarea():
    nombre = input("Ingrese nombre de su tarea")
    tarea = Tarea(nombre)

    listaDeTareas.append(tarea)


def listarTareas():
      
    if(len(listaDeTareas) > 0):
        print("| Nombre de Tarea | Estado |")

        for i in range(0, len(listaDeTareas)):
            print(f"{i+1}. | {listaDeTareas[i].getNombre()} | {listaDeTareas[i].getEstado()} |")
        print()

    else:
        print("No existen tareas pendientes guardadas")
        print()


def marcarCompletada():
    print("funcion1")


def borrarTareas():
    print("funcion4")