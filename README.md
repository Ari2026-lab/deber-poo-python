# Deber POO en Python - Sistema de Vehículos

## 📋 Descripción del Programa

Este proyecto implementa un **sistema de gestión de vehículos** utilizando **Programación Orientada a Objetos (POO)** en Python. El programa modela diferentes tipos de vehículos (automóviles y motocicletas) con sus características y comportamientos específicos.

## 🎯 Objetivos

- Aplicar conceptos fundamentales de POO: herencia, encapsulación, polimorfismo y composición
- Crear una estructura de clases jerárquica y bien organizada
- Implementar propiedades y métodos específicos para cada tipo de vehículo
- Demostrar el funcionamiento del sistema con ejemplos prácticos

## 🏗️ Estructura de Clases

```
Motor
  └─ (utilizado por)
     └─ Vehiculo (clase base)
        ├─ Automovil
        └─ Motocicleta
```

## 📚 Descripción de Clases

### 1. **Motor** (`motor.py`)
Representa el motor de un vehículo.

**Atributos privados:**
- `__tipo`: Tipo de combustible (Gasolina, Diésel, Eléctrico)
- `__potencia`: Potencia en HP

**Métodos:**
- `encender_motor()`: Enciende el motor
- `detener_motor()`: Detiene el motor
- Getters y setters para tipo y potencia
- `__str__()`: Representación en texto

### 2. **Vehiculo** (`vehiculo.py`)
Clase base abstracta para todos los vehículos.

**Atributos privados:**
- `__marca`: Marca del vehículo
- `__modelo`: Modelo del vehículo
- `__anio`: Año de fabricación
- `__motor`: Objeto Motor asociado

**Métodos:**
- `encender()`: Enciende el vehículo
- `apagar()`: Apaga el vehículo
- Getters y setters para todos los atributos
- `__str__()`: Representación en texto

### 3. **Automovil** (`automovil.py`)
Clase que hereda de Vehiculo, representa automóviles.

**Atributos privados adicionales:**
- `__puertas`: Número de puertas

**Métodos propios:**
- `abrir_maletero()`: Abre el maletero
- `tocar_claxon()`: Toca el claxón
- Getter y setter para puertas
- `__str__()`: Representación extendida

### 4. **Motocicleta** (`motocicleta.py`)
Clase que hereda de Vehiculo, representa motocicletas.

**Atributos privados adicionales:**
- `__cilindraje`: Cilindraje en cc

**Métodos propios:**
- `hacer_caballito()`: Realiza un caballito
- `usar_patada_arranque()`: Enciende con patada
- Getter y setter para cilindraje
- `__str__()`: Representación extendida

## 💡 Conceptos de POO Implementados

### ✅ **Herencia**
Las clases `Automovil` y `Motocicleta` heredan de `Vehiculo`, reutilizando código común.

```python
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, anio, motor, puertas):
        super().__init__(marca, modelo, anio, motor)
```

### ✅ **Encapsulación**
Los atributos son privados (con `__`) y se accede mediante propiedades.

```python
@property
def puertas(self):
    return self.__puertas
```

### ✅ **Composición**
La clase `Vehiculo` contiene un objeto `Motor`.

### ✅ **Polimorfismo**
Cada clase implementa su propio `__str__()` y métodos específicos.

### ✅ **Propiedades (Properties)**
Uso de decoradores `@property` y `@setter` para getters y setters.

## 🚀 Instrucciones de Uso

### Requisitos
- Python 3.6 o superior

### Ejecución

1. **Clona o descarga el repositorio**

2. **Navega a la carpeta del proyecto**
   ```bash
   cd deber-poo-python
   ```

3. **Ejecuta el programa principal**
   ```bash
   python main.py
   ```

## 📝 Ejemplo de Uso

```python
from motor import Motor
from automovil import Automovil
from motocicleta import Motocicleta

# Crear motores
motor1 = Motor("Gasolina", 180)
motor2 = Motor("Eléctrico", 50)

# Crear vehículos
auto = Automovil("Toyota", "Corolla", 2022, motor1, 4)
moto = Motocicleta("Yamaha", "R3", 2023, motor2, 300)

# Usar vehículos
auto.encender()
auto.tocar_claxon()
auto.abrir_maletero()

moto.encender()
moto.hacer_caballito()

# Mostrar información
print(auto)
print(moto)
```

## 📤 Salida Esperada

```
Vehículo encendido
Piii Piii!
Mailetero abierto
Vehículo encendido
La motocicleta hace un caballito
Motocicleta encendida con patada
Marca: Toyota, Modelo: Corolla, Año: 2022, Motor: Gasolina, Potencia: 180 HP, Puertas: 4
Marca: Yamaha, Modelo: R3, Año: 2023, Motor: Eléctrico, Potencia: 50 HP, Cilindraje: 300 cc
```

## 📁 Estructura del Proyecto

```
deber-poo-python/
├── README.md          # Este archivo
├── motor.py           # Clase Motor
├── vehiculo.py        # Clase base Vehiculo
├── automovil.py       # Clase Automovil
├── motocicleta.py     # Clase Motocicleta
├── main.py            # Programa principal
└── .gitignore         # Archivos ignorados por Git
```

## 👤 Autor

Estudiante de Programación - Deber POO

## 📅 Fecha de Entrega

2026-05-01

## 📖 Notas Adicionales

- El código está completamente comentado para facilitar la comprensión
- Todos los atributos son privados, siguiendo buenas prácticas de encapsulación
- El uso de `super()` demuestra la llamada a métodos de la clase padre
- Las propiedades permiten validación y control de acceso a los atributos

---

**¡Proyecto completado exitosamente! ✨**