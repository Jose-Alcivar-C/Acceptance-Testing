from behave import *
from Tarea import Tarea


@given("la lista tiene uno o mas elementos")
def step_impl(context):
    global lista 
    lista = list([])
    lista.append(Tarea("comer"))
    lista.append(Tarea("estudiar"))


@when('el usuario elige la opcion "{opcion}"')
def  step_impl(context, opcion):
    assert opcion == "4"


@then('el tamanio de la lista es cero')
def step_impl(context):
    lista.clear()
    assert len(lista)==0