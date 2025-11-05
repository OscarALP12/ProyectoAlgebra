import math

# --- (Aquí va la clase NumeroComplejo que escribimos antes) ---
class NumeroComplejo:
    def __init__(self, valor1, valor2, modo='binomica'):
        if modo == 'binomica':
            self.a = valor1
            self.b = valor2
            self.r = math.sqrt(self.a**2 + self.b**2)
            self.theta = math.atan2(self.b, self.a) 
        elif modo == 'polar':
            self.r = valor1
            self.theta = valor2
            self.a = self.r * math.cos(self.theta)
            self.b = self.r * math.sin(self.theta)
            
    def mostrar_binomica(self):
        if self.b < 0:
            return f"{self.a} - {abs(self.b)}i"
        else:
            return f"{self.a} + {self.b}i"

    def mostrar_polar(self):
        grados = math.degrees(self.theta)
        return f"{self.r:.4f} * (cos({grados:.4f}°) + i*sin({grados:.4f}°))"

# --- (Aquí irían tus funciones de suma, resta, etc.) ---
def suma_compleja(z1, z2):
    # z1 y z2 son objetos NumeroComplejo
    # La suma es (a+c) + (b+d)i
    nueva_a = z1.a + z2.a
    nueva_b = z1.b + z2.b
    # Creamos un NUEVO número complejo con el resultado
    return NumeroComplejo(nueva_a, nueva_b, modo='binomica')

# --- (Y aquí empieza la parte interactiva) ---

def mostrar_menu():
    """Función simple para no repetir el print() mil veces."""
    print("\n--- Calculadora de Complejos ---")
    print("Elige una opción:")
    print("  1. Sumar dos números")
    print("  2. Restar dos números")
    print("  ... (agrega las demás operaciones aquí)")
    print("  0. Salir")

def iniciar_calculadora():
    """Función principal que corre el programa."""
    
    while True:  # El bucle infinito del menú
        mostrar_menu()
        opcion = input("Tu elección: ")

        if opcion == '1':
            # --- SUMA ---
            print("\n== Suma de Complejos ==")
            print("Datos del PRIMER número (Z1):")
            # Pedimos los números y los convertimos a float
            a1 = float(input("  Parte Real (a): "))
            b1 = float(input("  Parte Imaginaria (b): "))
            
            print("Datos del SEGUNDO número (Z2):")
            a2 = float(input("  Parte Real (a): "))
            b2 = float(input("  Parte Imaginaria (b): "))
            
            # Usamos nuestra clase para crear los números
            z1 = NumeroComplejo(a1, b1, modo='binomica')
            z2 = NumeroComplejo(a2, b2, modo='binomica')
            
            # Llamamos a nuestra función de suma
            resultado = suma_compleja(z1, z2)
            
            # Mostramos el resultado en AMBAS formas (como pide el proyecto)
            print(f"\nResultado en Binómica: {resultado.mostrar_binomica()}")
            print(f"Resultado en Polar:    {resultado.mostrar_polar()}")

        elif opcion == '2':
            # --- RESTA ---
            print("\n== Resta de Complejos ==")
            # (Aquí iría el código para pedir los números de la resta)
            print("Función de resta no implementada... ¡todavía!")
            
        elif opcion == '0':
            # --- SALIR ---
            print("¡Adiós!")
            break  # Esta es la única forma de salir del while True
            
        else:
            # --- OPCIÓN INVÁLIDA ---
            print("Opción no válida. Intenta de nuevo.")

# --- Arrancamos el programa ---
iniciar_calculadora()