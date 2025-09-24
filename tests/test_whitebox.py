from src.todo import ToDoList

def test_completar_tarea():
    todo = ToDoList()
    tarea = todo.agregar("Leer libro")
    todo.completar(tarea.id)
    assert todo.tasks[tarea.id].completed is True

def test_listar_tareas_filtradas():
    todo = ToDoList()
    todo.agregar("Estudiar", priority="alta")
    todo.agregar("Jugar", priority="baja")
    filtradas = todo.listar(prioridad="alta")
    assert all(t.priority == "alta" for t in filtradas)
