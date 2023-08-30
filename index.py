import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Función para graficar varios vectores en la misma gráfica
def plot_vectors(vectors):

    fig, ax = plt.subplots()

    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    for i, vector in enumerate(vectors):
        x, y = vector
        color = colors[i % len(colors)]  # Ciclo de colores
        ax.quiver(0, 0, x, y, angles='xy', scale_units='xy', scale=1, color=color)

    # Establecer límites del eje
    max_x = max(vector[0] for vector in vectors)
    max_y = max(vector[1] for vector in vectors)
    ax.set_xlim(0, max_x + 1)
    ax.set_ylim(0, max_y + 1)

    # Etiquetas de los ejes
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

    # Título del gráfico
    ax.set_title('Graficador de Vectores')

    # Mostrar el gráfico
    plt.show()



def plot_vectors_3d(vectors):

    fig = plt.figure()


    ax = fig.add_subplot(111, projection='3d')

    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    for i, vector in enumerate(vectors):
        x, y, z = vector
        color = colors[i % len(colors)]
        ax.quiver(0, 0, 0, x, y, z, color=color)

    ax.set_xlim([0, x + 1])
    ax.set_ylim([0, y + 1])
    ax.set_zlim([0, z + 1])

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()

def add_vectors(vector1, vector2):
    return [vector1[i] + vector2[i] for i in range(len(vector1))]

def subtract_vectors(vector1, vector2):
    return [vector1[i] - vector2[i] for i in range(len(vector1))]

def scalar_multiply(vector, scalar):
    return [scalar * component for component in vector]

def dot_product(vector1, vector2):
    return sum(vector1[i] * vector2[i] for i in range(len(vector1)))

def main():
    num_vectors = int(input("Ingrese la cantidad de vectores: "))
    vectors = []  # Lista para almacenar los vectores

        
    dimension = int(input("Ingrese el número de dimensiones (2 o 3): "))
    if dimension not in (2, 3):
        print("Dimensiones no válidas. Debe ser 2 o 3.")
        return

    for i in range(num_vectors):
        print(f"Vector {i + 1}:")
        vector = []
        for j in range(dimension):
            component_label = chr(ord('X') + j)
            component = float(input(f"Ingrese el componente {component_label} del vector: "))
            vector.append(component)
        vectors.append(vector)

    tipo_operacion = int(input("Ingrese el tipo de operación que desea realizar:\n1. Suma de vectores.\n2. Resta de vectores.\n3. Producto escalar.\n4. Producto punto.\nOtro. Salir."))

    if tipo_operacion in (1, 2, 3, 4):
        vector_func = {1: add_vectors, 2: subtract_vectors, 3: scalar_multiply, 4: dot_product}
        if tipo_operacion == 3:
            scalar = float(input("Ingrese el valor del escalar: "))
            result = [vector_func[tipo_operacion](vector, scalar) for vector in vectors]
        elif tipo_operacion == 4 and len(vectors) == 2:
            result = vector_func[tipo_operacion](vectors[0], vectors[1])
        elif tipo_operacion == 1 or tipo_operacion == 2:
            if dimension == 2:
                result = vector_func[tipo_operacion](vectors[0], vectors[1])
            elif dimension == 3:
                if tipo_operacion == 1:
                    result = add_vectors(vectors[0], vectors[1])
                elif tipo_operacion == 2:
                    result = subtract_vectors(vectors[0], vectors[1])
        else:
            print("Operación no válida para los vectores proporcionados.")
            return

        print("Resultado de la operación:", result)

        if dimension == 2:
            print("Vectores originales:", vectors)
            plot_vectors(vectors + [result])
        elif dimension == 3:
            print("Vectores originales:", vectors)
            plot_vectors_3d(vectors + [result])

    else:
        print("Operación no válida.")

if __name__ == "__main__":
    main()



