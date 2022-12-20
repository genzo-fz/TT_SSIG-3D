# BIBLIOTECA Vectors
# Contiene funciones para realizar operaciones con Vectores

# Bibliotecas
from decimal import MAX_EMAX
import matplotlib.pyplot as plt
import numpy as np

# Lista de colores para asignar a los Vectores
colors = ['red', 'green', 'blue', 'orange', 'violet', '#94d', '#740', '#0f0', '#f0f', '#0ff', '#00a', '#28f', '#f44', '#245']
    
# ====================================================================================
# FUNCION Add
# Realiza la Suma entre dos Vectores
# RECIBE: 2 vectores
# DEVUELVE: Un vector Resultado
def Add(a, b):
    return np.add(a, b)


# ====================================================================================
# FUNCION Subtract
# Realiza la Resta entre dos Vectores
# RECIBE: 2 vectores
# DEVUELVE: Un vector Resultado
def Subtract(a, b):
    return np.subtract(a, b)


# ====================================================================================
# FUNCION Multiply
# Realiza la Multiplicacion entre dos Vectores
# RECIBE: 2 vectores
# DEVUELVE: Un vector Resultado
def Multiply(a, b):
    return np.multiply(a, b)


# ====================================================================================
# FUNCION CrossProduct
# Realiza el Producto Cruz entre dos Vectores
# RECIBE: 2 vectores
# DEVUELVE: Un vector Resultado
def CrossProduct(a, b):
    return np.cross(a, b)

'''
    vector = list(vectorList.values())
    resultado = vector[0]
    
    for x in range(1, len(vectorList)):
        resultado = np.cross(resultado, vector[x])
    
    return resultado
'''

# ====================================================================================
# FUNCION DotProduct
# Realiza el Producto Punto entre dos Vectores, o entre un Vector y un Escalar
# RECIBE: 2 vectores, o 1 vector y 1 escalar
# DEVUELVE: 
# -> En el caso de ser entre dos vectores: Un valor entero u flotante con el resultado 
#    del Producto Punto
# -> En el caso de ser entre un vector y un escalar: Un vector resultado
def DotProduct(a, b):
    return np.dot(a,b)


# ====================================================================================
# FUNCION Graph
# Genera el ambiente grafico 3D donde se graficaran los vectores generados, asi
# como tambien los vectores en cuestion
def Graph(vectorList, compVectors = 0):
    # Configuracion del tamanio de la pantalla de Graficacion
    fig = plt.figure()
    fig.set_figwidth(7.5)   # Ancho de la pantalla
    fig.set_figheight(6.5)  # Altura de la pantalla
    
    # Configuracion de los ejes que se mostraran en la Grafica
    global ax
    ax = plt.axes(projection = '3d')
    # Etiquetas para cada eje
    ax.xaxis.set_label_text('x', color = 'b')
    ax.yaxis.set_label_text('y', color = 'b')
    ax.zaxis.set_label_text('z', color = 'b')
      
    
    vector = list(vectorList.values())
    labels = list(vectorList.keys())
    
    GraphLimitDefinition(ax, vector)
    GraphVectors(ax, vector, labels, compVectors)
     
    # Impresion de la Leyenda
    plt.legend()
    
    # Muestra la pantalla y la Grafica en cuestion
    plt.show()
    

# ====================================================================================
# FUNCION GraphLimitDefinition
# Genera el ambiente grafico 3D donde se graficaran los vectores generados, asi
# como tambien los vectores en cuestion
def GraphLimitDefinition(ax, vector):
    # Se establece como valor inicial de los limites de cada eje, el primer punto de cada eje
    # de la Grafica, enlistado en la lista de Vectores
    max_axis_x = min_axis_x = vector[0][0]
    max_axis_y = min_axis_y = vector[0][1]
    max_axis_z = min_axis_z = vector[0][2]
    
    # Se obtienen los puntos maximos y minimos de cada eje de la Grafica, recorriendo cada uno
    # de los ejes enlistados en la lista de Vectores
    for x in range(1, len(vector)):
        max_axis_x = max(max_axis_x, vector[x][0])
        max_axis_y = max(max_axis_y, vector[x][1])
        max_axis_z = max(max_axis_z, vector[x][2])
        min_axis_x = min(min_axis_x, vector[x][0])
        min_axis_y = min(min_axis_y, vector[x][1])
        min_axis_z = min(min_axis_z, vector[x][2])
    
    # En caso de que el minimo sea un num positivo, se reduce a 0, para que asi las lineas siempre
    # se grafiquen desde el eje 0
    min_axis_x = min(min_axis_x, 0)
    min_axis_y = min(min_axis_y, 0)
    min_axis_z = min(min_axis_z, 0)
    
    # Establecimiento de los limites de cada eje (Punto max y min de cada eje de la Grafica
    # que sera mostrada al momento de esta ejecutarse, y sin aplicar zoom)
    print(ax.set_xlim([min_axis_x, max_axis_x]))
    print(ax.set_ylim([min_axis_y, max_axis_y]))
    print(ax.set_zlim([min_axis_z, max_axis_z]))
    
    # Definicion de los ejes x, y, z que se marcaran para definir la grafica
    ax.plot((min_axis_x, max_axis_x), (0, 0), (0, 0), color="grey")
    ax.plot((0, 0), (min_axis_y, max_axis_y), color="grey")
    ax.plot((0, 0), (0, 0), (min_axis_z, max_axis_z), color="grey") 


# ====================================================================================
# FUNCION GraphVectors
# Realiza la graficacion de los Vectores en la Grafica generada
def GraphVectors(ax, vector, labels, compVectors):
    # Se realiza la graficacion de cada uno de los vectores
    for x in range(len(vector)):
        ax.quiver(0, 0, 0, vector[x][0], vector[x][1], vector[x][2], color = colors[x], label = labels[x], arrow_length_ratio=0.1)
    
    ## GRAFICACION DE VECTORES COMPLEMENTARIOS PARA LA SUMA DE VECTORES
    if compVectors == 1:
        init_x = vector[0][0]
        init_y = vector[0][1]
        init_z = vector[0][2]
        
        for x in range(len(vector) - 2):
            end_x = vector[x + 1][0]
            end_y = vector[x + 1][1]
            end_z = vector[x + 1][2]
            
            ax.quiver(init_x, init_y, init_z, end_x, end_y, end_z, color = colors[x+1], label = labels[x+1] + "*", arrow_length_ratio=0.1, linestyle = '--')
            
            init_x = init_x + end_x
            init_y = init_y + end_y
            init_z = init_z + end_z
