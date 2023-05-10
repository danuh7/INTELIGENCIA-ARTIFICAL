#mapa de colores 
import pygame
import time
import star

def mapeado(mapeado, row, col, cell_size):
    if col > 0:
        if playerknown[row][col-1] == 9:
             playerknown[row][col-1] = 9
        elif mapeado[row][col-1] != 0:
            playerknown[row][col-1] = mapeado[row][col-1]
        else :
            playerknown[row][col-1] = 8
        recolor(playerknown, row, col-1, cell_size)

    if col < len(mapeado[row]) - 1:
        if playerknown[row][col+1] == 9:
             playerknown[row][col+1] = 9
        elif mapeado[row][col+1] != 0:
            playerknown[row][col+1] = mapeado[row][col+1]
        else :
            playerknown[row][col+1] = 8
        recolor(playerknown, row, col+1, cell_size)

    if row > 0:
        if playerknown[row-1][col] == 9:
             playerknown[row-1][col] = 9
        elif mapeado[row-1][col] != 0:
            playerknown[row-1][col] = mapeado[row-1][col]
        else :
            playerknown[row-1][col] = 8
        recolor(playerknown, row-1, col, cell_size)

    if row < len(mapeado) - 1:
        if playerknown[row+1][col] == 9:
             playerknown[row+1][col] = 9
        elif mapeado[row+1][col] != 0 :
            playerknown[row+1][col] = mapeado[row+1][col]
        else :
            playerknown[row+1][col] = 8
        recolor(playerknown, row+1, col, cell_size)

    playerknown[row][col] = mapeado[row][col]
    recolor(playerknown, row, col, cell_size)

    return playerknown

def recolor(playerknown,row,col,cell_size):
    x = col * cell_size
    y = row * cell_size
    if   playerknown[row][col] == 0:
            pygame.draw.rect(screen, BLACK, (x, y, cell_size, cell_size))
    elif playerknown[row][col] == 1:
            pygame.draw.rect(screen, WHITE, (x, y, cell_size, cell_size))
    elif playerknown[row][col] == 2:
            pygame.draw.rect(screen, GRAY, (x, y, cell_size, cell_size))
    elif playerknown[row][col] == 3:
            pygame.draw.rect(screen, LAND, (x, y, cell_size, cell_size))
    elif playerknown[row][col] == 4:
            pygame.draw.rect(screen, BLUE, (x, y, cell_size, cell_size))
    elif playerknown[row][col] == 5:
            pygame.draw.rect(screen, YELLOW, (x, y, cell_size, cell_size))
    elif playerknown[row][col] == 6:
            pygame.draw.rect(screen, GREEN, (x, y, cell_size, cell_size))
    elif playerknown[row][col] == 8:
            pygame.draw.rect(screen, KNOWN, (x, y, cell_size, cell_size))
    elif playerknown[row][col] == 9:
            pygame.draw.rect(screen, GOAL, (x, y, cell_size, cell_size))
    elif playerknown[row][col] == 10:
            pygame.draw.rect(screen, FINISH, (x, y, cell_size, cell_size))

def recargar(playerknown,matriz,playerlocation):
    # Calculamos el tamaño de cada celda
    cell_size = min(WINDOW_SIZE) // max(len(matriz), len(matriz[0]))

    # Creamos el laberinto
    for row in range(len(playerknown)):
        for col in range(len(playerknown[row])):
            x = col * cell_size
            y = row * cell_size

            if playerlocation[row][col] == 7:
                playerknown = mapeado(matriz,row,col,cell_size)
                pygame.draw.rect(screen, PLAYER, (x, y, cell_size, cell_size))
            else:
                recolor(playerknown,row,col,cell_size)

    # Actualizamos la pantalla
    pygame.display.update()

def meta(p1,p2,k1,k2):
    playerknown[p1][p2] = 10
    recargar(playerknown,matriz,playerlocation)
    pygame.display.update()
    Texto_Exito= pygame.font.SysFont("Arial",25).render("ha llegado a la meta",True,(91,186,200))
    screen.blit(Texto_Exito, (50,50))

class Agente:
     def __init__(self) -> None:
          self.tipo
          self.posicion
          
# Definimos el tamaño de la ventana
# WINDOW_SIZE = (580, 580)
# Definimos los colores

BLACK = (0, 0, 0) #0
WHITE = (255, 255, 255)#1
GRAY = (96, 96, 96)#2
LAND = (255, 229, 209)#3
BLUE = (51, 153, 255)#4
YELLOW = (255, 153, 51)#5
GREEN = (0, 153, 0)#6
PLAYER = (220,20,60)#7
KNOWN = (18,8,23)#8
GOAL = (198,83,98)#9
FINISH = (214,133,160)#10

cost = [
     [0,1,2,3,4],
     [0,4,1,0,3],
]

# Leemos el archivo de texto con la matriz de números
with open("./Agente/txt/map1.txt", "r") as file:
    matriz = [list(map(int, line.split())) for line in file]
n_filas, n_columnas = len(matriz), len(matriz[0])

playerlocation = [[0 for j in range(n_columnas)] for i in range(n_filas)]
playerknown = [[0 for j in range(n_columnas)] for i in range(n_filas)]

for i in range(len(playerknown)):
    for j in range(len(playerknown[i])):
        playerknown[i][j] = 0
p1 = 1
p2 = 4
k1 = 14
k2 = 4
playerlocation[p1][p2] = 7
playerknown[p1][p2] = 7
playerknown[k1][k2] = 9

origen = (p1,p2,"none")
destino = (k1,k2)

raiz = Nodo(origen,playerknown)

arbol_known(raiz,destino,matriz)

"""
# Inicializamos Pygame
pygame.init()
# Creamos la ventana
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Laberinto")


recargar(playerknown,matriz,playerlocation)
time.sleep(.5)


#CONTROLAR ELEMENTO POR TECLADO.
while True:
    for event in pygame. event.get () :
         if event.type == pygame.QUIT:
            pygame.quit ()
            quit()

    keys = pygame.key.get_pressed()
    
    recargar(playerknown,matriz,playerlocation)


    #if selector == 1:
    # Si se presiona la flecha izquierda, imprimir un mensaje
    if keys[pygame.K_LEFT]:
        if p2 > 0 and playerknown[p1][p2-1] != 0 and playerknown[p1][p2-1] != 8:
            playerlocation[p1][p2] = matriz[p1][p2]
            p2=p2-1
            playerlocation[p1][p2] = 7
            pygame.time.delay(200)
        else:
         pygame.time.delay(100)
    if keys[pygame.K_RIGHT]:
        if p2<len(playerlocation[p1])-1 and playerknown[p1][p2+1] != 0 and playerknown[p1][p2+1] != 8:
            playerlocation[p1][p2] = matriz[p1][p2]
            p2+=1
            playerlocation[p1][p2] = 7
            pygame.time.delay(200)
        else:
         pygame.time.delay(100)
    if keys[pygame.K_UP]:
        if p1 > 0 and playerknown[p1-1][p2] != 0 and playerknown[p1-1][p2] != 8:
            playerlocation[p1][p2] = matriz[p1][p2]
            p1-=1
            playerlocation[p1][p2] = 7
            pygame.time.delay(200)
        else:
         pygame.time.delay(100)
    if keys[pygame.K_DOWN]:
        if p1 < len(playerlocation)-1 and playerknown[p1+1][p2] != 0 and playerknown[p1+1][p2] != 8:
            playerlocation[p1][p2] = matriz[p1][p2]
            p1+=1
            playerlocation[p1][p2] = 7
            pygame.time.delay(200)
        else:
         pygame.time.delay(100)
    
    if p1 == k1 and p2 == k2:
        meta(p1,p2,k1,k2)

    pygame.display.update()
"""