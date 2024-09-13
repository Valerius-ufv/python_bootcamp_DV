# Crear un perro y señalar su altura, peso, nombre, que ladre y una condicional de que si el perro está gordo o no entrenar o dormir

peso_ideal_max = 20 #Este valor puede cambiar dependiendo de la raza o tamaño del perro

# Definición de atributos del perro

class Perro:
    def __init__(self, nombre, altura, peso):
        self.nombre = nombre
        self.altura = altura
        self.peso = peso

def ladrar(self):
    print(f'{self.name} dice : SIIIIIIIII! ')

def mostrar_datos(self):
    print(f'Nombre: {self.nombre}')
    print(f'Altura: {self.altura}')
    print(f'Peso: {self.peso}')

def necesita_entrenamiento(self):
    if self.peso > peso_ideal_max:
        print(f'{self.nombre} Tiene sobrepeso, hay que ponerlo a entrenar.')
    else:
        print(f'{self.nombre} Esta en buena forma física. Enhorabuena.')

# Creando un objeto Perro
mi_Perro = Perro("Max", 40, 20)

# Mostrando los datos del perro
mi_Perro (mostrar_datos)

# Evaluando si necesita entrenamiento
mi_Perro.necesita_entrenamiento()
