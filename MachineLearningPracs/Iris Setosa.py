import numpy as np

def load_txt_file():
    file_path = input("Ingrese la ruta del archivo TXT: ")
    attribute_separator = input("Ingrese el separador de atributos: ")

    # Leer el archivo de texto y dividirlo en líneas
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Obtener el número de atributos y patrones
    num_attributes = len(lines[0].strip().split(attribute_separator))
    num_patterns = len(lines)

    # Crear una matriz para almacenar los atributos
    attribute_matrix = np.zeros((num_patterns, num_attributes), dtype=object)

    # Cargar los atributos en la matriz
    for i, line in enumerate(lines):
        attributes = line.strip().split(attribute_separator)
        attribute_matrix[i] = attributes

    # Analizar los atributos para determinar su tipo
    attribute_types = []
    for j in range(num_attributes):
        attribute_column = attribute_matrix[:, j]
        unique_values = np.unique(attribute_column)
        if len(unique_values) <= 10:  # Criterio para atributos cualitativos
            attribute_types.append("qualitative")
            categories = ", ".join(unique_values)
            print(f"Atributo {j + 1}: cualitativo ({categories})")
        else:
            attribute_types.append("quantitative")
            min_value = np.min(attribute_column.astype(float))
            max_value = np.max(attribute_column.astype(float))
            mean_value = np.mean(attribute_column.astype(float))
            print(f"Atributo {j + 1}: cuantitativo (min={min_value}, max={max_value}, media={mean_value})")

    # Elegir un subconjunto de atributos para generar un vector
    subset_indices = input("Ingrese los índices de los atributos separados por comas: ")
    subset_indices = [int(index.strip()) for index in subset_indices.split(",")]
    vector = attribute_matrix[:, subset_indices]
    print("Vector resultante:")
    print(vector)


# Ejecutar la función
load_txt_file()
