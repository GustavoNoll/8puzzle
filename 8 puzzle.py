class Estado:

    def __init__(self, estado, pai, ação, custo):
        self.estado = estado
        self.pai = pai
        self.ação = ação
        self.custo = custo
  
        
def sucessor(estado):
    estado_lista=string_to_list(estado)
    indice_buraco=estado.index('_')
    sucessores=[]
    ##ação esquerda
    if indice_buraco != 2 and indice_buraco != 5 and indice_buraco != 8:
        novo_estado=estado_lista.copy()
        temp=novo_estado[indice_buraco]
        novo_estado[indice_buraco]=novo_estado[indice_buraco+1]
        novo_estado[indice_buraco+1]=temp
        ação='esquerda', ''.join(novo_estado)
        sucessores.append(ação)
    ##ação cima
    if indice_buraco != 6 and indice_buraco != 7 and indice_buraco != 8:
        novo_estado=estado_lista.copy()
        temp=novo_estado[indice_buraco]
        novo_estado[indice_buraco]=novo_estado[indice_buraco+3]
        novo_estado[indice_buraco+3]=temp
        ação='cima', ''.join(novo_estado)
        sucessores.append(ação)
    ##ação baixo
    if indice_buraco != 0 and indice_buraco != 1 and indice_buraco != 2:
        novo_estado=estado_lista.copy()
        temp=novo_estado[indice_buraco]
        novo_estado[indice_buraco]=novo_estado[indice_buraco-3]
        novo_estado[indice_buraco-3]=temp
        ação='baixo', ''.join(novo_estado)
        sucessores.append(ação)
    ##ação direita
    if indice_buraco != 0 and indice_buraco != 3 and indice_buraco != 6:
        novo_estado=estado_lista.copy()
        temp=novo_estado[indice_buraco]
        novo_estado[indice_buraco]=novo_estado[indice_buraco-1]
        novo_estado[indice_buraco-1]=temp
        ação='direita', ''.join(novo_estado)
        sucessores.append(ação)
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
        print(f'({no.ação},{no.estado},{no.custo},{no.pai.estado})', end=' ')
    print()

def avalia_sucessor(estado):
    listaSucessores= sucessor(estado)
    for suc in listaSucessores:
        print(f'({suc[0]},{suc[1]})', end=' ')
    print()

estado='1234_5678'
avalia_sucessor(estado)
avalia_expande(estado,0)