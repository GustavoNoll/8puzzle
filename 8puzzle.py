from math import floor
from collections import deque
import time
import sys


class Vertice:

    def __init__(self, estado, pai, acao, custo, f=0):
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.custo = custo
        self.f = f


class FilaPrioridade:

    def __init__(self):
        self.fila = []

    # Insere um elemento e faz o shiftup
    def insere(self, estado: Vertice):
        self.fila.append(estado)
        self.shiftup(len(self.fila)-1)
    
    # Troca dois elementos de lugar
    def troca(self, i1, i2):
        temp = self.fila[i1]
        self.fila[i1] = self.fila[i2]
        self.fila[i2] = temp

    # Retorna o f() do vertice
    def f(self, i):
        return self.fila[i].f

    # Testa fila vazia
    def vazia(self):
        if not self.fila:
            return True
        else:
            return False

    # Remove elemento
    def pop(self):
        # Fila vazia
        if not self.fila:
            return []

        # Fila unitária, retorna o único elemento
        if len(self.fila) == 1:
            return self.fila.pop()

        # Guardamos o primeiro elemento e o substituímos pelo último
        primeiro = self.fila[0]
        self.fila[0] = self.fila.pop()

        # ordenamos o heap e retornamos o elemento retirado
        self.minheapify(0)
        return primeiro

    # Reordena o heap
    def minheapify(self, i):
        # índices dos filhos esquerdo e direito
        fe = 2*i+1
        fd = 2*i+2
        tf = len(self.fila)  # tamanho da fila

        # procura o elemento com menor heurística
        if fe < tf and self.f(fe) < self.f(i):
            menor = fe
        else:
            menor = i
        if fd < tf and self.f(fd) < self.f(menor):
            menor = fd

        # continua recursivamente
        if menor != i:
            self.troca(i, menor)
            self.minheapify(menor)

    # Move um elemento até ficar no lugar correto do Heap
    def shiftup(self, i):
        while i != 0:
            pai = floor((i-1)/2)
            if self.f(pai) > self.f(i):
                self.troca(pai, i)
            i = pai


def sucessor(estado):
    estado_lista = string_to_list(estado)
    indice_buraco = estado.index('_')
    sucessores = []
    # acao direita
    if indice_buraco != 2 and indice_buraco != 5 and indice_buraco != 8:
        novo_estado = estado_lista.copy()
        temp = novo_estado[indice_buraco]
        novo_estado[indice_buraco] = novo_estado[indice_buraco+1]
        novo_estado[indice_buraco+1] = temp
        acao = 'direita', ''.join(novo_estado)
        sucessores.append(acao)
    # acao abaixo
    if indice_buraco != 6 and indice_buraco != 7 and indice_buraco != 8:
        novo_estado = estado_lista.copy()
        temp = novo_estado[indice_buraco]
        novo_estado[indice_buraco] = novo_estado[indice_buraco+3]
        novo_estado[indice_buraco+3] = temp
        acao = 'abaixo', ''.join(novo_estado)
        sucessores.append(acao)
    # acao acima
    if indice_buraco != 0 and indice_buraco != 1 and indice_buraco != 2:
        novo_estado = estado_lista.copy()
        temp = novo_estado[indice_buraco]
        novo_estado[indice_buraco] = novo_estado[indice_buraco-3]
        novo_estado[indice_buraco-3] = temp
        acao = 'acima', ''.join(novo_estado)
        sucessores.append(acao)
    # acao esquerda
    if indice_buraco != 0 and indice_buraco != 3 and indice_buraco != 6:
        novo_estado = estado_lista.copy()
        temp = novo_estado[indice_buraco]
        novo_estado[indice_buraco] = novo_estado[indice_buraco-1]
        novo_estado[indice_buraco-1] = temp
        acao = 'esquerda', ''.join(novo_estado)
        sucessores.append(acao)
    return sucessores


def string_to_list(estado):
    est = []
    for elemento in estado:
        est.append(str(elemento))
    return est


def expande(vertice):
    neighbors = []
    moves = []
    moves = sucessor(vertice.estado)
    for m in moves:
        neighbors.append(Vertice(m[1], vertice, m[0], vertice.custo + 1))
    return neighbors


def avalia_expande(estado, custo):
    teste = Vertice(estado, None, None, custo)
    listaExpandidos = expande(teste)
    for vertice in listaExpandidos:
        print(f'({vertice.acao},{vertice.estado},{vertice.custo},{vertice.pai.estado})', end=' ')
    print()


def avalia_sucessor(estado):
    listaSucessores = sucessor(estado)
    for suc in listaSucessores:
        print(f'({suc[0]},{suc[1]})', end=' ')
    print()


def print_caminho(vertice):
    caminho = deque()
    while vertice.custo != 0:
        caminho.append(vertice.acao)
        vertice = vertice.pai
    while caminho:
        print(caminho.pop(), end=' ')

# efetua a busca em largura
def busca_largura(s):
    tempo = time.time()
    x = deque([])
    F = deque([Vertice(s, None, None, 0)])
    visitados = set()
    found = False

    while not found:
        if not F:
            return False

        # popleft retira o primeiro elemento do deque, efetivamente agindo como fila
        vertice = F.popleft()
        
        if vertice.estado == '12345678_':
            print_caminho(vertice)
            #print(f'| custo: {vertice.custo} | tempo: {time.time() - tempo} s')
            found = True
        else:
            x.append(vertice)
            visitados.add(vertice.estado) # salva os estados visitados em um set
            for vizinho in expande(vertice):
                if vizinho.estado not in visitados: # só adiciona estados não visitados
                    F.append(vizinho)
                    visitados.add(vizinho.estado)


def busca_profundidade(s):
    tempo = time.time()
    x = deque([])
    F = deque([Vertice(s, None, None, 0)])
    visitados = set()
    found = False

    while not found:
        if not F:
            return False

        # pop retira o último elemento do deque, efetivamente agindo como pilha
        vertice = F.pop()
        
        if vertice.estado == '12345678_':
            print_caminho(vertice)
            #print(f'| custo: {vertice.custo} | tempo: {time.time() - tempo} s')
            found = True
        else:
            x.append(vertice)
            visitados.add(vertice.estado) #salva os estados visitados em um set
            for vizinho in expande(vertice):
                if vizinho.estado not in visitados: # só adiciona estados não visitados
                    F.append(vizinho)
                    visitados.add(vizinho.estado)


def busca_astar_h1(s):
    tempo = time.time()
    x = []
    F = FilaPrioridade()
    visitados = set()
    found = False
    
    F.insere(Vertice(s, None, None, 0, h1(s)))

    while not found:
        if F.vazia():
            return False

        # Aqui, pop é um métoto que retira o elemento com o menor f() do heap
        vertice = F.pop()

        if vertice.estado == '12345678_':
            print_caminho(vertice)
            #print(f'| custo: {vertice.custo} | tempo: {time.time() - tempo} s')
            found = True
        else:
            x.append(vertice)
            visitados.add(vertice.estado) #salva os estados visitados em um set
            for vizinho in expande(vertice):
                if vizinho.estado not in visitados: # só adiciona estados não visitados
                    vizinho.f = h1(vizinho.estado) + vizinho.custo
                    visitados.add(vizinho.estado)
                    F.insere(vizinho)


def busca_astar_h2(s):
    tempo = time.time()
    x = []
    F = FilaPrioridade()
    visitados = set()
    found = False
    
    F.insere(Vertice(s, None, None, 0, h2(s)))

    while not found:
        if F.vazia():
            return False

        # Aqui, pop é um métoto que retira o elemento com o menor f() do heap
        vertice = F.pop()

        if vertice.estado == '12345678_':
            print_caminho(vertice)
            #print(f'| custo: {vertice.custo} | tempo: {time.time() - tempo} s')
            found = True
        else:
            x.append(vertice)
            visitados.add(vertice.estado) #salva os estados visitados em um set
            for vizinho in expande(vertice):
                if vizinho.estado not in visitados: # só adiciona estados não visitados
                    vizinho.f = h2(vizinho.estado) + vizinho.custo
                    visitados.add(vizinho.estado)
                    F.insere(vizinho)


def h2(v):  # manhatan
    distance = 0
    goal = ['1', '2', '3', '4', '5', '6', '7', '8', '_']
    estado_lista = [[v[0], v[1], v[2]], [v[3], v[4], v[5]], [v[6], v[7], v[8]]]
    for i in range(3):
        for j in range(3):
            if estado_lista[i][j] != '_':
                a = int(goal.index(estado_lista[i][j])/3)
                b = int(goal.index(estado_lista[i][j]) % 3)
                distance += abs(i-a) + abs(j-b)
    return distance


def h1(v):  # hamming
    distance = 0
    goal = ['1', '2', '3', '4', '5', '6', '7', '8', '_']
    estado_lista = string_to_list(v)
    for i in range(9):
        if goal[i] != estado_lista[i] and estado_lista[i] != '_':
            distance += 1
    return distance


# Main

acao = sys.argv[1]

if acao == 's':
    avalia_sucessor(sys.argv[2])
elif acao == 'e': 
    avalia_expande(sys.argv[2], int(sys.argv[3]))
elif acao == 'bfs':
    busca_largura(sys.argv[2])
elif acao == 'dfs':
    busca_profundidade(sys.argv[2])
elif acao == 'h1':
    busca_astar_h1(sys.argv[2])
elif acao == 'h2':
    busca_astar_h2(sys.argv[2])