import Binomial_Heap
H = Binomial_Heap.Binomial_Heap([14, 4, 6, 13, 3, 12, 11, 8, 9, 15, 5, 1, 2, 7, 0, 10])
H.Mostrar()
H.Extract_Minimun()
print("Luego de la extraccion")
H.Mostrar()
H.Decrease_Key(H.Find(13), 0)
print("Luego de cambiar el valor de 13 a 0")
H.Mostrar()