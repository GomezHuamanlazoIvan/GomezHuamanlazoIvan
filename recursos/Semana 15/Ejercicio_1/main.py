class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años."

class Paciente(Persona):
    def __init__(self, nombre, edad, sintomas):
        super().__init__(nombre, edad)
        self.sintomas = sintomas

    def mostrar_sintomas(self):
        return f"Síntomas reportados: {', '.join(self.sintomas)}"
def diagnosticar(sintomas):
    if "fiebre" in sintomas and "tos" in sintomas and "dolor de garganta" in sintomas:
        return "Diagnóstico: Posible gripe común"
    elif "fiebre" in sintomas and "dolor muscular" in sintomas and "cansancio" in sintomas:
        return "Diagnóstico: Posible influenza"
    elif "dolor de cabeza" in sintomas and "mareos" in sintomas and "visión borrosa" in sintomas:
        return "Diagnóstico: Posible migraña"
    elif "tos" in sintomas and "dificultad para respirar" in sintomas:
        return "Diagnóstico: Posible bronquitis"
    else:
        return "Diagnóstico: No se identificó una condición clara. Se recomienda consulta médica."

if __name__ == "__main__":
    sintomas_ingresados = ["fiebre", "tos", "dolor de garganta"]
    paciente = Paciente("Lucía", 22, sintomas_ingresados)

    print(paciente.presentarse())
    print(paciente.mostrar_sintomas())
    resultado = diagnosticar(paciente.sintomas)
    print(resultado)
