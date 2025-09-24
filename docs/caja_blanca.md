# 🧪 Testing Caja Blanca

La técnica de **Caja Blanca** analiza directamente el código para asegurar cobertura de ramas y condiciones.

## 🔀 Diagrama de Flujo Simplificado
```mermaid
flowchart TD
  Start --> CheckTitle
  CheckTitle{title.strip() == ""}
  CheckTitle -- yes --> ErrorTitulo
  CheckTitle -- no --> CheckPriority
  CheckPriority{priority in [alta, media, baja]}
  CheckPriority -- no --> ErrorPrioridad
  CheckPriority -- yes --> CrearTarea
  CrearTarea --> End
