from pprint import pprint\

class Estado:

    def __init__(self, estado, pai, acao, custo):
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.custo = custo
  
        
def sucessor(estado):
    estado_lista=string_to_list(estado)
    indice_buraco=estado.index('_')
    sucessores=[]
    ##acao direita
    if indice_buraco != 2 and indice_buraco != 5 and indice_buraco != 8:
        novo_estado=estado_lista.copy()
        temp=novo_estado[indice_buraco]
        novo_estado[indice_buraco]=novo_estado[indice_buraco+1]
        novo_estado[indice_buraco+1]=temp
        acao='direita', ''.join(novo_estado)
        sucessores.append(acao)
    ##acao abaixo
    if indice_buraco != 6 and indice_buraco != 7 and indice_buraco != 8:
        novo_estado=estado_lista.copy()
        temp=novo_estado[indice_buraco]
        novo_estado[indice_buraco]=novo_estado[indice_buraco+3]
        novo_estado[indice_buraco+3]=temp
        acao='abaixo', ''.join(novo_estado)
        sucessores.append(acao)
    ##acao acima
    if indice_buraco != 0 and indice_buraco != 1 and indice_buraco != 2:
        novo_estado=estado_lista.copy()
        temp=novo_estado[indice_buraco]
        novo_estado[indice_buraco]=novo_estado[indice_buraco-3]
        novo_estado[indice_buraco-3]=temp
        acao='acima', ''.join(novo_estado)
        sucessores.append(acao)
    ##acao esquerda
    if indice_buraco != 0 and indice_buraco != 3 and indice_buraco != 6:
        novo_estado=estado_lista.copy()
        temp=novo_estado[indice_buraco]
        novo_estado[indice_buraco]=novo_estado[indice_buraco-1]
        novo_estado[indice_buraco-1]=temp
        acao='esquerda', ''.join(novo_estado)
        sucessores.append(acao)
    return sucessores


def string_to_list(estado):
    est=[]
    for elemento in estado:
        est.append(str(elemento))
    return est

def expande(no):
    neighbors = []
    moves=[]
    moves=sucessor(no.estado)
    for m in moves:
    	neighbors.append(Estado(m[1], no, m[0], no.custo + 1))
    return neighbors


def avalia_expande(estado,custo):
    teste=Estado(estado,None,None,custo)
    listaExpandidos= expande(teste)
    for no in listaExpandidos:
        print(f'({no.acao},{no.estado},{no.custo},{no.pai.estado})', end=' ')
    print()

def avalia_sucessor(estado):
    listaSucessores= sucessor(estado)
    for suc in listaSucessores:
        print(f'({suc[0]},{suc[1]})', end=' ')
    print()

def print_caminho(v: Estado):
    if v.custo > 0:
        print_caminho(v.pai)
    if not v.acao == None:
        print(v.acao, end=' ')

def busca_largura(s):
    x = []
    F = [Estado(s,None,None,0)]
    found = False
    iter = 1

    while not found:
        if not F:
            return False

        v = F.pop(0)

        if v.estado == '12345678_':
            print_caminho(v)
            print("iterações: ", iter)
            found = True
        else:
            if not estado_visistado(v,x):
                x.append(v)
                for vizinho in expande(v):
                    if not estado_visistado(vizinho,x):
                        if not estado_visistado(vizinho,F):
                            F.append(vizinho)
                            iter += 1

def busca_profundidade(s):
    x = []
    F = [Estado(s,None,None,0)]
    found = False
    iter = 1

    while not found:
        if not F:
            return False     

        v = F.pop()

        if v.estado == '12345678_':
            print_caminho(v)
            print("iterações: ", iter)
            found = True
        else:
            if not estado_visistado(v,x):
                x.append(v)
                for vizinho in expande(v):
                    if not estado_visistado(vizinho,x):
                        if not estado_visistado(vizinho,F):
                            F.append(vizinho)
                            iter += 1


def h2(v): #manhatan
    distance = 0
    goal = ['1','2','3','4','5','6','7','8','_']
    estado_lista=[[v[0],v[1],v[2]],[v[3],v[4],v[5]],[v[6],v[7],v[8]]]
    for i in range(3):
        for j in range(3):
            if estado_lista[i][j]!= '_':
                a=int(goal.index(estado_lista[i][j])/3)
                b=int(goal.index(estado_lista[i][j])%3)
                distance+=abs(i-a) + abs(j-b)
    #print("{}".format(distance))
    return distance


def h1(v): #hamming
    distance = 0
    goal = ['1','2','3','4','5','6','7','8','_']
    estado_lista=string_to_list(v)
    for i in range(9):
        if goal[i] != estado_lista[i] and estado_lista[i]!= '_': distance += 1
    #print("{}".format(distance))
    return distance

def estado_visistado(estado, expandidos):
    for expandido in expandidos:
        if expandido.estado == estado.estado:
            return True
    return False


def imprime_estado(estado): 
    print('-------------------')
    print("e: " + estado.estado)
    if estado.acao == None:
        print("None")
    else:
        print(estado.acao)
    print("c: " + str(estado.custo))
    if estado.pai:
        print("p: " + estado.pai.estado)
    else:
        print("p: None")
    print('-------------------')

#estado='123456_78'
#print(estado)
#avalia_sucessor(estado)
#avalia_expande(estado,0)

#busca_largura('2_3541687')
#busca_largura('123_56478')
#busca_profundidade('2_3541687')
h2('5_4732816')
h1('5_4732816')
