## Node
Cada nodo tiene un value y una lista de hijos. Redefino el operador < (less than) con el metodo __lt__. Tiene un metodo Mostrar q sirve para mostrar arboles pero q m gustia fuera mas pijo. El metodo Find q le implemente es para trabajar con mas comodidad las operaciones que implican decrementar un nodo del Binomial Heap

## Binomial_Tree
Hay tres formas de construir un Binomial_Tree como se puede apreciar en su metodo __init__. Una de ellas es a partir de una lista de elementos, otra es a partir de la mezcla de dos binomial trees y la tercera estableciendo cual es el nodo de la cabecera. No controlo el tamanho de los arboles a ser mezclados porq dado el uso que le dare a la clase (Construir un Binomial_Heap), tendre en cuenta todo el tiempo esta peculiaridad
La construccion del Binomial_Tree a partir de una lista de elementos es realizada recursivamente.

Tambien redefino el less than y le agrego un metodo mostrar q no hace otra cosa sino llamar al Mostrar del nodo raiz

## Binomial_Heap
El __init__ del Binomial_Heap es igualmente recursivo, aunq hay una opcion para inicializarlo a partir d una lista de arboles q se establecera en el campo heads

Esta implementacion del binomial heap cuenta de un arreglo llamado heads que en la posicion i contiene el arbol binomial de grado i perteneciente al bosque del binomial heap, o en su defecto un valor -1

El metodo Merge va mergeando posicion a posicion los binomial trees de cada uno de los heaps involucrados. En cada iteracion del for no hago sino una separacion de casos para simular la suma como se haria la suma de dos numeros (con carry y all that stuff)

EL Metodo Mostrar muestra cada uno de los arboles del bosque del binomila heap. Cada arbol esta separado del otro usando una raya discontinua

