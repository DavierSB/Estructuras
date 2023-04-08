import random
class Node:
    def __init__(self, value, padre = -1):
        self.value = value
        self.hijos = []
        self.padre = -1
    def __lt__(self, other):
        return self.value < other.value
    def Add_Child(self, child):
        self.hijos.append(child)
        child.padre = self
    def Heapify_Up(self):
        if self.padre == -1:
            return
        while self.value < self.padre.value:
            if self.padre == -1:
                return
            padre = self.padre
            padre.hijos.remove(self)
            if padre.padre != -1:
                padre.padre.Add_Child(self)
                padre.padre.hijos.remove(padre)
                self.Add_Child(padre)
            else:
                self.Add_Child(padre)
                self.padre = -1
                return
    def Decrease_Key(self, new_value):
        if new_value > self.value:
            return
        self.value = new_value
        self.Heapify_Up()
    def Find(self, value):
        if self.value == value:
            return self
        for child in self.hijos:
            aux = child.Find(value)
            if aux != -1:
                return aux
        return -1
    def Mostrar(self, espacios):
        espacios = espacios + " "
        print(espacios + str(self.value) + '\n')
        for hijo in self.hijos:
            hijo.Mostrar(espacios)