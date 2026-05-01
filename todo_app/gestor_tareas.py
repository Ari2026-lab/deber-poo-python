"""Módulo que define la clase GestorTareas."""

from tarea import Tarea
from almacenamiento import Almacenamiento

class GestorTareas:
    """Clase que gestiona todas las operaciones con tareas.
    
    Atributos:
        __tareas: Lista de objetos Tarea
        __almacenamiento: Objeto de almacenamiento
        __proximo_id: Siguiente ID disponible
    """
    
    def __init__(self, ruta_almacenamiento="tareas.json"):
        """Inicializa el gestor de tareas.
        
        Args:
            ruta_almacenamiento: Ruta del archivo de almacenamiento
        """
        self.__almacenamiento = Almacenamiento(ruta_almacenamiento)
        self.__tareas = []
        self.__proximo_id = 1
        self.__cargar_tareas()

    def __cargar_tareas(self):
        """Carga las tareas desde almacenamiento."""
        datos = self.__almacenamiento.cargar_tareas()
        for dato in datos:
            tarea = Tarea.from_dict(dato)
            self.__tareas.append(tarea)
            if tarea.id >= self.__proximo_id:
                self.__proximo_id = tarea.id + 1

    def agregar_tarea(self, titulo, descripcion="", fecha_vencimiento=""):
        """Agrega una nueva tarea.
        
        Args:
            titulo: Título de la tarea
            descripcion: Descripción (opcional)
            fecha_vencimiento: Fecha de vencimiento (opcional)
            
        Returns:
            Tarea: La tarea creada
        """
        if not titulo.strip():
            raise ValueError("El título de la tarea no puede estar vacío")
        
        tarea = Tarea(self.__proximo_id, titulo, descripcion, fecha_vencimiento)
        self.__tareas.append(tarea)
        self.__proximo_id += 1
        self.guardar_cambios()
        return tarea

    def obtener_tareas(self):
        """Obtiene todas las tareas.
        
        Returns:
            list: Lista de tareas
        """
        return self.__tareas

    def obtener_tarea_por_id(self, id_tarea):
        """Obtiene una tarea por su ID.
        
        Args:
            id_tarea: ID de la tarea
            
        Returns:
            Tarea o None: La tarea encontrada o None
        """
        for tarea in self.__tareas:
            if tarea.id == id_tarea:
                return tarea
        return None

    def obtener_tareas_pendientes(self):
        """Obtiene todas las tareas pendientes.
        
        Returns:
            list: Lista de tareas pendientes
        """
        return [tarea for tarea in self.__tareas if not tarea.completada]

    def obtener_tareas_completadas(self):
        """Obtiene todas las tareas completadas.
        
        Returns:
            list: Lista de tareas completadas
        """
        return [tarea for tarea in self.__tareas if tarea.completada]

    def actualizar_tarea(self, id_tarea, titulo=None, descripcion=None, fecha_vencimiento=None):
        """Actualiza una tarea existente.
        
        Args:
            id_tarea: ID de la tarea a actualizar
            titulo: Nuevo título (opcional)
            descripcion: Nueva descripción (opcional)
            fecha_vencimiento: Nueva fecha de vencimiento (opcional)
            
        Returns:
            bool: True si se actualizó correctamente
        """
        tarea = self.obtener_tarea_por_id(id_tarea)
        if not tarea:
            return False
        
        if titulo is not None and titulo.strip():
            tarea.titulo = titulo
        if descripcion is not None:
            tarea.descripcion = descripcion
        if fecha_vencimiento is not None:
            tarea.fecha_vencimiento = fecha_vencimiento
        
        self.guardar_cambios()
        return True

    def marcar_completada(self, id_tarea):
        """Marca una tarea como completada.
        
        Args:
            id_tarea: ID de la tarea
            
        Returns:
            bool: True si se marcó correctamente
        """
        tarea = self.obtener_tarea_por_id(id_tarea)
        if not tarea:
            return False
        
        tarea.marcar_completada()
        self.guardar_cambios()
        return True

    def marcar_pendiente(self, id_tarea):
        """Marca una tarea como pendiente.
        
        Args:
            id_tarea: ID de la tarea
            
        Returns:
            bool: True si se marcó correctamente
        """
        tarea = self.obtener_tarea_por_id(id_tarea)
        if not tarea:
            return False
        
        tarea.marcar_pendiente()
        self.guardar_cambios()
        return True

    def togglear_estado(self, id_tarea):
        """Cambia el estado de una tarea.
        
        Args:
            id_tarea: ID de la tarea
            
        Returns:
            bool: True si se cambió correctamente
        """
        tarea = self.obtener_tarea_por_id(id_tarea)
        if not tarea:
            return False
        
        tarea.togglear_estado()
        self.guardar_cambios()
        return True

    def eliminar_tarea(self, id_tarea):
        """Elimina una tarea.
        
        Args:
            id_tarea: ID de la tarea a eliminar
            
        Returns:
            bool: True si se eliminó correctamente
        """
        tarea = self.obtener_tarea_por_id(id_tarea)
        if not tarea:
            return False
        
        self.__tareas.remove(tarea)
        self.guardar_cambios()
        return True

    def guardar_cambios(self):
        """Guarda todos los cambios en almacenamiento.
        
        Returns:
            bool: True si se guardó correctamente
        """
        return self.__almacenamiento.guardar_tareas(self.__tareas)

    def contar_tareas_pendientes(self):
        """Cuenta el número de tareas pendientes.
        
        Returns:
            int: Número de tareas pendientes
        """
        return len(self.obtener_tareas_pendientes())

    def contar_tareas_completadas(self):
        """Cuenta el número de tareas completadas.
        
        Returns:
            int: Número de tareas completadas
        """
        return len(self.obtener_tareas_completadas())

    def obtener_estadisticas(self):
        """Obtiene estadísticas del gestor de tareas.
        
        Returns:
            dict: Diccionario con estadísticas
        """
        total = len(self.__tareas)
        completadas = self.contar_tareas_completadas()
        pendientes = self.contar_tareas_pendientes()
        porcentaje = (completadas / total * 100) if total > 0 else 0
        
        return {
            "total": total,
            "completadas": completadas,
            "pendientes": pendientes,
            "porcentaje_completado": round(porcentaje, 2)
        }