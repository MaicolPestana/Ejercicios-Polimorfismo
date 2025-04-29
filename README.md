#Ejercicio Empleado

1. Clase Base: Empleado
class Empleado:
    def __init__(self, nombre, sueldo_base):
        self.nombre = nombre
        self.__sueldo_base = sueldo_base  # Encapsulamiento
Empleado es la clase base de la que heredarán todas las clases hijas.

Los atributos nombre y sueldo_base se inicializan en el constructor (__init__).

El atributo __sueldo_base es privado (mediante el uso de los dos guiones bajos __), lo que significa que no puede ser accedido directamente fuera de la clase. Este es un ejemplo de encapsulamiento.

    def get_sueldo_base(self):
        return self.__sueldo_base

    def set_sueldo_base(self, nuevo_sueldo):
        if nuevo_sueldo >= 0:
            self.__sueldo_base = nuevo_sueldo
        else:
            print("El sueldo debe ser mayor o igual a 0.")
get_sueldo_base(): Método que sirve como getter para obtener el valor del sueldo base.

set_sueldo_base(nuevo_sueldo): Método setter que permite cambiar el sueldo base, pero con una validación para asegurarse de que el sueldo sea mayor o igual a 0.

    def calcular_salario(self):
        pass
calcular_salario(): Este método es abstracto (en el sentido de que no hace nada en la clase base). Las clases hijas deben sobrescribir este método para calcular el salario de acuerdo a sus características.

2. Clase EmpleadoFijo (Hija de Empleado)

class EmpleadoFijo(Empleado):
    def calcular_salario(self):
        return self.get_sueldo_base()
EmpleadoFijo hereda de la clase Empleado.

El método calcular_salario() en esta clase simplemente devuelve el sueldo base, ya que los empleados fijos tienen un salario constante. Este es un ejemplo de polimorfismo, ya que calcular_salario() tiene un comportamiento diferente en esta clase comparado con las otras clases hijas.

3. Clase EmpleadoPorHoras (Hija de Empleado)

class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, sueldo_base, horas_trabajadas, tarifa_por_hora):
        super().__init__(nombre, sueldo_base)
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_por_hora = tarifa_por_hora
EmpleadoPorHoras hereda de la clase Empleado.

En el constructor (__init__), además de los atributos nombre y sueldo_base, se agregan los atributos horas_trabajadas (el número de horas trabajadas por el empleado) y tarifa_por_hora (el pago por cada hora trabajada).

    def calcular_salario(self):
        return self.horas_trabajadas * self.tarifa_por_hora
calcular_salario(): En este caso, el salario se calcula multiplicando las horas trabajadas por la tarifa por hora. Esta implementación muestra cómo el comportamiento del método calcular_salario() se adapta a un tipo de empleado diferente (por horas).

4. Clase EmpleadoTemporal (Hija de Empleado)
5. 
class EmpleadoTemporal(Empleado):
    def __init__(self, nombre, sueldo_base, dias_trabajados):
        super().__init__(nombre, sueldo_base)
        self.dias_trabajados = dias_trabajados
EmpleadoTemporal hereda de la clase Empleado.

En el constructor (__init__), además de los atributos nombre y sueldo_base, se agrega el atributo dias_trabajados, que indica cuántos días trabajó el empleado.

    def calcular_salario(self):
        salario_diario = self.get_sueldo_base() / 30
        return salario_diario * self.dias_trabajados
calcular_salario(): El salario se calcula dividiendo el sueldo base entre 30 (suponiendo que el sueldo base corresponde a un mes de 30 días) y luego multiplicando el salario diario por los días trabajados. Esto muestra cómo el cálculo del salario también varía según el tipo de empleado (en este caso, temporal).

5. Crear empleados y calcular salarios

empleado1 = EmpleadoFijo("Carlos", 2500)
empleado2 = EmpleadoPorHoras("Ana", 0, 120, 15)
empleado3 = EmpleadoTemporal("Luis", 1800, 10)

# Lista de empleados
lista_empleados = [empleado1, empleado2, empleado3]

# Calcular salarios usando polimorfismo
for empleado in lista_empleados:
    print(f"{empleado.nombre} gana: ${empleado.calcular_salario():.2f}")
Se crean tres objetos de tipo EmpleadoFijo, EmpleadoPorHoras y EmpleadoTemporal.
empleado1 es un empleado fijo con un sueldo base de 2500.
empleado2 es un empleado por horas, con un sueldo base de 0 (no se usa), 120 horas trabajadas y una tarifa de 15 por hora.
empleado3 es un empleado temporal con un sueldo base de 1800 y 10 días trabajados.
Luego, se crea una lista de empleados y se recorre esta lista usando un ciclo for para calcular y mostrar el salario de cada uno de ellos, aprovechando el polimorfismo. Cada tipo de empleado usa su propia versión del método calcular_salario().

Resultado esperado:
Si ejecutamos este código con los valores dados, la salida será algo así:
Carlos gana: $2500.00
Ana gana: $1800.00
Luis gana: $600.00
Carlos gana 2500 porque es un empleado fijo.
Ana gana 1800 porque trabajó 120 horas y tiene una tarifa de 15 USD por hora.
Luis gana 600 porque el sueldo base se divide entre 30 días (1800 / 30 = 60), y como trabajó 10 días, su salario es 60 * 10 = 600.

Conclusión:
Este código demuestra el uso de herencia, polimorfismo y encapsulamiento en la programación orientada a objetos. Cada clase hija define su propia forma de calcular el salario, y el uso de métodos getter y setter garantiza que el sueldo base esté correctamente protegido.
