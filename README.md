#Ejercicio Empleado

Este código define una jerarquía de clases para representar a diferentes tipos de empleados y calcular sus salarios.

Clase Empleado:
Es la clase base que tiene dos atributos: nombre y __sueldo_base (este último es privado debido al encapsulamiento).
Proporciona métodos getter y setter para acceder y modificar el sueldo base, con validación en el setter para asegurar que el sueldo sea mayor o igual a cero.
Incluye un método calcular_salario() que se deja vacío para ser implementado en las clases hijas (esto es un ejemplo de polimorfismo).

Clase EmpleadoFijo (hereda de Empleado):
Implementa el método calcular_salario(), el cual simplemente devuelve el sueldo base, ya que es un empleado con un salario fijo.

Clase EmpleadoPorHoras (hereda de Empleado):
Tiene atributos adicionales: horas_trabajadas y tarifa_por_hora.

Implementa calcular_salario(), que calcula el salario multiplicando las horas trabajadas por la tarifa por hora.

Clase EmpleadoTemporal (hereda de Empleado):
Tiene el atributo dias_trabajados.

Implementa calcular_salario(), que calcula el salario según los días trabajados, basándose en el sueldo base dividido entre 30 (para obtener el salario diario).

Instanciación y polimorfismo:
Se crean tres empleados de diferentes tipos: fijo, por horas y temporal.
Luego, se utiliza polimorfismo para calcular y mostrar el salario de cada uno, llamando al método calcular_salario() de cada objeto, lo que da resultados diferentes según el tipo de empleado.
En resumen, el código demuestra el uso de la programación orientada a objetos (POO) con conceptos como encapsulamiento, herencia y polimorfismo para modelar y calcular los salarios de diferentes tipos de empleados.


#Ejercicio Transporte

El código define una jerarquía de clases para diferentes tipos de transporte: Transporte (base) y sus clases hijas Coche, Avion, y Barco. Cada clase hija sobrescribe el método Tipo_transporte() para devolver un mensaje específico según el tipo de transporte (terrestre, aéreo o marítimo). Luego, se crean instancias de cada tipo de transporte y se imprime el tipo correspondiente.

Este es un transporte Aéreo

Este es un transporte terrestre

Este es un transporte Marítimo
