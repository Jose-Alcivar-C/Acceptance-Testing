from Manejador import agregarTarea, listarTareas, marcarCompletada, borrarTareas, cambiarNombreTarea

def ProgramaPrincipal():
    print("***Bienvenido al sistema***")
    print("¿Qué desea hacer?")
    while(True):
        print("1. Agregar una tarea a la lista de tareas pendientes")
        print("2. Enumerar todas las tareas en la lista de tareas pendientes")
        print("3. Marcar una tarea como completada")
        print("4. Borrar toda la lista de tareas pendientes")
        print("5. Cambiar nombre a una tarea")
        print("6. Salir")
        print("")
        
        seleccion = input("Ingrese su seleccion: ")
        print("")

        if(seleccion == "1"):
            agregarTarea()
        
        elif(seleccion == "2"):
            listarTareas()

        elif(seleccion == "3"):
            marcarCompletada()

        elif(seleccion == "4"):
            borrarTareas()

        elif(seleccion == "5"):
            cambiarNombreTarea()

        elif(seleccion == "6"):
            print("Programa finalizado")
            print("")
            break

        else:
            print("seleccion incorrecta")
            print("")

ProgramaPrincipal()
