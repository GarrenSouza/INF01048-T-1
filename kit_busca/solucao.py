OBJETIVO = "12345678_"


def swap(estado, i1, i2):
    estado = list(estado)
    estado[i1], estado[i2] = estado[i2], estado[i1]
    return ''.join(estado)

class Nodo:
    """
    Implemente a classe Nodo com os atributos descritos na funcao init
    """
    def __init__(self, estado, pai, acao, custo):
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.custo = custo
        """
        Inicializa o nodo com os atributos recebidos
        :param estado:str, representacao do estado do 8-puzzle
        :param pai:Nodo, referencia ao nodo pai, (None no caso do nó raiz)
        :param acao:str, acao a partir do pai que leva a este nodo (None no caso do nó raiz)
        :param custo:int, custo do caminho da raiz até este nó
        """

    def getCusto(self):
        return self.custo
    
    def getEstado(self):
        return self.estado

    def getPai(self):
        return self.pai

    def getAcao(self):
        return self.acao

    def caminho(self):
        caminho = []
        pai = self.getPai()
        while pai:
            caminho.insert(0, pai.getAcao())
            pai = pai.getPai()
        return caminho

    # def caminho(self):
    # l = [self.estado]
    # if(self.pai)
    #     l.append(self.pai._caminho(l))
    # return l

    # def _caminho(self, l):
    # l.append(self.estado)
    # if !self.pai:
    #     return l
    # else :
    #     pai._caminho(l)
    #     return l

def sucessor(estado):
    """
    Recebe um estado (string) e retorna uma lista de tuplas (ação,estado atingido)
    para cada ação possível no estado recebido.
    Tanto a ação quanto o estado atingido são strings também.
    :param estado:
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    sucessores = []
    pos_vazio = estado.find('_')

    if pos_vazio - 3 >= 0:
        sucessores.append(("acima", swap(estado, pos_vazio, pos_vazio - 3)))
    if pos_vazio + 3 < 9:
        sucessores.append(("abaixo", swap(estado, pos_vazio, pos_vazio + 3)))    
    if pos_vazio % 3 == 0:
        sucessores.append(("direita", swap(estado, pos_vazio, pos_vazio + 1)))
    elif pos_vazio % 3 == 1:
        sucessores.append(("direita", swap(estado, pos_vazio, pos_vazio + 1)))
        sucessores.append(("esquerda", swap(estado, pos_vazio, pos_vazio - 1)))
    elif pos_vazio % 3 == 2:
        sucessores.append(("esquerda", swap(estado, pos_vazio, pos_vazio - 1)))

    return sucessores

def expande(nodo):
    """
    Recebe um nodo (objeto da classe Nodo) e retorna um iterable de nodos.
    Cada nodo do iterable é contém um estado sucessor do nó recebido.
    :param nodo: objeto da classe Nodo
    :return:
    """

    return [Nodo(estado, nodo, acao, nodo.getCusto() + 1) for acao, estado  in sucessor(nodo.estado)]

def retiraBFS(F):
    return (F[0], F[1:])

def bfs(estado):
    """
    Recebe um estado (string), executa a busca em LARGURA e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """

    X = {}
    F = [Nodo(estado, None, None, 0)]

    while F:
        v, F = retiraBFS(F)
        if v.getEstado() == OBJETIVO:
            return v.caminho()
        if v.getEstado() not in X:
            X[v.getEstado()] = v
            F = F + expande(v)
    return None


def dfs(estado):
    """
    Recebe um estado (string), executa a busca em PROFUNDIDADE e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


def astar_hamming(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


def astar_manhattan(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

len(bfs("2_3541687")) == 23