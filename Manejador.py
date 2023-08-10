from Tarea import Tarea

listaDeTareas = list([])

def agregarTarea():
    nombre = input("Ingrese nombre de su tarea: ")
    print("")
    print("Tarea agregada exitosamente")
    print("")
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
    eleccion = input("Ingrese numero de tarea que desea marcar como completada: ")
    print("")

    try:
        valor = int(eleccion)
        if( (valor > 0) and (valor <= len(listaDeTareas) ) ):
            listaDeTareas.pop(valor-1)
            print("Tarea marcada exitosamente exitosamente")
            print("")

        else:
            print("Numero de tarea no valido.")
            print("")

    except:
        print("Debe ingresar un numero")
        print("")


def borrarTareas():
    listaDeTareas.clear()
    print("Tareas borradas exitosamente")
    print("")


def cambiarNombreTarea():
    numero = input("Ingrese numero de tarea a cambiar: ")
    
    try:
        numero = int(numero)
    except:
        print("")
        print("Debe ingresar un numero")
        print("")
        return
    
    if( (numero > 0) and (numero <= len(listaDeTareas) ) ):
        nombre = input("Ingrese nuevo nombre: ")
        print("")
        listaDeTareas[numero-1].setNombre(nombre)
        print("Nombre cambiado exitosamente")
        print("")
    
    else:
        print("")
        print("Numero de tarea no valido")
        print("")

