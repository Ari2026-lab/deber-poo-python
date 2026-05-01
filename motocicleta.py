"""Módulo que define la clase Motocicleta."""

from vehiculo import Vehiculo

class Motocicleta(Vehiculo):
    """Clase que representa una motocicleta, hereda de Vehiculo.
    
    Atributos adicionales:
        __cilindraje: Cilindraje de la motocicleta en cc
    """
    
    def __init__(self, marca, modelo, anio, motor, cilindraje):
        """Inicializa una motocicleta con todas sus características.
        
        Args:
            marca: Marca de la motocicleta
            modelo: Modelo de la motocicleta
            anio: Año de fabricación
            motor: Motor de la motocicleta
            cilindraje: Cilindraje en cc
        """
        super().__init__(marca, modelo, anio, motor)
        self.__cilindraje = cilindraje

    @property
    def cilindraje(self):
        """Obtiene el cilindraje de la motocicleta."""
        return self.__cilindraje

    @cilindraje.setter
    def cilindraje(self, nuevo_cilindraje):
        """Establece el cilindraje de la motocicleta."""
        self.__cilindraje = nuevo_cilindraje

    def hacer_caballito(self):
        """Realiza un caballito con la motocicleta."""
        print("La motocicleta hace un caballito")

    def usar_patada_arranque(self):
        """Enciende la motocicleta con patada de arranque."""
        print("Motocicleta encendida con patada")

    def __str__(self):
        """Retorna la representación en texto de la motocicleta."""
        return super().__str__() + f", Cilindraje: {self.cilindraje} cc"