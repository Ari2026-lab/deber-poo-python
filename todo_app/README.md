# Aplicación de Lista de Tareas (To-Do List)

## 📋 Descripción

Aplicación de línea de comandos para gestionar una lista de tareas con almacenamiento local en JSON. Permite crear, editar, eliminar, marcar como completada y listar tareas de forma persistente.

## ✨ Características

- ✅ **Crear tareas** - Agregar nuevas tareas a la lista
- ✅ **Listar tareas** - Ver todas las tareas o filtrar por estado
- ✅ **Marcar completadas** - Cambiar el estado de una tarea
- ✅ **Editar tareas** - Modificar el contenido de una tarea
- ✅ **Eliminar tareas** - Borrar tareas de la lista
- ✅ **Almacenamiento persistente** - Guardar datos en JSON
- ✅ **Interfaz intuitiva** - Menú interactivo fácil de usar

## 🏗️ Estructura del Proyecto

```
todo_app/
├── README.md              # Este archivo
├── main.py                # Programa principal (menú)
├── tarea.py               # Clase Tarea
├── gestor_tareas.py       # Clase GestorTareas
├── almacenamiento.py      # Clase Almacenamiento
├── tareas.json            # Archivo de almacenamiento (se crea automáticamente)
└── data/                  # Carpeta para datos (se crea automáticamente)
```

## 🏛️ Estructura de Clases

### 1. **Tarea** (`tarea.py`)
Representa una tarea individual.

**Atributos:**
- `id`: Identificador único
- `titulo`: Título de la tarea
- `descripcion`: Descripción detallada
- `completada`: Estado (True/False)
- `fecha_creacion`: Fecha de creación
- `fecha_vencimiento`: Fecha límite (opcional)

**Métodos:**
- `marcar_completada()` - Marca la tarea como completada
- `marcar_pendiente()` - Marca la tarea como pendiente
- `to_dict()` - Convierte a diccionario
- `from_dict()` - Crea desde diccionario

### 2. **Almacenamiento** (`almacenamiento.py`)
Maneja la persistencia de datos en JSON.

**Métodos:**
- `guardar_tareas()` - Guarda tareas en archivo
- `cargar_tareas()` - Carga tareas del archivo
- `existe_archivo()` - Verifica si existe el archivo

### 3. **GestorTareas** (`gestor_tareas.py`)
Maneja la lógica de negocio de las tareas.

**Métodos:**
- `agregar_tarea()` - Crea nueva tarea
- `obtener_tareas()` - Obtiene todas las tareas
- `obtener_tarea_por_id()` - Busca tarea por ID
- `actualizar_tarea()` - Modifica una tarea
- `eliminar_tarea()` - Borra una tarea
- `marcar_completada()` - Marca como completada
- `obtener_tareas_pendientes()` - Filtra tareas pendientes
- `obtener_tareas_completadas()` - Filtra tareas completadas
- `guardar_cambios()` - Persiste los cambios

### 4. **Interfaz Principal** (`main.py`)
Menú interactivo para el usuario.

**Opciones:**
1. Ver todas las tareas
2. Ver tareas pendientes
3. Ver tareas completadas
4. Crear nueva tarea
5. Marcar tarea como completada
6. Editar tarea
7. Eliminar tarea
8. Salir

## 📊 Conceptos de POO

### ✅ Encapsulación
- Atributos privados con `__`
- Propiedades y setters para control de acceso

### ✅ Herencia
- Posibilidad de extender la clase `Tarea` (ej: `TareaRecurrente`)

### ✅ Composición
- `GestorTareas` utiliza objetos `Tarea`
- `GestorTareas` utiliza `Almacenamiento`

### ✅ Abstracción
- Métodos bien definidos y responsables
- Separación de concerns

### ✅ Polimorfismo
- Métodos to_dict() y from_dict() para conversión

## 🚀 Cómo Usar

### Instalación

1. **Descarga o clona el repositorio**

2. **Navega a la carpeta**
   ```bash
   cd todo_app
   ```

3. **Ejecuta la aplicación**
   ```bash
   python main.py
   ```

### Ejemplo de Uso Interactivo

```
╔════════════════════════════════════════╗
║   GESTOR DE TAREAS - TO-DO LIST        ║
╚════════════════════════════════════════╝

1. Ver todas las tareas
2. Ver tareas pendientes
3. Ver tareas completadas
4. Crear nueva tarea
5. Marcar tarea como completada
6. Editar tarea
7. Eliminar tarea
8. Salir

Selecciona una opción (1-8): 4

Título de la tarea: Estudiar Python
Descripción (opcional): Aprender POO y listas
Fecha de vencimiento (opcional, YYYY-MM-DD): 2026-05-15

✅ Tarea creada exitosamente (ID: 1)
```

## 💾 Formato de Almacenamiento (JSON)

```json
[
  {
    "id": 1,
    "titulo": "Estudiar Python",
    "descripcion": "Aprender POO",
    "completada": false,
    "fecha_creacion": "2026-05-01T10:30:00",
    "fecha_vencimiento": "2026-05-15"
  },
  {
    "id": 2,
    "titulo": "Hacer ejercicio",
    "descripcion": "30 minutos de cardio",
    "completada": true,
    "fecha_creacion": "2026-05-01T11:00:00",
    "fecha_vencimiento": "2026-05-02"
  }
]
```

## 🔧 Requisitos

- Python 3.6 o superior
- No requiere dependencias externas

## 📝 Funcionalidades Detalladas

### Crear Tarea
- Solicita título (obligatorio)
- Solicita descripción (opcional)
- Solicita fecha de vencimiento (opcional)
- Asigna ID automático
- Guarda en almacenamiento

### Ver Tareas
- Muestra todas las tareas en formato tabular
- Indica estado (✓ Completada / ○ Pendiente)
- Ordena por ID o fecha

### Marcar Completada
- Permite cambiar el estado de una tarea
- Solicita el ID de la tarea
- Actualiza el almacenamiento

### Editar Tarea
- Permite modificar título y descripción
- Solicita el ID de la tarea
- Mantiene ID y fechas

### Eliminar Tarea
- Permite eliminar una tarea
- Solicita confirmación
- Actualiza el almacenamiento

## 🎯 Casos de Uso

1. **Usuario estudiante**: Gestionar tareas de estudio
2. **Usuario trabajador**: Organizar tareas del proyecto
3. **Usuario personal**: Seguimiento de tareas del hogar
4. **Usuario gestor**: Supervisar múltiples tareas

## 🔒 Características de Seguridad

- Validación de entrada de datos
- Manejo de excepciones
- Confirmación antes de eliminar
- IDs únicos para cada tarea

## 📈 Posibles Mejoras Futuras

- [ ] Base de datos SQL
- [ ] Interfaz gráfica (GUI)
- [ ] Sincronización en la nube
- [ ] Recordatorios y notificaciones
- [ ] Categorías y etiquetas
- [ ] Prioridades
- [ ] Búsqueda avanzada
- [ ] Estadísticas

## 👨‍💻 Autor

Estudiante de Programación - Proyecto POO

## 📅 Fecha de Creación

2026-05-01

---

**¡Aplicación completada exitosamente! 🎉**