import math
import matplotlib.pyplot as plt

# --- (Clase NumeroComplejo) ---
class NumeroComplejo:
    def __init__(self, valor1, valor2, modo='binomica'):
        """
        Inicializa el número complejo.
        modo='binomica': valor1=a, valor2=b
        modo='polar':    valor1=r, valor2=theta (en radianes)
        """
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
        # Maneja el signo para una impresión limpia
        if self.b < 0:
            return f"{self.a:.4f} - {abs(self.b):.4f}i"
        else:
            return f"{self.a:.4f} + {self.b:.4f}i"

    def mostrar_polar(self):
        # Muestra el ángulo en grados, que es más legible
        grados = math.degrees(self.theta)
        return f"{self.r:.4f} * (cos({grados:.4f}°) + i*sin({grados:.4f}°))"

# --- Funciones de Operaciones  ---

def suma_compleja(z1, z2):
    # Suma en forma binómica: (a+c) + (b+d)i
    nueva_a = z1.a + z2.a
    nueva_b = z1.b + z2.b
    return NumeroComplejo(nueva_a, nueva_b, modo='binomica')

def resta_compleja(z1, z2):
    # Resta en forma binómica: (a-c) + (b-d)i
    nueva_a = z1.a - z2.a
    nueva_b = z1.b - z2.b
    return NumeroComplejo(nueva_a, nueva_b, modo='binomica')

def multiplicacion_compleja(z1, z2):
    # Multiplicación en forma polar: (r1*r2, theta1+theta2)
    nuevo_r = z1.r * z2.r
    nuevo_theta = z1.theta + z2.theta
    return NumeroComplejo(nuevo_r, nuevo_theta, modo='polar')

def division_compleja(z1, z2):
    # Chequeo de división por cero
    if z2.r == 0:
        print("Error: División por cero.")
        return None
    # División en forma polar: (r1/r2, theta1-theta2)
    nuevo_r = z1.r / z2.r
    nuevo_theta = z1.theta - z2.theta
    return NumeroComplejo(nuevo_r, nuevo_theta, modo='polar')

def potencia_compleja(z, n):
    # Potencia (De Moivre): z^n = r^n * (cos(n*theta) + i*sin(n*theta))
    nuevo_r = z.r ** n
    nuevo_theta = z.theta * n
    return NumeroComplejo(nuevo_r, nuevo_theta, modo='polar')

def raiz_compleja(z, n):
    # Raíz n-ésima: Devuelve una LISTA de 'n' raíces
    if n <= 0:
        print("Error: 'n' debe ser un entero positivo.")
        return []
        
    raices = []
    nuevo_r = z.r ** (1/n) # La n-ésima raíz del módulo
    
    # Fórmula de De Moivre para raíces
    for k in range(n):
        # (theta + 2*pi*k) / n
        nuevo_theta = (z.theta + 2 * math.pi * k) / n
        raiz_k = NumeroComplejo(nuevo_r, nuevo_theta, modo='polar')
        raices.append(raiz_k)
    return raices

# --- Funciones de Interfaz (Ayudantes) ---

def pedir_numero_complejo():
    """
    Cumple el requisito  de recibir el número en cualquier forma.
    Devuelve un objeto NumeroComplejo.
    """
    while True:
        modo = input("  ¿Forma de entrada? (1-Binómica, 2-Polar): ")
        
        if modo == '1':
            try:
                a = float(input("    Parte Real (a): "))
                b = float(input("    Parte Imaginaria (b): "))
                return NumeroComplejo(a, b, modo='binomica')
            except ValueError:
                print("Error: Ingresa solo números.")
                
        elif modo == '2':
            try:
                r = float(input("    Módulo (r): "))
                # Pedimos en grados por facilidad, convertimos a radianes
                theta_grados = float(input("    Argumento (theta en grados): "))
                theta_rad = math.radians(theta_grados)
                return NumeroComplejo(r, theta_rad, modo='polar')
            except ValueError:
                print("Error: Ingresa solo números.")
                
        else:
            print("Opción no válida. Intenta de nuevo.")

def graficar_complejos(lista_z, titulo="Resultado en Plano de Argand"):
    """
    Grafica una lista de números complejos en el plano de Argand.
    """
    plt.figure(figsize=(7, 7))
    ax = plt.gca() # Get current axes

    lim_max = 0 # Para ajustar los límites del gráfico

    # Dibuja cada número en la lista
    for z in lista_z:
        a, b = z.a, z.b
        # Actualiza el límite máximo para escalar el gráfico
        lim_max = max(lim_max, abs(a), abs(b))
        
        # Dibuja el vector (flecha)
        
        ax.arrow(0, 0, a, b, head_width=0.1, head_length=0.1, fc='blue', ec='blue', length_includes_head=True)
        # Dibuja el punto final
        ax.plot(a, b, 'bo') # 'bo' = blue dot
        # Añade una etiqueta
        ax.text(a * 1.1, b * 1.1, f"{z.mostrar_binomica()}", fontsize=9)

    if lim_max == 0: lim_max = 5 # Evitar un gráfico colapsado si el resultado es 0
    
    lim_max = lim_max * 1.5 # Añade un 50% de margen
    
    ax.set_xlim([-lim_max, lim_max])
    ax.set_ylim([-lim_max, lim_max])
    
    # Pone los ejes X e Y en el origen (0,0)
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    
    ax.set_xlabel("Eje Real", loc='right')
    ax.set_ylabel("Eje Imaginario", loc='top')
    ax.set_title(titulo)
    plt.grid(True)
    plt.show() # Muestra la gráfica


def mostrar_menu():
    """Función simple para no repetir el print() mil veces. [cite: 11]"""
    print("\n--- Calculadora de Complejos (UNAM FI) ---")
    print("Elige una opción:")
    print("  1. Sumar (Z1 + Z2)")
    print("  2. Restar (Z1 - Z2)")
    print("  3. Multiplicar (Z1 * Z2)")
    print("  4. Dividir (Z1 / Z2)")
    print("  5. Potencia (Z^n)")
    print("  6. Raíz n-ésima (Z^(1/n))")
    print("  0. Salir")

def iniciar_calculadora():
    """Función principal que corre el programa."""
    
    while True:  # El bucle infinito del menú
        mostrar_menu()
        opcion = input("Tu elección: ")

        # --- Opciones que usan DOS números (Z1 y Z2) ---
        if opcion in ['1', '2', '3', '4']:
            print("\nDatos del PRIMER número (Z1):")
            z1 = pedir_numero_complejo()
            print("Z1 ingresado:", z1.mostrar_binomica())
            
            print("\nDatos del SEGUNDO número (Z2):")
            z2 = pedir_numero_complejo()
            print("Z2 ingresado:", z2.mostrar_binomica())

            resultado = None
            if opcion == '1':
                print("\n== Suma de Complejos ==")
                resultado = suma_compleja(z1, z2)
            elif opcion == '2':
                print("\n== Resta de Complejos ==")
                resultado = resta_compleja(z1, z2)
            elif opcion == '3':
                print("\n== Multiplicación de Complejos ==")
                resultado = multiplicacion_compleja(z1, z2)
            elif opcion == '4':
                print("\n== División de Complejos ==")
                resultado = division_compleja(z1, z2)
            
            # Mostrar resultado si la operación fue exitosa
            if resultado:
                print(f"\nResultado en Binómica: {resultado.mostrar_binomica()}")
                print(f"Resultado en Polar:    {resultado.mostrar_polar()}")
                # Graficar el resultado único [cite: 16, 17]
                graficar_complejos([resultado], titulo=f"Resultado de {opcion}")

        # --- Opciones que usan UN número (Z) y un entero (n) ---
        elif opcion in ['5', '6']:
            print("\nDatos del número (Z):")
            z = pedir_numero_complejo()
            print("Z ingresado:", z.mostrar_binomica())
            
            try:
                n = int(input("  Ingresa el entero 'n': "))
            except ValueError:
                print("Error: 'n' debe ser un entero.")
                continue # Vuelve al inicio del bucle

            if opcion == '5':
                # --- POTENCIA ---
                print("\n== Potencia n-ésima ==")
                resultado = potencia_compleja(z, n)
                print(f"\nResultado en Binómica: {resultado.mostrar_binomica()}")
                print(f"Resultado en Polar:    {resultado.mostrar_polar()}")
                graficar_complejos([resultado], titulo=f"Resultado de Z^{n}")

            elif opcion == '6':
                # --- RAÍZ ---
                print("\n== Raíz n-ésima ==")
                raices = raiz_compleja(z, n)
                if raices:
                    print(f"\nSe encontraron {n} raíces:")
                    for i, raiz in enumerate(raices):
                        print(f"  k={i}:")
                        print(f"    Binómica: {raiz.mostrar_binomica()}")
                        print(f"    Polar:    {raiz.mostrar_polar()}")
                    # Graficar TODAS las raíces juntas
                    graficar_complejos(raices, titulo=f"Raíces {n}-ésimas de Z")

        elif opcion == '0':
            # --- SALIR ---
            print("¡Listo! No olvides hacer tu reporte. ¡Éxito!")
            break  # Rompe el bucle while True
            
        else:
            # --- OPCIÓN INVÁLIDA ---
            print("Opción no válida. Intenta de nuevo.")

# --- Arrancamos el programa ---
if __name__ == "__main__":
    iniciar_calculadora()