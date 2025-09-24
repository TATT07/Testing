class Task:
    def __init__(self, task_id, title, description="", priority="media"):
        if not title.strip():
            raise ValueError("El título no puede estar vacío")
        if priority not in ["alta", "media", "baja"]:
            raise ValueError("Prioridad inválida")
        self.id = task_id
        self.title = title
        self.description = description
        self.priority = priority
        self.completed = False

    def completar(self):
        self.completed = True

    def __repr__(self):
        estado = "✔️" if self.completed else "❌"
        return f"[{self.id}] {self.title} ({self.priority}) {estado}"


class ToDoList:
    def __init__(self):
        self.tasks = {}
        self.next_id = 1

    def agregar(self, title, description="", priority="media"):
        tarea = Task(self.next_id, title, description, priority)
        self.tasks[self.next_id] = tarea
        self.next_id += 1
        return tarea

    def listar(self, prioridad=None, completadas=None):
        result = list(self.tasks.values())
        if prioridad:
            result = [t for t in result if t.priority == prioridad]
        if completadas is not None:
            result = [t for t in result if t.completed == completadas]
        return result

    def completar(self, task_id):
        if task_id not in self.tasks:
            raise KeyError("ID inexistente")
        self.tasks[task_id].completar()

    def eliminar(self, task_id):
        if task_id not in self.tasks:
            raise KeyError("ID inexistente")
        del self.tasks[task_id]
