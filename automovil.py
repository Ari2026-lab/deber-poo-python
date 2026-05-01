"""Módulo que define la clase Automovil."""

from vehiculo import Vehiculo

class Automovil(Vehiculo):
    """Clase que representa un automóvil, hereda de Vehiculo.
    
    Atributos adicionales:
        __puertas: Número de puertas del automóvil
    """
    
    def __init__(self, marca, modelo, anio, motor, puertas):
        """Inicializa un automóvil con todas sus características.
        
        Args:
            marca: Marca del automóvil
            modelo: Modelo del automóvil
            anio: Año de fabricación
            motor: Motor del automóvil
            puertas: Número de puertas
        """
        super().__init__(marca, modelo, anio, motor)
        self.__puertas = puertas

    @property
    def puertas(self):
        """Obtiene el número de puertas del automóvil."""
        return self.__puertas

    @puertas.setter
    def puertas(self, nuevas_puertas):
        """Establece el número de puertas del automóvil."""
        self.__puertas = nuevas_puertas

    def abrir_maletero(self):
        """Abre el maletero del automóvil."""
        print("Maletero abierto")

    def tocar_claxon(self):
        """Toca el claxón del automóvil."""
        print("Piii Piii!")

    def __str__(self):
        """Retorna la representación en texto del automóvil."""
        return super().__str__() + f", Puertas: {self.puertas}"