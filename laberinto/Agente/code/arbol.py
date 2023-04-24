import queue

son_queue = queue.Queue()

class Nodo:
    def __init__(self,inx,playermap,padre=None,profundidad = 0) :
        self.inx = inx
        self.padre = padre
        self.prof = profundidad
        self.hijos=[]
        self.playermap=playermap

def arbol_known(raiz,destino,mapp):
    global son_queue
    global mapeado 

    mapeado = mapp

    node_market(raiz.inx,raiz.playermap,destino,raiz)
    for hijo in raiz.hijos:
        print(hijo.inx)
    while not son_queue.empty():
        hijo = son_queue.get()
        node_market(hijo.inx,hijo.playermap,destino,hijo.padre)
    
    print("sin ruta")

def node_market(inx,playermap,destino,dad):
    global son_queue
    pos = inx[2]
    p1 = inx[0]
    p2 = inx[1]

    playermap = mapping(playermap,p1,p2)
    query = Move_query(playermap,inx)
    if p1 == destino[0] and p2==destino[1] :
        hijo = Nodo(inx,playermap,dad,dad.prof+1)
        dad.hijos.append(hijo)
        ruta(hijo)

    if query == 1:
        if p2 > 0 and playermap[p1][p2-1] != 0 and playermap[p1][p2-1] != 8 and pos !="left":
            ps = (p1,p2-1,"left")
            playermap[p1][p2] = mapeado[p1][p2]
            playermap[p1][p2-1] = 7
            node_market(ps,playermap,destino,dad)
        if p2<len(playermap[p1])-1 and playermap[p1][p2+1] != 0 and playermap[p1][p2+1] != 8 and pos !="right":
            ps = (p1,p2-1,"right")
            playermap[p1][p2] = mapeado[p1][p2]
            playermap[p1][p2+1] = 7
            node_market(ps,playermap,destino,dad)
        if p1 > 0 and playermap[p1-1][p2] != 0 and playermap[p1-1][p2] != 8 and pos !="up":
            ps = (p1-1,p2,"up")
            playermap[p1][p2] = mapeado[p1][p2]
            playermap[p1-1][p2] = 7
            node_market(ps,playermap,destino,dad)
        if p1 < len(playermap)-1 and playermap[p1+1][p2] != 0 and playermap[p1+1][p2] != 8 and pos !="down":
            ps = (p1+1,p2,"down")
            playermap[p1][p2] = mapeado[p1][p2]
            playermap[p1+1][p2] = 7
            node_market(ps,playermap,destino,dad)
    elif query == 0:
            hijo = Nodo(inx,playermap,dad,dad.prof+1)
            dad.hijos.append(hijo)
    else:
        if p2 > 0 and playermap[p1][p2-1] != 0 and playermap[p1][p2-1] != 8 and pos !="left":
            inx=(p1,p2-1,"left")
            hijo = next_node(inx,playermap,destino,dad)
            dad.hijos.append(hijo)
            print("nodo por la izq",hijo)
            son_queue.put(hijo)
        if p2<len(playermap[p1])-1 and playermap[p1][p2+1] != 0 and playermap[p1][p2+1] != 8 and pos !="right":
            inx=(p1,p2+1,"right")
            hijo = next_node(inx,playermap,destino,dad)
            dad.hijos.append(hijo)
            print("nodo por la der",hijo)
            son_queue.put(hijo)
        if p1 > 0 and playermap[p1-1][p2] != 0 and playermap[p1-1][p2] != 8 and pos !="up":
            inx=(p1-1,p2,"up")
            hijo = next_node(inx,playermap,destino,dad)
            dad.hijos.append(hijo)
            print("nodo por arr",hijo)
            son_queue.put(hijo)
        if p1 < len(playermap)-1 and playermap[p1+1][p2] != 0 and playermap[p1+1][p2] != 8 and pos !="down":
            inx=(p1+1,p2,"down")
            hijo = next_node(inx,playermap,destino,dad)
            dad.hijos.append(hijo)
            print("nodo por aba",hijo)
            son_queue.put(hijo)

def mapping (playerknown,row,col):

        if col > 0:
            if playerknown[row][col-1] == 9:
                 playerknown[row][col-1] = 9
            elif mapeado[row][col-1] != 0:
                playerknown[row][col-1] = mapeado[row][col-1]
            else :
                playerknown[row][col-1] = 8
        

        if col < len(mapeado[row]) - 1:
            if playerknown[row][col+1] == 9:
                 playerknown[row][col+1] = 9
            elif mapeado[row][col+1] != 0:
                playerknown[row][col+1] = mapeado[row][col+1]
            else :
                playerknown[row][col+1] = 8
           

        if row > 0:
            if playerknown[row-1][col] == 9:
                 playerknown[row-1][col] = 9
            elif mapeado[row-1][col] != 0:
                playerknown[row-1][col] = mapeado[row-1][col]
            else :
                playerknown[row-1][col] = 8
          

        if row < len(mapeado) - 1:
            if playerknown[row+1][col] == 9:
                 playerknown[row+1][col] = 9
            elif mapeado[row+1][col] != 0 :
                playerknown[row+1][col] = mapeado[row+1][col]
            else :
                playerknown[row+1][col] = 8
            

        #playerknown[row][col] = mapeado[row][col]
        

        return playerknown

def next_node(inx,playermap,destino,dad):
    global son_queue
    pos = inx[2]
    p1 = inx[0]
    p2 = inx[1]

    playermap = mapping(playermap,p1,p2)
    query = Move_query(playermap,inx)
    if p1 == destino[0] and p2==destino[1] :
        hijo = Nodo(inx,playermap,dad,dad.prof+1)
        dad.hijos.append(hijo)
        ruta(hijo)

    if query == 1:
        if p2 > 0 and playermap[p1][p2-1] != 0 and playermap[p1][p2-1] != 8 and pos !="left":
            ps = (p1,p2-1,"left")
            playermap[p1][p2] = mapeado[p1][p2]
            playermap[p1][p2-1] = 7
            return next_node(ps,playermap,destino,dad)
        if p2<len(playermap[p1])-1 and playermap[p1][p2+1] != 0 and playermap[p1][p2+1] != 8 and pos !="right":
            ps = (p1,p2-1,"right")
            playermap[p1][p2] = mapeado[p1][p2]
            playermap[p1][p2+1] = 7
            next_node(ps,playermap,destino,dad)
        if p1 > 0 and playermap[p1-1][p2] != 0 and playermap[p1-1][p2] != 8 and pos !="up":
            ps = (p1-1,p2,"up")
            playermap[p1][p2] = mapeado[p1][p2]
            playermap[p1-1][p2] = 7
            next_node(ps,playermap,destino,dad)
        if p1 < len(playermap)-1 and playermap[p1+1][p2] != 0 and playermap[p1+1][p2] != 8 and pos !="down":
            ps = (p1+1,p2,"down")
            playermap[p1][p2] = mapeado[p1][p2]
            playermap[p1+1][p2] = 7
            next_node(ps,playermap,destino,dad)
    elif query == 0:
            hijo = Nodo(inx,playermap,dad,dad.prof+1)
            return hijo
    else:
        hijo = Nodo(inx,playermap,dad,dad.prof+1)
        return hijo

def Move_query(playerknown,inx):
    cont = 0
    pos = inx[2]
    p1 = inx[0]
    p2 = inx[1] 

    if p2 > 0 and playerknown[p1][p2-1] != 0 and playerknown[p1][p2-1] != 8 and pos !="left":
        cont+=1
    if p2<len(playerknown[p1])-1 and playerknown[p1][p2+1] != 0 and playerknown[p1][p2+1] != 8 and pos !="right":
        cont+=1
    if p1 > 0 and playerknown[p1-1][p2] != 0 and playerknown[p1-1][p2] != 8 and pos !="up":
        cont+=1
    if p1 < len(playerknown)-1 and playerknown[p1+1][p2] != 0 and playerknown[p1+1][p2] != 8 and pos !="down":
        cont+=1
    return cont

def ruta(Rute):
    camino = []
    while Rute.padre != None :
        camino.append(Rute.posicion)
        Rute = Rute.padre
         
    for elemento in camino :
        print(elemento)

