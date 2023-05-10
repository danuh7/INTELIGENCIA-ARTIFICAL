import heapq
import maze

# Definir los movimientos permitidos (arriba, abajo, izquierda, derecha y diagonales)
MOVIMIENTOS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def calcular_costo(punto_actual, punto_final, cost):
    """
    Calcula el costo heurístico entre dos puntos.
    Utilizamos la distancia Manhattan como heurística.
    """
    x1, y1 = punto_actual
    x2, y2 = punto_final
    return abs(x1 - x2) + abs(y1 - y2)

def encontrar_ruta(mapa, punto_inicial, punto_final, cost):
    """
    Encuentra la ruta con el menor costo utilizando el algoritmo A*.
    El mapa es una lista que indica el tipo de agente en cada casilla.
    La lista cost representa los costos de movimiento.
    """
    filas = len(mapa)
    columnas = len(mapa[0])

    # Verificar si el punto inicial y final están dentro de los límites del mapa
    if punto_inicial[0] < 0 or punto_inicial[0] >= filas or punto_inicial[1] < 0 or punto_inicial[1] >= columnas:
        raise ValueError("El punto inicial está fuera del mapa.")
    if punto_final[0] < 0 or punto_final[0] >= filas or punto_final[1] < 0 or punto_final[1] >= columnas:
        raise ValueError("El punto final está fuera del mapa.")

    # Crear una matriz para almacenar el costo acumulado de llegar a cada punto
    costo_acumulado = [[float('inf')] * columnas for _ in range(filas)]
    costo_acumulado[punto_inicial[0]][punto_inicial[1]] = 0

    # Crear una matriz para almacenar la ruta de cada punto anterior
    ruta_anterior = [[None] * columnas for _ in range(filas)]

    # Crear una cola de prioridad para almacenar los puntos a explorar
    cola_prioridad = []
    heapq.heappush(cola_prioridad, (0, punto_inicial))
    
    while cola_prioridad:
        punto_actual = heapq.heappop(cola_prioridad)[1]
    
        if punto_actual == punto_final:
            # Se encontró el punto final, reconstruir la ruta y retornarla
            ruta = []
            while punto_actual:
                ruta.append(punto_actual)
                punto_actual = ruta_anterior[punto_actual[0]][punto_actual[1]]
            ruta.reverse()
            return ruta
    
        for movimiento in MOVIMIENTOS:
            dx, dy = movimiento
            nuevo_x = punto_actual[0] + dx
            nuevo_y = punto_actual[1] + dy
    
            # Verificar si el nuevo punto está dentro de los límites del mapa
            if nuevo_x < 0 or nuevo_x >= filas or nuevo_y < 0 or nuevo_y >= columnas:
                continue
            
            tipo_agente = mapa[nuevo_x][nuevo_y]
            costo = cost[tipo_agente][movimiento]
    
            # Verificar si el costo asociado al nuevo tipo de agente y movimiento es válido (diferente de 0)
            # y si el costo acumulado es menor al costo acumulado previo para el nuevo punto
            if costo != 0 and costo_acumulado[punto_actual[0]][punto_actual[1]] + costo < costo_acumulado[nuevo_x][nuevo_y]:
                costo_acumulado[nuevo_x][nuevo_y] = costo_acumulado[punto_actual[0]][punto_actual[1]] + costo
                costo_total = costo_acumulado[nuevo_x][nuevo_y] + calcular_costo((nuevo_x, nuevo_y), punto_final, cost)
                heapq.heappush(cola_prioridad, (costo_total, (nuevo_x, nuevo_y)))
                ruta_anterior[nuevo_x][nuevo_y] = punto_actual
