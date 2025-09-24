# 🧪 Testing Caja Negra

La técnica de **Caja Negra** se centra en probar entradas y salidas del sistema, sin conocer la implementación interna.

## 🎯 Particiones de Equivalencia
| Entrada              | Válida | Inválida |
|----------------------|--------|----------|
| Título               | Texto no vacío | Vacío o solo espacios |
| Prioridad            | alta, media, baja | otro valor (ej: "urgente") |
| ID de tarea (eliminar/completar) | ID existente | ID inexistente |

## 📐 Valores Límite
- Lista vacía (0 tareas).
- Una sola tarea.
- Muchas tareas (1000+).

## ✅ Casos de Prueba (15)
1. Agregar tarea con título válido.  
2. Agregar tarea sin título → error.  
3. Agregar tarea con título en blanco `"   "` → error.  
4. Agregar tarea con prioridad `"alta"`.  
5. Agregar tarea con prioridad `"urgente"` → error.  
6. Agregar tarea con descripción muy larga (1000 caracteres).  
7. Listar tareas cuando no hay ninguna → devuelve lista vacía.  
8. Listar por prioridad `"media"` sin tareas de esa prioridad → lista vacía.  
9. Completar tarea con ID válido → estado cambia a completada.  
10. Completar tarea con ID inexistente → error.  
11. Eliminar tarea con ID válido → desaparece de la lista.  
12. Eliminar tarea con ID inexistente → error.  
13. Agregar varias tareas y comprobar IDs secuenciales.  
14. Listar tareas filtradas por completadas (0, 1, N).  
15. Agregar 1000 tareas y verificar rendimiento aceptable.  

📌 **Resultado:** Todos los casos ejecutados, errores controlados y sistema robusto ante entradas inválidas.
