"""Módulo que define la clase Tarea."""

from datetime import datetime

class Tarea:
    """Clase que representa una tarea individual.
    
    Atributos:
        __id: Identificador único de la tarea
        __titulo: Título de la tarea
        __descripcion: Descripción detallada
        __completada: Estado de la tarea
        __fecha_creacion: Fecha de creación
        __fecha_vencimiento: Fecha límite
    """
    
    def __init__(self, id, titulo, descripcion="", fecha_vencimiento=""):
        """Inicializa una tarea.
        
        Args:
            id: Identificador único
            titulo: Título de la tarea
            descripcion: Descripción (opcional)
            fecha_vencimiento: Fecha límite (opcional)
        """
        self.__id = id
        self.__titulo = titulo
        self.__descripcion = descripcion
        self.__completada = False
        self.__fecha_creacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.__fecha_vencimiento = fecha_vencimiento

    @property
    def id(self):
        """Obtiene el ID de la tarea."""
        return self.__id

    @property
    def titulo(self):
        """Obtiene el título de la tarea."""
        return self.__titulo

    @titulo.setter
    def titulo(self, nuevo_titulo):
        """Establece el título de la tarea."""
        if nuevo_titulo.strip():
            self.__titulo = nuevo_titulo
        else:
            raise ValueError("El título no puede estar vacío")

    @property
    def descripcion(self):
        """Obtiene la descripción de la tarea."""
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, nueva_descripcion):
        """Establece la descripción de la tarea."""
        self.__descripcion = nueva_descripcion

    @property
    def completada(self):
        """Obtiene el estado de la tarea."""
        return self.__completada

    @property
    def fecha_creacion(self):
        """Obtiene la fecha de creación."""
        return self.__fecha_creacion

    @property
    def fecha_vencimiento(self):
        """Obtiene la fecha de vencimiento."""
        return self.__fecha_vencimiento

    @fecha_vencimiento.setter
    def fecha_vencimiento(self, nueva_fecha):
        """Establece la fecha de vencimiento."""
        self.__fecha_vencimiento = nueva_fecha

    def marcar_completada(self):
        """Marca la tarea como completada."""
        self.__completada = True

    def marcar_pendiente(self):
        """Marca la tarea como pendiente."""
        self.__completada = False

    def togglear_estado(self):
        """Cambia el estado de la tarea."""
        self.__completada = not self.__completada

    def to_dict(self):
        """Convierte la tarea a diccionario.
        
        Returns:
            dict: Representación en diccionario
        """
        return {
            "id": self.__id,
            "titulo": self.__titulo,
            "descripcion": self.__descripcion,
            "completada": self.__completada,
            "fecha_creacion": self.__fecha_creacion,
            "fecha_vencimiento": self.__fecha_vencimiento
        }

    @staticmethod
    def from_dict(datos):
        """Crea una tarea desde un diccionario.
        
        Args:
            datos: Diccionario con datos de la tarea
            
        Returns:
            Tarea: Nueva instancia de Tarea
        """
        tarea = Tarea(
            datos["id"],
            datos["titulo"],
            datos.get("descripcion", ""),
            datos.get("fecha_vencimiento", "")
        )
        if datos.get("completada", False):
            tarea.marcar_completada()
        # Restaurar fecha de creación
        tarea._Tarea__fecha_creacion = datos["fecha_creacion"]
        return tarea

    def __str__(self):
        """Retorna la representación en texto de la tarea."""
        estado = "✓ Completada" if self.__completada else "○ Pendiente"
        vencimiento = f" (Vence: {self.__fecha_vencimiento})" if self.__fecha_vencimiento else ""
        return f"[{self.__id}] {self.__titulo} - {estado}{vencimiento}"

    def __repr__(self):
        """Retorna la representación oficial de la tarea."""
        return f"Tarea(id={self.__id}, titulo='{self.__titulo}', completada={self.__completada})"