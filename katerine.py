import sympy as sp

# Definir las corrientes desconocidas
I1, I2, I3 = sp.symbols('I1 I2 I3')  # Corrientes en ramas principales
V = 14  # Voltaje de la batería

# Ecuaciones de mallas usando las leyes de Kirchhoff:
# Malla 1 (batería → R1 → R3 → R2 → batería):
eq1 = -V + 1*I1 + 1*(I1 - I3) + 2*I2  # R1 + R3 + R2

# Malla 2 (R3 → R4 → R5 → R2):
eq2 = 1*(I3 - I1) + 2*I3 + 1*(I3 - I2)  # R3 + R4 + R5

# Nodo inferior (Ley de corrientes): I1 = I2 + I3
eq3 = I1 - I2 - I3

# Resolver el sistema
sol = sp.solve([eq1, eq2, eq3], (I1, I2, I3))

# Extraer soluciones
I1_val = sol[I1].evalf()
I2_val = sol[I2].evalf()
I3_val = sol[I3].evalf()

# Corrientes reales por cada resistor
I_R1 = I1_val
I_R2 = I2_val
I_R3 = I1_val - I3_val
I_R4 = I3_val
I_R5 = I2_val - I3_val

# Corriente total = I1 (sale de la batería)
I_bateria = I1_val

# Resistencia total de la red
R_total = V / I_bateria

# Mostrar resultados
print(f"Corriente a través de la batería: {I_bateria:.4f} A")
print(f"Corriente por R1 (1Ω): {I_R1:.4f} A")
print(f"Corriente por R2 (2Ω): {I_R2:.4f} A")
print(f"Corriente por R3 (1Ω): {I_R3:.4f} A")
print(f"Corriente por R4 (2Ω): {I_R4:.4f} A")
print(f"Corriente por R5 (1Ω): {I_R5:.4f} A")
print(f"\nResistencia total de la red: {R_total:.4f} Ω")
