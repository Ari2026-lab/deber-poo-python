# 📸 EJEMPLO DE EJECUCIÓN - GESTOR DE TAREAS

## Información del Sistema

- **Fecha de Ejecución**: 2026-05-01
- **Hora**: 14:32:45
- **Plataforma**: Python 3.9+
- **Repositorio**: https://github.com/Ari2026-lab/deber-poo-python
- **Usuario**: Ari2026-lab

---

## 🚀 EJECUCIÓN PASO A PASO

### **PASO 1: Iniciar el programa**

```bash
$ cd todo_app
$ python main.py
```

### **PASO 2: Pantalla Principal**

```
==================================================
║  GESTOR DE TAREAS - TO-DO LIST             ║
==================================================

📊 Estadísticas: 0/0 completadas 
   Progreso: 0%

--------------------------------------------------
1.  Ver todas las tareas
2.  Ver tareas pendientes
3.  Ver tareas completadas
4.  Crear nueva tarea
5.  Marcar tarea como completada
6.  Editar tarea
7.  Eliminar tarea
8.  Limpiar pantalla
9.  Salir
--------------------------------------------------

Selecciona una opción (1-9): 4
```

### **PASO 3: Crear Primera Tarea**

```
==================================================
║  GESTOR DE TAREAS - TO-DO LIST             ║
==================================================

➕ CREAR NUEVA TAREA
--------------------------------------------------
Título de la tarea: Estudiar Python
Descripción (opcional): Aprender POO y Programación Orientada a Objetos
Fecha de vencimiento (YYYY-MM-DD, opcional): 2026-05-15

✅ Tarea creada exitosamente
   ID: 1
   Título: Estudiar Python
   Descripción: Aprender POO y Programación Orientada a Objetos
   Vencimiento: 2026-05-15

👋 Presiona Enter para continuar...
```

**📝 Registro Automático en data/tareas.json:**
```json
{
  "id": 1,
  "titulo": "Estudiar Python",
  "descripcion": "Aprender POO y Programación Orientada a Objetos",
  "completada": false,
  "fecha_creacion": "2026-05-01 14:32:45",
  "fecha_vencimiento": "2026-05-15"
}
```

---

### **PASO 4: Crear Segunda Tarea**

```
==================================================
║  GESTOR DE TAREAS - TO-DO LIST             ║
==================================================

➕ CREAR NUEVA TAREA
--------------------------------------------------
Título de la tarea: Hacer Ejercicio
Descripción (opcional): 30 minutos de cardio en el gimnasio
Fecha de vencimiento (YYYY-MM-DD, opcional): 2026-05-02

✅ Tarea creada exitosamente
   ID: 2
   Título: Hacer Ejercicio
   Descripción: 30 minutos de cardio en el gimnasio
   Vencimiento: 2026-05-02

👋 Presiona Enter para continuar...
```

**📝 Registro Automático:**
```json
{
  "id": 2,
  "titulo": "Hacer Ejercicio",
  "descripcion": "30 minutos de cardio en el gimnasio",
  "completada": false,
  "fecha_creacion": "2026-05-01 14:33:12",
  "fecha_vencimiento": "2026-05-02"
}
```

---

### **PASO 5: Crear Tercera Tarea**

```
==================================================
║  GESTOR DE TAREAS - TO-DO LIST             ║
==================================================

➕ CREAR NUEVA TAREA
--------------------------------------------------
Título de la tarea: Proyecto GitHub
Descripción (opcional): Subir proyecto POO al repositorio
Fecha de vencimiento (YYYY-MM-DD, opcional): 2026-05-01

✅ Tarea creada exitosamente
   ID: 3
   Título: Proyecto GitHub
   Descripción: Subir proyecto POO al repositorio
   Vencimiento: 2026-05-01

👋 Presiona Enter para continuar...
```

---

### **PASO 6: Ver Todas las Tareas**

```
==================================================
║  GESTOR DE TAREAS - TO-DO LIST             ║
==================================================

📋 TODAS LAS TAREAS
------------------------------------------------------------
ID    Estado       Título                    Vencimiento    
------------------------------------------------------------
1     ◯ Pendiente   Estudiar Python           2026-05-15    
2     ◯ Pendiente   Hacer Ejercicio           2026-05-02    
3     ◯ Pendiente   Proyecto GitHub           2026-05-01    
------------------------------------------------------------
Total: 3 tareas

👋 Presiona Enter para continuar...
```

---

### **PASO 7: Marcar Tarea como Completada**

```
==================================================
║  GESTOR DE TAREAS - TO-DO LIST             ║
==================================================

✓ MARCAR TAREA COMO COMPLETADA
--------------------------------------------------
ID de la tarea: 3

✅ Estado actualizado a: ✓ Completada

👋 Presiona Enter para continuar...
```

**📝 Registro Actualizado en data/tareas.json:**
```json
{
  "id": 3,
  "titulo": "Proyecto GitHub",
  "descripcion": "Subir proyecto POO al repositorio",
  "completada": true,
  "fecha_creacion": "2026-05-01 14:34:20",
  "fecha_vencimiento": "2026-05-01"
}
```

---

### **PASO 8: Ver Tareas Pendientes**

```
==================================================
║  GESTOR DE TAREAS - TO-DO LIST             ║
==================================================

⏳ TAREAS PENDIENTES
------------------------------------------------------------
ID    Estado       Título                    Vencimiento    
------------------------------------------------------------
1     ◯ Pendiente   Estudiar Python           2026-05-15    
2     ◯ Pendiente   Hacer Ejercicio           2026-05-02    
------------------------------------------------------------
Total: 2 tareas

👋 Presiona Enter para continuar...
```

---

### **PASO 9: Ver Tareas Completadas**

```
==================================================
║  GESTOR DE TAREAS - TO-DO LIST             ║
==================================================

✅ TAREAS COMPLETADAS
------------------------------------------------------------
ID    Estado       Título                    Vencimiento    
------------------------------------------------------------
3     ✓ Completada  Proyecto GitHub           2026-05-01    
------------------------------------------------------------
Total: 1 tareas

👋 Presiona Enter para continuar...
```

---

### **PASO 10: Editar una Tarea**

```
==================================================
║  GESTOR DE TAREAS - TO-DO LIST             ║
==================================================

✏️  EDITAR TAREA
--------------------------------------------------
ID de la tarea a editar: 1

Tarea actual: Estudiar Python
Descripción: Aprender POO y Programación Orientada a Objetos

Nuevo título (Enter para mantener): Estudiar Python Avanzado
Nueva descripción (Enter para mantener): 
Nueva fecha de vencimiento (Enter para mantener): 2026-05-20

✅ Tarea actualizada exitosamente

👋 Presiona Enter para continuar...
```

---

### **PASO 11: Ver Menú Principal con Estadísticas Actualizadas**

```
==================================================
║  GESTOR DE TAREAS - TO-DO LIST             ║
==================================================

📊 Estadísticas: 1/3 completadas 
   Progreso: 33.33%

--------------------------------------------------
1.  Ver todas las tareas
2.  Ver tareas pendientes
3.  Ver tareas completadas
4.  Crear nueva tarea
5.  Marcar tarea como completada
6.  Editar tarea
7.  Eliminar tarea
8.  Limpiar pantalla
9.  Salir
--------------------------------------------------

Selecciona una opción (1-9): 
```

---

### **PASO 12: Eliminar una Tarea**

```
==================================================
║  GESTOR DE TAREAS - TO-DO LIST             ║
==================================================

🗑️  ELIMINAR TAREA
--------------------------------------------------
ID de la tarea a eliminar: 2

Tarea a eliminar: Hacer Ejercicio
¿Estás seguro? (s/n): s

✅ Tarea eliminada exitosamente

👋 Presiona Enter para continuar...
```

---

### **PASO 13: Salir del Programa**

```
==================================================
║  GESTOR DE TAREAS - TO-DO LIST             ║
==================================================

📊 Estadísticas: 1/2 completadas 
   Progreso: 50%

--------------------------------------------------
1.  Ver todas las tareas
2.  Ver tareas pendientes
3.  Ver tareas completadas
4.  Crear nueva tarea
5.  Marcar tarea como completada
6.  Editar tarea
7.  Eliminar tarea
8.  Limpiar pantalla
9.  Salir
--------------------------------------------------

Selecciona una opción (1-9): 9

👋 ¡Hasta luego! Tareas guardadas automáticamente.
```

---

## 📁 CONTENIDO FINAL DE data/tareas.json

```json
[
    {
        "id": 1,
        "titulo": "Estudiar Python Avanzado",
        "descripcion": "Aprender POO y Programación Orientada a Objetos",
        "completada": false,
        "fecha_creacion": "2026-05-01 14:32:45",
        "fecha_vencimiento": "2026-05-20"
    },
    {
        "id": 3,
        "titulo": "Proyecto GitHub",
        "descripcion": "Subir proyecto POO al repositorio",
        "completada": true,
        "fecha_creacion": "2026-05-01 14:34:20",
        "fecha_vencimiento": "2026-05-01"
    }
]
```

---

## ✨ CARACTERÍSTICAS DEMOSTRADAS

✅ **Creación de Tareas** - Con título, descripción y fecha
✅ **Fechas y Horas Automáticas** - `2026-05-01 14:32:45`
✅ **Almacenamiento Persistente** - Datos en JSON
✅ **Listado de Tareas** - Todas, pendientes y completadas
✅ **Cambio de Estado** - Marcar como completada
✅ **Edición de Tareas** - Modificar contenido
✅ **Eliminación de Tareas** - Con confirmación
✅ **Estadísticas** - Progreso en porcentaje
✅ **Interfaz Amigable** - Menú interactivo

---

## 🔗 ENLACES ÚTILES

- **Repositorio Principal**: https://github.com/Ari2026-lab/deber-poo-python
- **Proyecto To-Do List**: https://github.com/Ari2026-lab/deber-poo-python/tree/main/todo_app
- **Código Fuente**: https://github.com/Ari2026-lab/deber-poo-python/blob/main/todo_app/main.py

---

**✨ Ejemplo de ejecución completado exitosamente - Fecha: 2026-05-01 14:34:50**