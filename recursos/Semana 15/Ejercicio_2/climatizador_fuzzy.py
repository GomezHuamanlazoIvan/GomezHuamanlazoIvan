import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# 1. Variables de entrada y salida
temperatura = ctrl.Antecedent(np.arange(15, 41, 1), 'temperatura')
potencia = ctrl.Consequent(np.arange(0, 101, 1), 'potencia')

# 2. Conjuntos difusos
temperatura['baja'] = fuzz.trimf(temperatura.universe, [15, 15, 25])
temperatura['media'] = fuzz.trimf(temperatura.universe, [20, 27, 34])
temperatura['alta'] = fuzz.trimf(temperatura.universe, [30, 40, 40])

potencia['baja'] = fuzz.trimf(potencia.universe, [0, 0, 50])
potencia['media'] = fuzz.trimf(potencia.universe, [30, 50, 70])
potencia['alta'] = fuzz.trimf(potencia.universe, [60, 100, 100])

# 3. Reglas difusas IF-THEN
regla1 = ctrl.Rule(temperatura['baja'], potencia['baja'])
regla2 = ctrl.Rule(temperatura['media'], potencia['media'])
regla3 = ctrl.Rule(temperatura['alta'], potencia['alta'])

# 4. Sistema de control difuso
controlador = ctrl.ControlSystem([regla1, regla2, regla3])
simulador = ctrl.ControlSystemSimulation(controlador)

# 5. Prueba con entrada
simulador.input['temperatura'] = 39
simulador.compute()

print(f"Potencia sugerida del aire acondicionado: {simulador.output['potencia']:.2f}%")
