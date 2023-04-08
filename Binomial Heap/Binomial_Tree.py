import Node
class Binomial_Tree:
    #El cabron d python no admite dos constructores
    def __init__(self, elementos, tipo = 0):
        if tipo == 0:
            n = len(elementos)
            if(n == 1):
                self.head = Node.Node(elementos[0])
            else:
                izq = Binomial_Tree(elementos[: n//2])
                der = Binomial_Tree(elementos[n//2 :])
                self.head = (Binomial_Tree([izq, der], True)).head
        if tipo == 1:
            if elementos[0] < elementos[1]:
                elementos[0].head.Add_Child(elementos[1].head)
                #elementos[1].head.padre = elementos[0].head
                self.head = elementos[0].head
            else:
                elementos[1].head.Add_Child(elementos[0].head)
                #elementos[0].head.padre = elementos[1].head
                self.head = elementos[1].head
        if tipo == 2:
            self.head = elementos[0]
    def __lt__(self, other):
        return self.head < other.head
    def Mostrar(self):
        self.head.Mostrar("")