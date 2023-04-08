import Binomial_Tree
class Binomial_Heap:
    def __init__(self, elementos, tipo = 0):
        if tipo == 1:
            self.heads = elementos
            return
        n = len(elementos)
        if n == 1:
            self.heads = [Binomial_Tree.Binomial_Tree([elementos[0]]), -1]
            self.pos_del_min = 0
        else:
            izq = Binomial_Heap(elementos[: n//2])
            der = Binomial_Heap(elementos[n//2:])
            if len(izq.heads) <= len(der.heads):
                der.Merge(izq)
                self.heads = der.heads
                self.pos_del_min = der.pos_del_min
            else:
                izq.Merge(der)
                self.heads = izq.heads
                self.pos_del_min = izq.pos_del_min
    def Merge(self, other):
        carry = -1
        pos_del_min = -1
        def Actualizar_Min(pos):
            if self.heads[pos] != -1:
                if pos_del_min != -1:
                    if self.heads[pos].head < self.heads[pos_del_min].head:
                        self.pos_del_min = pos
                else:
                    if self.heads[pos].head != -1:
                        self.pos_del_min = pos
        for i in range(0, len(self.heads)):
            Actualizar_Min(i - 1)
            #Si ninguno d los dos sumandos tiene un tree de grado i
            if (self.heads[i] == -1) and ((i >= len(other.heads) or (other.heads[i] == -1))):
                self.heads[i] = carry
                carry = -1
                continue
                
            #Si solo self tiene un tree de grado i
            if (i >= len(other.heads)) or other.heads[i] == -1:
                if carry != -1:
                    carry = Binomial_Tree.Binomial_Tree([self.heads[i], carry], True)
                    self.heads[i] = -1
                continue
                
            #Si solo other tiene un tree de grado i
            if self.heads[i] == -1:
                if carry == -1:
                    self.heads[i] = other.heads[i]
                else:
                    carry = Binomial_Tree.Binomial_Tree([other.heads[i], carry], True)
                continue
            
            #Cuando los dos sumandos tienen un tree de grado i
            if carry == -1:
                carry = Binomial_Tree.Binomial_Tree([self.heads[i], other.heads[i]], True)
                self.heads[i] = -1
            else:
                carry = Binomial_Tree.Binomial_Tree([other.heads[i], carry], True)
        Actualizar_Min(len(self.heads) - 1)
        if self.heads[len(self.heads) - 1] != -1:
            self.heads.append(-1)
    def Insertar(self, elemento):
        aux = Binomial_Heap([elemento])
        self.Merge(aux)
    def Minimun(self):
        return self.heads[self.pos_del_min].head.value
    def Extract_Minimun(self):
        BT_aux = self.heads[self.pos_del_min]
        elementos = []
        for node in BT_aux.head.hijos:
            node.padre = -1
            elementos.append(Binomial_Tree.Binomial_Tree([node], 2))
        elementos.append(-1)
        self.heads[self.pos_del_min] = -1
        BH_aux = Binomial_Heap(elementos, 1)
        self.Merge(BH_aux)
    def Decrease_Key(self, node, new_value):
        node.Decrease_Key(new_value)
        for i in range(0, len(self.heads)):
            if self.heads[i] == -1:
                continue
            if self.heads[i].head.padre != -1:
                self.heads[i] = self.heads[i].head.padre
                while self.heads[i].padre != -1:
                    self.heads[i] = self.heads[i].padre
                self.heads[i] = Binomial_Tree.Binomial_Tree([self.heads[i]], 2)
    def Delete(self, node):
        node.Decrase_Key(self.Minimun() - 1)
        node.Heapify_Up()
        self.Extract_Minimun()
    def Find(self, value):
        for tree in self.heads:
            if tree == -1:
                continue
            aux = tree.head.Find(value)
            if aux != -1:
                return aux
        return -1
    def Mostrar(self):
        for heap in self.heads:
            if heap != -1:
                print("----------------------")
                heap.Mostrar()
        print("----------------------")