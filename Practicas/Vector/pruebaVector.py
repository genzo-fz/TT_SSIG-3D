# Pruebas de Funciones de Vector.py

# Bibliotecas
import matplotlib.pyplot as plt
import numpy as np
import Vector as v

# Definicion de Vectores de Pruebas

a = np.array([2, 3, 1])
b = np.array([0, 5, 4])
#c = np.array([3, 5, -7])
#d = np.array([2, -6, 4])
vectorList = {
    "a" : a,
    "b" : b#,
    #"c" : c,
    #"d" : d
}
'''
a = np.array([2, 2, 2])
b = np.array([0, 5, 0])
c = np.array([0, 1, -1])
vectorList = {
    "a" : a,
    "b" : b,
    "c" : c,
}
'''

vector = list(vectorList.values())
#list() sive para convertir los valores del diccionario en una lista ordenada


# Prueba de Funcion Add
resultado = vector[0]

for x in range(1, len(vectorList)):
    resultado = v.Subtract(resultado, vector[x])
    
vectorList["resultado"] = resultado

print(vectorList)
v.Graph(vectorList, 0)



# Prueba de Funcion CrossProduct
'''
resultado = vector[0]

for x in range(1, len(vectorList)):
    resultado = v.CrossProduct(resultado, vector[x])
    
vectorList["resultado"] = resultado

print(vectorList)
v.Graph(vectorList)
'''




# Prueba de Funcion Subtract
'''
resultado = v.Subtract(a,b)
print(resultado)
'''
'''
resultado = v.Subtract(b,a)
print(resultado)
'''


# Prueba de Funcion Multiply
'''
resultado = v.Multiply(a,b)
print(resultado)
'''


# Prueba de Funcion DotProduct
'''
# Multiplicacion entre vectores
resultado = v.DotProduct(a,b)
print(resultado)
'''
'''
# Multiplicacion Vector Escalar
resultado = v.DotProduct(2,b)
print(resultado)
'''