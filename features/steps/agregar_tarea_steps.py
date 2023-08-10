from behave import *
from Tarea import Tarea

def estaEnLista(tarea, listaDeTareas):
    for valor in listaDeTareas:
        if(valor.getNombre() == tarea.getNombre()):
            return True
    return False


@given("la lista esta vacia")
def step_impl(context):
    global lista
    lista = []


@when('el usuario ingresa la tarea "{tarea}"')
def step_impl(context, tarea):
    lista.append(Tarea(tarea))


@then('la lista debe contener "{tarea}"')
def step_impl(context, tarea):
    assert estaEnLista(Tarea(tarea), lista), f'Tarea "{tarea}" no esta en lista de tarea pendientes'