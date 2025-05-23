from sympy import symbols, Eq, solve
import numpy as np
import sounddevice as sd

class CircuitSolver:
    def __init__(self):
        self.I1, self.I2, self.I3 = symbols('I1 I2 I3')

    def setup_equations(self):
        # Ecuación 1: Ley de corrientes de Kirchhoff
        eq1 = Eq(self.I1, self.I2 + self.I3)

        # Se aplican ley de los voltajes de Kirchhoff
        # Rama del centro, recorrido horario
        # dio negativo entonces el recorrido es contrario)
        eq2 = Eq(-8*self.I1 - 6*self.I2 + 4, 0)

        # Rama derecha (recorrido horario)
        eq3 = Eq(8*self.I1 + 4*self.I3 - 12, 0)

        return [eq1, eq2, eq3]

    def solve(self):
        equations = self.setup_equations()
        solution = solve(equations, (self.I1, self.I2, self.I3))
        return solution

class MusicPhysics:
    def __init__(self):
        self.sample_rate = 44100
        self.duration = 1.0

    def current_to_frequency(self, current):
        base_freq = 220
        freq = base_freq * (1 + abs(float(current)))
        return freq

    def play_tone(self, freq):
        t = np.linspace(0, self.duration, int(self.sample_rate * self.duration), endpoint=False)
        wave = 0.5 * np.sin(2 * np.pi * freq * t)
        sd.play(wave, self.sample_rate)
        sd.wait()

    def play_currents(self, currents):
        print("\n🔉 Reproduciendo frecuencias basadas en las corrientes:")
        for name, current in currents.items():
            freq = self.current_to_frequency(current)
            print(f"{name} → {freq:.2f} Hz (corriente: {current:.4f} A)")
            self.play_tone(freq)

def main():
    solver = CircuitSolver()
    currents = solver.solve()


    I1, I2, I3 = solver.I1, solver.I2, solver.I3

    # Invertimos el signo de I2 porque sabemos que su dirección real es contraria
    currents[I2] = -currents[I2]

    print("⚡ Corrientes en cada rama (ajuste de dirección para I2):")
    for sym, current in currents.items():
        print(f"{sym} = {float(current):.4f} A")

    music = MusicPhysics()

    # Convertimos claves simbólicas a strings para impresión más clara
    music.play_currents({str(k): v for k, v in currents.items()})

if __name__ == "__main__":
    main()
