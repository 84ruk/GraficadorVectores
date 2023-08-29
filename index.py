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

def main():
    num_vectors = int(input("Ingrese la cantidad de vectores: "))
    vectors = []  # Lista para almacenar los vectores

        
    dimension = int(input("Ingrese el número de dimensiones (2 o 3): "))





    def add_vectors(vector1, vector2):
        return [vector1[0] + vector2[0], vector1[1] + vector2[1]]

    def subtract_vectors(vector1, vector2):
        return [vector1[0] - vector2[0], vector1[1] - vector2[1]]

    def scalar_multiply(vector, scalar):
        return [scalar * vector[0], scalar * vector[1]]

    def dot_product(vector1, vector2):
        return vector1[0] * vector2[0] + vector1[1] * vector2[1]

    

    

    if dimension == 2:

        # Pedir al usuario los componentes de cada vector
        for i in range(num_vectors):
            print(f"Vector {i + 1}:")
            vector_x = float(input("Ingrese el componente X del vector: "))
            vector_y = float(input("Ingrese el componente Y del vector: "))
            vectors.append([vector_x, vector_y])

        # Mostrar los vectores ingresados
        print("Vectores ingresados:")
        for i, vector in enumerate(vectors):
            print(f"Vector {i + 1}: {vector}")

        plot_vectors(vectors)
        
    elif dimension == 3:
                # Pedir al usuario los componentes de cada vector
        for i in range(num_vectors):
            print(f"Vector {i + 1}:")
            vector_x = float(input("Ingrese el componente X del vector: "))
            vector_y = float(input("Ingrese el componente Y del vector: "))
            vector_z = float(input("Ingrese el componente Z del vector: "))
            vectors.append([vector_x, vector_y, vector_z])
            
        # Mostrar los vectores ingresados
        print("Vectores ingresados:")
        for i, vector in enumerate(vectors):
            print(f"Vector {i + 1}: {vector}")

        plot_vectors_3d(vectors) 

    else:
        print("Dimensiones no válidas. Debe ser 2 o 3.")
        return

if __name__ == "__main__":
    main()



