import cv2
import numpy as np
import easyocr
from sympy import symbols, Eq, solve

# Ruta de la imagen
image_path = r"D:\V Semestre\Fisica II\circuito_ Katerine.jpg"

# Cargar imagen
image = cv2.imread(image_path)

# OCR para extraer texto
reader = easyocr.Reader(['en'])
results = reader.readtext(image)

# Procesar valores encontrados
resistores = []
voltaje = 0.0

print("📃 Valores detectados en la imagen:")
for (_, text, _) in results:
    try:
        val = float(text)
        print(f"🔍 Detectado: {val}")
        if val >= 5:   # Posible voltaje
            voltaje = val
        else:          # Posible resistencia
            resistores.append(val)
    except ValueError:
        continue

# Verificación de datos
if len(resistores) != 5 or voltaje == 0:
    print("\n❌ No se detectaron correctamente los 5 resistores y el voltaje.")
    print(f"Resistores detectados: {resistores}")
    print(f"Voltaje detectado: {voltaje}")
    exit()

# Asignación
R1, R2, R3, R4, R5 = resistores
V = voltaje

# Variables de corriente
I1, I2, I3 = symbols('I1 I2 I3')

# Ecuaciones
eq1 = Eq(R1 * I1, R2 * I2 + R3 * I2)  # Malla superior
eq2 = Eq(R4 * I3 + R5 * I3, V)        # Malla inferior
eq3 = Eq(I1, I2 + I3)                 # Nodo

# Resolución
solution = solve((eq1, eq2, eq3), (I1, I2, I3))
I1_val = float(solution[I1])
I2_val = float(solution[I2])
I3_val = float(solution[I3])
Req = V / I1_val

# Resultados
print("\n✅ Resultados del circuito:")
print(f"🔋 Corriente total de la batería (I1)  : {I1_val:.4f} A")
print(f"🔸 Corriente en R1                    : {I1_val:.4f} A")
print(f"🔸 Corriente en R2                    : {I2_val:.4f} A")
print(f"🔸 Corriente en R3                    : {I2_val:.4f} A")
print(f"🔸 Corriente en R4                    : {I3_val:.4f} A")
print(f"🔸 Corriente en R5                    : {I3_val:.4f} A")
print(f"🧮 Resistencia equivalente del circuito: {Req:.4f} Ohmios")
