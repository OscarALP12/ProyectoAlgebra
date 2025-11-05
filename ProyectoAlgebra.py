import math

class NumeroComplejo:
    """
    Esta es nuestra plantilla. Cada "NumeroComplejo" que creemos
    guardará su parte real (a), imaginaria (b), módulo (r) y argumento (theta).
    """
    
    def __init__(self, valor1, valor2, modo='binomica'):
        """
        El "constructor". Se llama cada vez que creamos un número nuevo.
        Le decimos si estamos metiendo forma binómica (a, b) o polar (r, theta).
        """
        if modo == 'binomica':
            # Guardamos a y b
            self.a = valor1
            self.b = valor2
            
            # --- Calculamos la forma polar a partir de la binómica ---
            self.r = math.sqrt(self.a**2 + self.b**2)
            # Usamos atan2 porque maneja bien todos los cuadrantes (signos de a y b)
            self.theta = math.atan2(self.b, self.a) 
            
        elif modo == 'polar':
            # Guardamos r y theta (asumimos theta en radianes)
            self.r = valor1
            self.theta = valor2
            
            # --- Calculamos la forma binómica a partir de la polar ---
            self.a = self.r * math.cos(self.theta)
            self.b = self.r * math.sin(self.theta)
            
        else:
            print("Error: Modo no reconocido. Creando número 0.")
            self.a = 0
            self.b = 0
            self.r = 0
            self.theta = 0

    def mostrar_binomica(self):
        """
        Una función para imprimir el número bonito en forma binómica.
        """
        # Esto es para que no imprima "3 + -2i", sino "3 - 2i"
        if self.b < 0:
            return f"{self.a} - {abs(self.b)}i"
        else:
            return f"{self.a} + {self.b}i"

    def mostrar_polar(self):
        """
        Una función para imprimir el número bonito en forma polar.
        Convertimos los radianes a grados para que sea más fácil de leer.
        """
        grados = math.degrees(self.theta)
        # f"{self.r:.4f}" redondea a 4 decimales, por si salen números muy largos
        return f"{self.r:.4f} * (cos({grados:.4f}°) + i*sin({grados:.4f}°))"

# --- EJEMPLO DE CÓMO USARLO ---

# Creamos el número 3 + 4i dándole la forma binómica
z1 = NumeroComplejo(3, 4, modo='binomica')

# Creamos un número dándole su forma polar: r=2, theta=pi/2 (o 90°)
# (pi/2 es aprox 1.5708 radianes)
z2 = NumeroComplejo(2, 1.5708, modo='polar')


print(f"z1 en binómica: {z1.mostrar_binomica()}")
print(f"z1 en polar:    {z1.mostrar_polar()}")
print("---")
print(f"z2 en binómica: {z2.mostrar_binomica()}") # Debería dar algo como 0 + 2i
print(f"z2 en polar:    {z2.mostrar_polar()}")
