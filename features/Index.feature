Feature: Lista de tareas pendientes
    Scenario: agregar tarea a la lista
        Given la lista esta vacia
        When el usuario ingresa la tarea "estudiar"
        Then la lista debe contener "estudiar"
    
    Scenario: listar tareas de la lista
        Given la lista tiene al menos un elemento
        When el usuario escoge la opcion "2"
        Then el tamanio de la lista es mayor a cero

    Scenario: marcar una tarea como completada
        Given la lista tiene cuatro elementos
        When el usuario escogio la opcion "3"
        When el usuario escoge la tarea "2"
        Then La lista ya no contiene la tarea "2"

    Scenario: borrar toda la lista
        Given la lista tiene uno o mas elementos
        When el usuario elige la opcion "4"
        Then el tamanio de la lista es cero

    Scenario: cambiar nombre de una tarea
        Given la lista tiene cinco elementos
        When el usuario selecciona la opcion "5"
        When el usuario elige la tarea "2"
        When el usuario ingresa el nombre "programar"
        Then la tarea en "2" tiene el nombre "programar"
