import sympy as sp

# Definir corrientes desconocidas
I1, I2, I3 = sp.symbols('I1 I2 I3')
V = 14  # Voltaje de la batería

# Ecuaciones de mallas
eq1 = 3*I1 - I2 - 2*I3 - V
eq2 = -I1 + 4*I2 - I3
eq3 = -2*I1 - I2 + 4*I3

# Resolver sistema
sol = sp.solve([eq1, eq2, eq3], (I1, I2, I3))

I1_val = sol[I1].evalf()
I2_val = sol[I2].evalf()
I3_val = sol[I3].evalf()

# Corriente real por cada resistor
I_R1 = I1_val - I2_val  # Entre mallas 1 y 2
I_R2 = I2_val           # Solo malla 2
I_R3 = I2_val - I3_val  # Entre mallas 2 y 3
I_R4 = I1_val - I3_val  # Entre mallas 1 y 3
I_R5 = I3_val           # Solo malla 3

# Corriente total (sale de la batería, malla 1)
I_bateria = I1_val

# Resistencia total equivalente
R_total = V / I_bateria

# Resultados
print(f"Corriente a través de la batería: {I_bateria:.4f} A")
print(f"Corriente por R1 (1Ω): {I_R1:.4f} A")
print(f"Corriente por R2 (2Ω): {I_R2:.4f} A")
print(f"Corriente por R3 (1Ω): {I_R3:.4f} A")
print(f"Corriente por R4 (2Ω): {I_R4:.4f} A")
print(f"Corriente por R5 (1Ω): {I_R5:.4f} A")
print(f"\nResistencia total de la red: {R_total:.4f} Ω")
