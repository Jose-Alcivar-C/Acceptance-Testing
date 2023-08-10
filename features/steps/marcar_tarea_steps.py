from behave import *
from Tarea import Tarea

def estaEnLista(tarea, listaDeTareas):
    for valor in listaDeTareas:
        if(valor.getNombre() == tarea.getNombre()):
            return True
    return False


@given("la lista tiene cuatro elementos")
def step_impl(context):
    global lista
    lista = list([])
    lista.append(Tarea("correr"))
    lista.append(Tarea("comer"))
    lista.append(Tarea("saltar"))
    lista.append(Tarea("dibujar"))


@when('el usuario escogio la opcion "{opcion}"')
def step_impl(context, opcion):
    assert opcion == "3"


@when('el usuario escoge la tarea "{opcion}"')
def step_impl(context, opcion):
    assert opcion == "2"


@then('La lista ya no contiene la tarea "{numTarea}"')
def step_impl(context, numTarea):
    tarea = lista.pop(int(numTarea))
    assert estaEnLista(tarea, lista) == False, f'Tarea "{tarea}" no esta en lista de tarea pendientes'