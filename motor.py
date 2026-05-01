"""Módulo que define la clase Motor."""

class Motor:
    """Clase que representa el motor de un vehículo.
    
    Atributos:
        __tipo: Tipo de combustible del motor
        __potencia: Potencia del motor en HP
    """
    
    def __init__(self, tipo, potencia):
        """Inicializa un motor con tipo y potencia.
        
        Args:
            tipo: Tipo de combustible (Gasolina, Diésel, Eléctrico)
            potencia: Potencia en HP
        """
        self.__tipo = tipo
        self.__potencia = potencia

    @property
    def tipo(self):
        """Obtiene el tipo de combustible del motor."""
        return self.__tipo

    @tipo.setter
    def tipo(self, nuevo_tipo):
        """Establece el tipo de combustible del motor."""
        self.__tipo = nuevo_tipo

    @property
    def potencia(self):
        """Obtiene la potencia del motor."""
        return self.__potencia

    @potencia.setter
    def potencia(self, nueva_potencia):
        """Establece la potencia del motor."""
        self.__potencia = nueva_potencia

    def encender_motor(self):
        """Enciende el motor."""
        print("Motor encendido")

    def detener_motor(self):
        """Detiene el motor."""
        print("Motor apagado")

    def __str__(self):
        """Retorna la representación en texto del motor."""
        return f"Motor: {self.tipo}, Potencia: {self.potencia} HP"