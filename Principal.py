from Manejador import agregarTarea, listarTareas, marcarCompletada, borrarTareas

def ProgramaPrincipal():
    print("***Bienvenido al sistema***")
    print("¿Qué desea hacer?")
    while(True):
        print("1. Agregar una tarea a la lista de tareas pendientes")
        print("2. Enumerar todas las tareas en la lista de tareas pendientes")
        print("3. Marcar una tarea como completada")
        print("4. Borrar toda la lista de tareas pendientes")
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

        else:
            print("seleccion incorrecta")
            print("")

ProgramaPrincipal()
