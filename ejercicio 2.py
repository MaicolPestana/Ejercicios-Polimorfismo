# Clase base
class Empleado:
    def __init__(self, nombre, sueldo_base):
        self.nombre = nombre
        self.__sueldo_base = sueldo_base  # Encapsulamiento

    # Getter
    def get_sueldo_base(self):
        return self.__sueldo_base

    # Setter
    def set_sueldo_base(self, nuevo_sueldo):
        if nuevo_sueldo >= 0:
            self.__sueldo_base = nuevo_sueldo
        else:
            print("El sueldo debe ser mayor o igual a 0.")

    # Método a sobrescribir
    def calcular_salario(self):
        pass


# Clase hija: Empleado Fijo
class EmpleadoFijo(Empleado):
    def calcular_salario(self):
        return self.get_sueldo_base()


# Clase hija: Empleado por Horas
class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, sueldo_base, horas_trabajadas, tarifa_por_hora):
        super().__init__(nombre, sueldo_base)
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_por_hora = tarifa_por_hora

    def calcular_salario(self):
        return self.horas_trabajadas * self.tarifa_por_hora


# Clase hija: Empleado Temporal
class EmpleadoTemporal(Empleado):
    def __init__(self, nombre, sueldo_base, dias_trabajados):
        super().__init__(nombre, sueldo_base)
        self.dias_trabajados = dias_trabajados

    def calcular_salario(self):
        salario_diario = self.get_sueldo_base() / 30
        return salario_diario * self.dias_trabajados


# Crear empleados
empleado1 = EmpleadoFijo("Carlos", 2500)
empleado2 = EmpleadoPorHoras("Ana", 0, 120, 15)
empleado3 = EmpleadoTemporal("Luis", 1800, 10)

# Lista de empleados
lista_empleados = [empleado1, empleado2, empleado3]

# Calcular salarios usando polimorfismo
for empleado in lista_empleados:
    print(f"{empleado.nombre} gana: ${empleado.calcular_salario():.2f}")
