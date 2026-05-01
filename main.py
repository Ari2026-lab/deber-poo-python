"""Módulo principal que demuestra el uso del sistema de vehículos."""

from motor import Motor
from automovil import Automovil
from motocicleta import Motocicleta

# Crear motores con diferentes tipos y potencias
motor1 = Motor("Gasolina", 180)
motor2 = Motor("Diésel", 200)
motor3 = Motor("Gasolina", 45)
motor4 = Motor("Eléctrico", 50)

# Crear automóviles
auto1 = Automovil("Toyota", "Corolla", 2022, motor1, 4)
auto2 = Automovil("Chevrolet", "Spark", 2021, motor2, 5)

# Crear motocicletas
moto1 = Motocicleta("Yamaha", "R3", 2023, motor3, 300)
moto2 = Motocicleta("Honda", "CB190R", 2022, motor4, 190)

# Demostración con automóvil 1
print("=== DEMOSTRACION CON AUTOMOVIL 1 ===")
auto1.encender()
auto1.tocar_claxon()
auto1.abrir_maletero()

# Demostración con motocicleta 1
print("\n=== DEMOSTRACION CON MOTOCICLETA 1 ===")
moto1.encender()
moto1.hacer_caballito()
moto1.usar_patada_arranque()

# Mostrar información de todos los vehículos
print("\n=== INFORMACION DE LOS VEHICULOS ===")
print("Automóvil 1:")
print(auto1)
print("\nAutomóvil 2:")
print(auto2)
print("\nMotocicleta 1:")
print(moto1)
print("\nMotocicleta 2:")
print(moto2)