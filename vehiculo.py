"""Módulo que define la clase base Vehiculo."""

class Vehiculo:
    """Clase base que representa un vehículo genérico.
    
    Atributos:
        __marca: Marca del vehículo
        __modelo: Modelo del vehículo
        __anio: Año de fabricación
        __motor: Motor del vehículo
    """
    
    def __init__(self, marca, modelo, anio, motor):
        """Inicializa un vehículo con sus características básicas.
        
        Args:
            marca: Marca del vehículo
            modelo: Modelo del vehículo
            anio: Año de fabricación
            motor: Objeto Motor del vehículo
        """
        self.__marca = marca
        self.__modelo = modelo
        self.__anio = anio
        self.__motor = motor

    @property
    def marca(self):
        """Obtiene la marca del vehículo."""
        return self.__marca

    @marca.setter
    def marca(self, nueva_marca):
        """Establece la marca del vehículo."""
        self.__marca = nueva_marca

    @property
    def modelo(self):
        """Obtiene el modelo del vehículo."""
        return self.__modelo

    @modelo.setter
    def modelo(self, nuevo_modelo):
        """Establece el modelo del vehículo."""
        self.__modelo = nuevo_modelo

    @property
    def anio(self):
        """Obtiene el año de fabricación del vehículo."""
        return self.__anio

    @anio.setter
    def anio(self, nuevo_anio):
        """Establece el año de fabricación del vehículo."""
        self.__anio = nuevo_anio

    @property
    def motor(self):
        """Obtiene el motor del vehículo."""
        return self.__motor

    @motor.setter
    def motor(self, nuevo_motor):
        """Establece el motor del vehículo."""
        self.__motor = nuevo_motor

    def encender(self):
        """Enciende el vehículo."""
        print("Vehículo encendido")

    def apagar(self):
        """Apaga el vehículo."""
        print("Vehículo apagado")

    def __str__(self):
        """Retorna la representación en texto del vehículo."""
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.anio}, {self.motor}"