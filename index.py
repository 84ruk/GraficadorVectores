import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Función para graficar varios vectores en la misma gráfica
def plot_vectors(vectors):
    fig, ax = plt.subplots()

    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    for i, vector in enumerate(vectors):
        x, y = vector[:2]
        color = colors[i % len(colors)]
        ax.quiver(0, 0, x, y, angles='xy', scale_units='xy', scale=1, color=color)

    max_x = max(vector[0] for vector in vectors for vector in vectors)
    max_y = max(vector[1] for vector in vectors for vector in vectors)
    ax.set_xlim(0, max_x + 1)
    ax.set_ylim(0, max_y + 1)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')

    ax.set_title('Graficador de Vectores')

    plt.show()


def plot_vectors_3d(vectors):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    max_values = [max(vector[i] for vector in vectors) for i in range(len(vectors[0]))]

    for i, vector in enumerate(vectors):
        x, y, z = vector[:3]
        color = colors[i % len(colors)]
        ax.quiver(0, 0, 0, x, y, z, color=color)

    ax.set_xlim([0, max_values[0] + 1])
    ax.set_ylim([0, max_values[1] + 1])
    ax.set_zlim([0, max_values[2] + 1])

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

def input_vector(dimension):
    vector = []
    for j in range(dimension):
        component_label = chr(ord('X') + j)
        component = float(input(f"Ingrese el componente {component_label} del vector: "))
        vector.append(component)
    return vector

def main():
    dimension = int(input("Ingrese el número de dimensiones (2 o 3): "))
    if dimension not in (2, 3):
        print("Dimensiones no válidas. Debe ser 2 o 3.")
        return

    while True:
        vector1 = input_vector(dimension)

        tipo_operacion = int(input("Ingrese el tipo de operación que desea realizar:\n1. Suma de vectores.\n2. Resta de vectores.\n3. Producto escalar.\n4. Producto punto.\n5. Salir."))

        if tipo_operacion in (1, 2, 3, 4):
            if tipo_operacion == 5:
                break 
            if tipo_operacion == 1 or tipo_operacion == 2 or tipo_operacion == 4:
                vector2 = input_vector(dimension)
            elif tipo_operacion == 3:
                scalar = float(input("Ingrese el valor del escalar: "))
            else:
                print("Operación no válida.")
                continue

            if tipo_operacion == 1:
                result = add_vectors(vector1, vector2)
            elif tipo_operacion == 2:
                result = subtract_vectors(vector1, vector2)
            elif tipo_operacion == 3:
                result = scalar_multiply(vector1, scalar)
            elif tipo_operacion == 4:
                result = dot_product(vector1, vector2)

            print("Resultado de la operación:", result)

            if dimension == 2:
                plot_vectors([vector1, vector2, result])
            elif dimension == 3:
                plot_vectors_3d([vector1, vector2, result])

            another_operation = input("¿Deseas ingresar otro vector y realizar otra operación? (S/N): ")
            if another_operation.upper() != "S":
                print("Saliendo del programa.")
                break

        else:
            print("Saliendo del programa.")
            break

if __name__ == "__main__":
    main()



