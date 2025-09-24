import pytest
from src.todo import ToDoList

def test_agregar_tarea_valida():
    todo = ToDoList()
    tarea = todo.agregar("Comprar pan", priority="alta")
    assert tarea.title == "Comprar pan"

def test_agregar_sin_titulo():
    todo = ToDoList()
    with pytest.raises(ValueError):
        todo.agregar("")

def test_prioridad_invalida():
    todo = ToDoList()
    with pytest.raises(ValueError):
        todo.agregar("Estudiar", priority="urgente")

def test_eliminar_id_inexistente():
    todo = ToDoList()
    with pytest.raises(KeyError):
        todo.eliminar(99)
