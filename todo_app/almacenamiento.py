"""Módulo que define la clase Almacenamiento."""

import json
import os
from pathlib import Path

class Almacenamiento:
    """Clase que maneja la persistencia de datos en JSON.
    
    Atributos:
        __ruta_archivo: Ruta del archivo de almacenamiento
    """
    
    def __init__(self, ruta_archivo="tareas.json"):
        """Inicializa el almacenamiento.
        
        Args:
            ruta_archivo: Ruta del archivo de almacenamiento
        """
        self.__ruta_archivo = ruta_archivo
        self.__crear_carpeta_si_no_existe()

    def __crear_carpeta_si_no_existe(self):
        """Crea la carpeta de datos si no existe."""
        directorio = os.path.dirname(self.__ruta_archivo)
        if directorio and not os.path.exists(directorio):
            os.makedirs(directorio)

    def guardar_tareas(self, tareas):
        """Guarda las tareas en archivo JSON.
        
        Args:
            tareas: Lista de objetos Tarea
            
        Returns:
            bool: True si se guardó correctamente
        """
        try:
            datos = [tarea.to_dict() for tarea in tareas]
            with open(self.__ruta_archivo, 'w', encoding='utf-8') as archivo:
                json.dump(datos, archivo, indent=4, ensure_ascii=False)
            return True
        except IOError as e:
            print(f"❌ Error al guardar tareas: {e}")
            return False

    def cargar_tareas(self):
        """Carga las tareas desde el archivo JSON.
        
        Returns:
            list: Lista de diccionarios con datos de tareas
        """
        try:
            if self.existe_archivo():
                with open(self.__ruta_archivo, 'r', encoding='utf-8') as archivo:
                    datos = json.load(archivo)
                    return datos if isinstance(datos, list) else []
            return []
        except json.JSONDecodeError:
            print(f"❌ Error: Archivo {self.__ruta_archivo} está corrupto")
            return []
        except IOError as e:
            print(f"❌ Error al cargar tareas: {e}")
            return []

    def existe_archivo(self):
        """Verifica si existe el archivo de almacenamiento.
        
        Returns:
            bool: True si existe el archivo
        """
        return os.path.exists(self.__ruta_archivo)

    def limpiar_almacenamiento(self):
        """Elimina el archivo de almacenamiento.
        
        Returns:
            bool: True si se eliminó correctamente
        """
        try:
            if self.existe_archivo():
                os.remove(self.__ruta_archivo)
                return True
            return True
        except IOError as e:
            print(f"❌ Error al limpiar almacenamiento: {e}")
            return False

    def obtener_ruta_archivo(self):
        """Obtiene la ruta del archivo de almacenamiento.
        
        Returns:
            str: Ruta del archivo
        """
        return self.__ruta_archivo

    def obtener_tamaño_archivo(self):
        """Obtiene el tamaño del archivo de almacenamiento en bytes.
        
        Returns:
            int: Tamaño en bytes, 0 si no existe
        """
        if self.existe_archivo():
            return os.path.getsize(self.__ruta_archivo)
        return 0