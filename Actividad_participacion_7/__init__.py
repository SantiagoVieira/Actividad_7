from Actividad import Elemento
from Actividad import Conjunto

# Caso de prueba 1
#elem1 = Elemento("Element 1")
#elem2 = Elemento("Element 2")

# Verificar que la igualdad funciona correctamente
#print(elem1 == elem2)

# Caso de prueba 2
#conjunto = Conjunto("Conjunto 1")
#elem = Elemento("Elemento 1")

#conjunto.agregar_elemento(elem)

# Verificar que el elemento se ha agregado correctamente al conjunto
#print(len(conjunto.elementos))
#print(conjunto.elementos[0].nombre)

# Caso de prueba 3
#conjunto1 = Conjunto("Conjunto 1")
#conjunto2 = Conjunto("Conjunto 2")

#elem1 = Elemento("Elemento 1")
#elem2 = Elemento("Elemento 2")
#elem3 = Elemento("Elemento 3")

# Agregar elementos a los conjuntos
#conjunto1.agregar_elemento(elem1)
#conjunto1.agregar_elemento(elem2)

#conjunto2.agregar_elemento(elem2)
#conjunto2.agregar_elemento(elem3)

# Realizar la unión
#conjunto1.unir(conjunto2)

# Verificar que la unión se ha realizado correctamente
#print(len(conjunto1.elementos))
#print(conjunto1.elementos[0].nombre)
#print(conjunto1.elementos[1].nombre)
#print(conjunto1.elementos[2].nombre)

conjunto1 = Conjunto("Conjunot 1")
conjunto2 = Conjunto("Conjunto 2")

elem1 = Elemento("Elemento 1")
elem2 = Elemento("Elemento 2")
elem3 = Elemento("Elemento 3")

# Agregar elementos a los conjuntos
conjunto1.agregar_elemento(elem1)
conjunto1.agregar_elemento(elem2)

conjunto2.agregar_elemento(elem2)
conjunto2.agregar_elemento(elem3)

# Realizar la intersección
conjunto3 = Conjunto.intersectar(conjunto1, conjunto2)

# Verificar que la intersección se ha realizado correctamente
print(len(conjunto3.elementos))
print(conjunto3.elementos[0].nombre)

