from src.todo import ToDoList

def test_estado_despues_de_eliminar():
    todo = ToDoList()
    tarea = todo.agregar("Viajar")
    todo.eliminar(tarea.id)
    assert tarea.id not in todo.tasks

def test_contador_incremento():
    todo = ToDoList()
    t1 = todo.agregar("A")
    t2 = todo.agregar("B")
    assert t2.id == t1.id + 1
