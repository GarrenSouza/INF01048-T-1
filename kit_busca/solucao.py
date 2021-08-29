import heapq as hpq
import math

_OBJETIVO = "12345678_"


def swap(estado, i1, i2):
    estado = list(estado)
    estado[i1], estado[i2] = estado[i2], estado[i1]
    return ''.join(estado)

class Nodo:
    # __lt__, __gt__, __le__, __ge__, __eq__, and __ne__

    def __lt__(self, nodo):
        return self.get_custo() < nodo.get_custo()

    def __le__(self, nodo):
        return self.get_custo() <= nodo.get_custo()

    def __gt__(self, nodo):
        return self.get_custo() > nodo.get_custo()

    def __ge__(self, nodo):
        return self.get_custo() >= nodo.get_custo()

    def __eq__(self, nodo):
        return self.get_custo() == nodo.get_custo()

    def __ne__(self, nodo):
        return self.get_custo() != nodo.get_custo()

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

    def get_custo(self):
        return self.custo
    
    def get_estado(self):
        return self.estado

    def get_pai(self):
        return self.pai

    def get_acao(self):
        return self.acao

    def caminho(self):
        caminho = []
        pai = self.get_pai()
        while pai:
            caminho.insert(0, pai.get_acao())
            pai = pai.get_pai()
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

    return [Nodo(estado, nodo, acao, nodo.get_custo() + 1) for acao, estado  in sucessor(nodo.estado)]

def retira_BFS(F):
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
        [print(e.get_estado()) for e in X.values()]
        input()
        v, F = retira_BFS(F)
        if v.get_estado() == _OBJETIVO:
            return v.caminho()
        # print(v.get_estado())
        # print(X)
        # input()
        if v.get_estado() not in X:
            X[v.get_estado()] = v
            F = F + expande(v)
    return None

def retira_DFS(F):
    return (F[-1], F[:-1])

def dfs(estado):
    """
    Recebe um estado (string), executa a busca em PROFUNDIDADE e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """

    X = {}
    F = [Nodo(estado, None, None, 0)]

    while F:
        [print(e.get_estado()) for e in X.values()]
        input()
        v, F = retira_DFS(F)
        if v.get_estado() == _OBJETIVO:
            return v.caminho()
        if v.get_estado() not in X:
            X[v.get_estado()] = v
            F = F + expande(v)
    return None

def retira_astar(estado):
    return hpq.heappop(estado)

def get_hamming_distance(estado):
    return len([1 for i, e in enumerate(estado) if '12345678_'.find(e) != i])

def expande_astar_hamming(F, nodo):
    l = F + [Nodo(estado, nodo, acao, nodo.get_custo() + 1 + get_hamming_distance(estado)) for acao, estado  in sucessor(nodo.estado)]
    hpq.heapify(l)
    return l

def astar_hamming(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    """
    Recebe um estado (string), executa a busca em PROFUNDIDADE e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """

    X = {}
    F = [Nodo(estado, None, None, 0)]

    while F:
        v = retira_astar(F)
        if v.get_estado() == _OBJETIVO:
            return v.caminho()
        if v.get_estado() not in X:
            X[v.get_estado()] = v
            F = expande_astar_hamming(F, v)

    return None

def get_manhattan_distance(estado):
  distancia = 0.
  for i, e in enumerate(estado):
      x = i%3
      y = int(i/3)
      i_real = _OBJETIVO.find(e)
      x_real = i_real%3
      y_real = int(i_real/3)
      distancia = distancia + math.sqrt((x - x_real)**2 + (y - y_real)**2)
  return distancia

def expande_astar_manhattan(F, nodo):
    l = F + [Nodo(estado, nodo, acao, nodo.get_custo() + 1 + get_manhattan_distance(estado)) for acao, estado  in sucessor(nodo.estado)]
    hpq.heapify(l)
    return l
    
def astar_manhattan(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """

    X = {}
    F = [Nodo(estado, None, None, 0)]

    while F:
        v = retira_astar(F)
        if v.get_estado() == _OBJETIVO:
            return v.caminho()
        if v.get_estado() not in X:
            X[v.get_estado()] = v
            F = expande_astar_manhattan(F, v)

    return None

print(len(astar_manhattan("2_3541687")) == 23)