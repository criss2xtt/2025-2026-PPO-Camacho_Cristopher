# Clase base (Herencia)

class Empleado:
    def __init__(self, nombre, salario):
        # Atributos protegidos (Encapsulación)
        self._nombre = nombre
        self._salario = salario

    # Método público
    def mostrar_info(self):
        return f"Empleado: {self._nombre}"

    # Método que será sobrescrito (Polimorfismo)
    def calcular_salario(self):
        return self._salario


# ==============================
# Clase derivada (Herencia)
# ==============================
class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, salario, bono):
        # Llamada al constructor de la clase base
        super().__init__(nombre, salario)
        self._bono = bono

    # Sobrescritura de método (Polimorfismo)
    def calcular_salario(self):
        return self._salario + self._bono


# ==============================
# Clase derivada (Herencia)
# ==============================
class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, horas_trabajadas, pago_por_hora):
        # El salario base se calcula dinámicamente
        super().__init__(nombre, 0)
        self._horas_trabajadas = horas_trabajadas
        self._pago_por_hora = pago_por_hora

    # Sobrescritura de método (Polimorfismo)
    def calcular_salario(self):
        return self._horas_trabajadas * self._pago_por_hora


# ==============================
# Programa principal
# ==============================
if __name__ == "__main__":
    # Creación de objetos (Instanciación)
    empleado1 = EmpleadoTiempoCompleto("Pablo", 600, 200)
    empleado2 = EmpleadoPorHoras("Amelia", 40, 12)

    # Lista de empleados (Polimorfismo)
    empleados = [empleado1, empleado2]

    # Uso de métodos
    for empleado in empleados:
        print(empleado.mostrar_info())
        print(f"Salario calculado: ${empleado.calcular_salario()}")
        print("-" * 30)
