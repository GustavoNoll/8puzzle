from pprint import pprint

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

def print_caminho(x,v):
    print('Achei')
             

def busca_largura(s):
    x = []
    F = [Estado(s,None,None,0)]
    
    while True:
        if not F:
            return False

        v = F.pop(0)

        if v.estado == '12345678_':
            print_caminho(x,v)
            break

        x.append(v)
        fronteira = expande(v)

        for estado in fronteira:
            F.append(estado)

def busca_profundidade(s):
    x = []
    F = [Estado(s,None,None,0)]
    
    while True:
        if not F:
            return False

        v = F.pop()

        if v.estado == '12345678_':
            print_caminho(x,v)
            break

        x.append(v)
        fronteira = expande(v)

        for estado in fronteira:
            F.append(estado)
        





estado='123456_78'
print(estado)
avalia_sucessor(estado)
avalia_expande(estado,0)

#busca_largura('2_3541687')
busca_largura('123_56478')
busca_profundidade('1234567_8')