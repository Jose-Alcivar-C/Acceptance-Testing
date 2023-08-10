from behave import *
from Tarea import Tarea


@given("la lista tiene cinco elementos")
def step_impl(context):
    global lista 
    lista = list([])
    lista.append(Tarea("comer"))
    lista.append(Tarea("estudiar"))
    lista.append(Tarea("viajar"))
    lista.append(Tarea("editar"))
    lista.append(Tarea("pasear"))

@when('el usuario selecciona la opcion "{opcion}"')
def  step_impl(context, opcion):
    assert opcion == "5"


@when('el usuario elige la tarea "{opcion}"')
def  step_impl(context, opcion):
    assert opcion == "2"


@when('el usuario ingresa el nombre "{nombre}"')
def  step_impl(context, nombre):
    assert nombre == "programar"

@then('la tarea en "{opcion}" tiene el nombre "{nombre}"')
def step_impl(context, opcion, nombre):
    lista[int(opcion)-1].setNombre(nombre)
    #assert lista[opcion-1] == nombre, f'Tarea en"{opcion}" no cambio'