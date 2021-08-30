from queue import Queue
from queue import PriorityQueue

_OBJETIVO = "12345678_"

def swap(estado, i1, i2):
    estado = list(estado)
    estado[i1], estado[i2] = estado[i2], estado[i1]
    return ''.join(estado)

class Nodo:
    
    def __lt__(self, nodo):
        return self.get_custo() < nodo.get_custo()
    
    def __init__(self, estado, pai, acao, custo):
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.custo = custo
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

def sucessor(estado):
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
    return [Nodo(estado, nodo, acao, nodo.get_custo() + 1) for acao, estado  in sucessor(nodo.estado)]

def bfs(estado):
    if not solucionavel(estado):
        return None
    X = {}
    F = Queue()
    F.put(Nodo(estado, None, None, 0))

    while not F.empty():
        v = F.get()
        if v.get_estado() == _OBJETIVO:
            return v.caminho()
        if v.get_estado() not in X:
            X[v.get_estado()] = v
            exp = expande(v)
            for e in exp:
              F.put(e)
    return None

def dfs(estado):
    if not solucionavel(estado):
        return None
    X = {}
    F = [Nodo(estado, None, None, 0)]

    while len(F) != 0:
        v = F.pop()
        if v.get_estado() == _OBJETIVO:
            return v.caminho()
        if v.get_estado() not in X:
            X[v.get_estado()] = v
            exp = expande(v)
            for e in exp:
                F.append(e)
    return None

def get_hamming_distance(estado):
    return len([1 for i, e in enumerate(estado) if '12345678_'.find(e) != i])

def astar_hamming(estado):
    if not solucionavel(estado):
        return None
    X = {}
    F = PriorityQueue()
    F.put((0, Nodo(estado, None, None, 0)))

    while not F.empty():
        v = F.get()[1]  # acessa o segundo elemento da tupla com menor custo
        if v.get_estado() == _OBJETIVO:
            return v.caminho()
        if v.get_estado() not in X:
            X[v.get_estado()] = v
            exp = expande(v)
            for e in exp:
                F.put((e.get_custo() + get_hamming_distance(e.get_estado()), e))
    return None

def get_manhattan_distance(estado):
  distancia = 0.
  for i, e in enumerate(estado):
      x = i%3
      y = int(i/3)
      i_real = _OBJETIVO.find(e)
      x_real = i_real%3
      y_real = int(i_real/3)
      distancia = distancia + abs(x - x_real) + abs(y - y_real)
  return distancia

def astar_manhattan(estado):
    if not solucionavel(estado):
        return None
    X = {}
    F = PriorityQueue()
    F.put((0, Nodo(estado, None, None, 0))) # cria um tupla custo - nodo

    while not F.empty():
        v = F.get()[1]  # acessa o segundo elemento da tupla com menor custo
        if v.get_estado() == _OBJETIVO:
            return v.caminho()
        if v.get_estado() not in X:
            X[v.get_estado()] = v
            exp = expande(v)
            for e in exp:
                F.put((e.get_custo() + get_manhattan_distance(e.get_estado()), e))
    return None

def solucionavel(estado):
  pos_vazio = estado.find('_')
  s = list(estado)
  s = s[:pos_vazio] + s[pos_vazio + 1:]
  inversoes = 0
  for i, num in enumerate(s):
    for num_precedente in s[:i]:
      if num_precedente < num:
        inversoes = inversoes + 1
  if inversoes%2 == 0:
    return True
  else:
    return False
