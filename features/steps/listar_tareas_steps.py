from behave import *
from Tarea import Tarea


@given("la lista tiene al menos un elemento")
def step_impl(context):
    global lista 
    lista = list([])
    lista.append(Tarea("comer"))
    lista.append(Tarea("estudiar"))


@when('el usuario escoge la opcion "{opcion}"')
def  step_impl(context, opcion):
    assert opcion == "2"


@then('el tamanio de la lista es mayor a cero')
def step_impl(context):
    assert len(lista)>0