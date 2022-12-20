import sys
from PyQt5 import uic, QtWidgets
#from PyQt5.QtGui import QMovie ## Para producir gifs


import sympy as sym ## Trabajo con los polinomios
import matplotlib.pyplot as plt ## Creación de gráficas
import numpy as np
import webbrowser as wb ## Abrir archivos

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas # Juntar matplotlib con las interfaces de Qt Designer
from sympy import * ## Operaciones con el polinomio (derivadas, integrales, sustituciones)
from matplotlib.animation import FuncAnimation #Animaciones de las gráficas

qtCreatorFile = "Practica01.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #------------- NUEVAS APLICACIONES EN LA INTERFAZ ---------------------------------------------------------#

        self.pushButton_cerrar.clicked.connect(self.cerrarVentana) # Función del botón cerrar.
        self.bt_insertarUsuario.clicked.connect(self.insertarUsuario) # Ingreso de Usuario.
        self.bt_grado.clicked.connect(self.obtenerGrado) # Obtener grado y constantes.
        self.bt_graficar.clicked.connect(self.graficacion) # Inicio de la graficación.
        self.pb_abrir_graf01.clicked.connect(self.ver_graf_01) # Abrir el gif de la gráfica de posiciones.
        self.pb_abrir_graf02.clicked.connect(self.ver_graf_02) # Abrir el gif de la gráfica de posiciones con vectores.
        self.pb_abrir_graf03.clicked.connect(self.ver_graf_03)  # Abrir el gif de la gráfica de velocidades.
        self.pb_abrir_graf04.clicked.connect(self.ver_graf_04)  # Abrir el gif de la gráfica de velocidades con vectores.
        self.pb_abrir_graf05.clicked.connect(self.ver_graf_05)  # Abrir el gif de la gráfica de aceleraciones.
        self.pb_abrir_graf06.clicked.connect(self.ver_graf_06)  # Abrir el gif de la gráfica de aceleraciones con vectores.

    #----------------- NUEVAS FUNCIONES ---------------------------------------------------------------------------#

    #-------- Función de cerrar----------------------------------------------
    def cerrarVentana(self):  
        quit()
    #-------- Función de cerrar (FIN) ---------------------------------------

    #-------- Función para Ingresar Usuario ---------------------------------
    def insertarUsuario(self):  ##
        usuario_nuevo = self.usuario.text()     # Tranforma el texto insertado en el espacio usuario_nuevo
        usuario_saludo = "Bienvenido " + usuario_nuevo + "."    
        self.saludo.setText(usuario_saludo)     # Inserta el texto en el espacio de saludo

        self.usuario.setEnabled(False)              #Para habilitar o deshabilitar los botones al avanzar en el proceso
        self.bt_insertarUsuario.setEnabled(False)
        self.spin_grado.setEnabled(True)
        self.bt_grado.setEnabled(True)
    #-------- Función para Ingresar Usuario (FIN) ---------------------------

    #-------- Función para el grado y las constantes ------------------------
    def obtenerGrado(self): 
        grado_poli = int(self.spin_grado.text())  # Toma el valor del boton spin_grado

        if grado_poli == 0:  # En caso de escoger un polinomio de grado 0
                self.spinBox_00.setEnabled(True)    # Habilita botones
                self.spinBox_01.setEnabled(False)
                self.spinBox_02.setEnabled(False)
                self.spinBox_03.setEnabled(False)
                self.spinBox_04.setEnabled(False)
                self.spinBox_05.setEnabled(False)
                self.spinBox_00.setMinimum(1)       # Pone un limite para los botones de las constantes
                self.spinBox_01.setMinimum(0)
                self.spinBox_02.setMinimum(0)
                self.spinBox_03.setMinimum(0)
                self.spinBox_04.setMinimum(0)
                self.spinBox_05.setMinimum(0)
                self.spinBox_01.setProperty("value", 0)     # Regresa los botones a sus valores de default (0)
                self.spinBox_02.setProperty("value", 0)
                self.spinBox_03.setProperty("value", 0)
                self.spinBox_04.setProperty("value", 0)
                self.spinBox_05.setProperty("value", 0)

        elif grado_poli == 1:  # En caso de escoger un polinomio de grado 1
                self.spinBox_00.setEnabled(True)    # Habilita botones
                self.spinBox_01.setEnabled(True)
                self.spinBox_02.setEnabled(False)
                self.spinBox_03.setEnabled(False)
                self.spinBox_04.setEnabled(False)
                self.spinBox_05.setEnabled(False)
                self.spinBox_00.setMinimum(0)       # Pone un limite para los botones de las constantes
                self.spinBox_01.setMinimum(1)
                self.spinBox_02.setMinimum(0)
                self.spinBox_03.setMinimum(0)
                self.spinBox_04.setMinimum(0)
                self.spinBox_05.setMinimum(0)
                self.spinBox_00.setProperty("value", 0)  # Regresa los botones a sus valores de default (0)
                self.spinBox_02.setProperty("value", 0)
                self.spinBox_03.setProperty("value", 0)
                self.spinBox_04.setProperty("value", 0)
                self.spinBox_05.setProperty("value", 0)


        elif grado_poli == 2:   # En caso de escoger un polinomio de grado 2
                self.spinBox_00.setEnabled(True)    # Habilita botones
                self.spinBox_01.setEnabled(True)
                self.spinBox_02.setEnabled(True)
                self.spinBox_03.setEnabled(False)
                self.spinBox_04.setEnabled(False)
                self.spinBox_05.setEnabled(False)
                self.spinBox_00.setMinimum(0)       # Pone un limite para los botones de las constantes
                self.spinBox_01.setMinimum(0)
                self.spinBox_02.setMinimum(1)
                self.spinBox_03.setMinimum(0)
                self.spinBox_04.setMinimum(0)
                self.spinBox_05.setMinimum(0)
                self.spinBox_00.setProperty("value", 0)     # Regresa los botones a sus valores de default (0)
                self.spinBox_01.setProperty("value", 0)
                self.spinBox_03.setProperty("value", 0)
                self.spinBox_04.setProperty("value", 0)
                self.spinBox_05.setProperty("value", 0)

        elif grado_poli == 3:    # En caso de escoger un polinomio de grado 3
                self.spinBox_00.setEnabled(True)    # Habilita botones
                self.spinBox_01.setEnabled(True)
                self.spinBox_02.setEnabled(True)
                self.spinBox_03.setEnabled(True)
                self.spinBox_04.setEnabled(False)
                self.spinBox_05.setEnabled(False)
                self.spinBox_00.setMinimum(0)       # Pone un limite para los botones de las constantes
                self.spinBox_01.setMinimum(0)
                self.spinBox_02.setMinimum(0)
                self.spinBox_03.setMinimum(1)
                self.spinBox_04.setMinimum(0)
                self.spinBox_05.setMinimum(0)
                self.spinBox_00.setProperty("value", 0)     # Regresa los botones a sus valores de default (0)
                self.spinBox_01.setProperty("value", 0)
                self.spinBox_02.setProperty("value", 0)
                self.spinBox_04.setProperty("value", 0)
                self.spinBox_05.setProperty("value", 0)

        elif grado_poli == 4:   # En caso de escoger un polinomio de grado 4
                self.spinBox_00.setEnabled(True)     # Habilita botones
                self.spinBox_01.setEnabled(True)
                self.spinBox_02.setEnabled(True)
                self.spinBox_03.setEnabled(True)
                self.spinBox_04.setEnabled(True)
                self.spinBox_05.setEnabled(False)
                self.spinBox_00.setMinimum(0)       # Pone un limite para los botones de las constantes
                self.spinBox_01.setMinimum(0)
                self.spinBox_02.setMinimum(0)
                self.spinBox_03.setMinimum(0)
                self.spinBox_04.setMinimum(1)
                self.spinBox_05.setMinimum(0)
                self.spinBox_00.setProperty("value", 0) # Regresa los botones a sus valores de default (0)
                self.spinBox_01.setProperty("value", 0)
                self.spinBox_02.setProperty("value", 0)
                self.spinBox_03.setProperty("value", 0)
                self.spinBox_05.setProperty("value", 0)
                
        elif grado_poli == 5:   # En caso de escoger un polinomio de grado 5
                self.spinBox_00.setEnabled(True)
                self.spinBox_01.setEnabled(True)
                self.spinBox_02.setEnabled(True)
                self.spinBox_03.setEnabled(True)
                self.spinBox_04.setEnabled(True)
                self.spinBox_05.setEnabled(True)
                self.spinBox_00.setMinimum(0)
                self.spinBox_01.setMinimum(0)
                self.spinBox_02.setMinimum(0)
                self.spinBox_03.setMinimum(0)
                self.spinBox_04.setMinimum(0)
                self.spinBox_05.setMinimum(1)
                self.spinBox_00.setProperty("value", 0)
                self.spinBox_01.setProperty("value", 0)
                self.spinBox_02.setProperty("value", 0)
                self.spinBox_03.setProperty("value", 0)
                self.spinBox_04.setProperty("value", 0)

        self.bt_graficar.setEnabled(True)   # Habilita el boton de bt_graficar
    #-------- Función para el grado y las constantes (FIN) -------------------

    #-------- Función para la graficación ------------------------------------
    def graficacion(self):
        self.spin_grado.setEnabled(False)   # Deshabilita los botones del paso anterior
        self.bt_grado.setEnabled(False)

        ## Creación de polinomio
        sym.init_printing()     # Para que funciones las variables en los polinomios
        x = Symbol("x")     # Declarando la variable "x"
        c00 = self.spinBox_00.text()    # Tomamos valores de las constantes en los spinbox
        c01 = self.spinBox_01.text()
        c02 = self.spinBox_02.text() 
        c03 = self.spinBox_03.text()
        c04 = self.spinBox_04.text()
        c05 = self.spinBox_05.text()
        if int(c05) != 0:       # Creamos el polinomio según el grado y constantes seleccionadas
            fx = c05+"*"+str(x**5) + " + " + c04+"*"+str(x**4) + " + " + c03+"*"+str(x**3) + " + " + c02+"*"+str(x**2) + " + " + c01+"*"+str(x**1) + " + " + c00
        elif int(c04) != 0:
            fx = c04+"*"+str(x**4) + " + " + c03+"*"+str(x**3) + " + " + c02+"*"+str(x**2) + " + " + c01+"*"+str(x**1) + " + " + c00
        elif int(c03) != 0:
            fx = c03+"*"+str(x**3) + " + " + c02+"*"+str(x**2) + " + " + c01+"*"+str(x**1) + " + " + c00
        elif int(c02) != 0:
            fx = c02+"*"+str(x**2) + " + " + c01+"*"+str(x**1) + " + " + c00
        elif int(c01) != 0:
            fx = c01+"*"+str(x**1) + " + " + c00
        elif int(c00) != 0:
            fx = c00

        self.polinomio.setText(str(fx))     # Asigna el polinomio al recuadro llamado polinomio
        self.bt_graficar.setEnabled(False)  # Deshabilita el botón de graficar.

        ##Creación y llenado de la tabla de Velocidades
        # La velocidad es la primera derivada de nuestro polinomio.
        fdx = sym.diff(fx,x,1)  # Derivamos el polinomio.
        vel = []        # Lista para los valores de velocidad
        t = []          # Lista para los valores de tiempo
        for i in range(0,20, 1):    # Hacemos las 20 repeticiones para guardar los valores en la tabla
            t.append(i)     # Ingresa los valores a la lista "t"
            vel.append(fdx.subs(x,i))   # Ingresa los valores a la lista "vel", haciendo las sustituciones en el polinomio
            self.tabla_vel.setItem(i, 0, QtWidgets.QTableWidgetItem(str(i)))    # Mete los valores a la tabla llamada "tabla_vel" en la columna Tiempo
            self.tabla_vel.setItem(i, 1, QtWidgets.QTableWidgetItem(str(vel[i])))   # Mete los valores a la tabla llamada "tabla_vel" en la columna Posición

        ##Creación y llenado de la tabla de Posiciones
        # La posición es la integral de la velocidad o nuestro polinomio inicial.
        pos = []    # Lista para guardar los valores de posición
        for k in range(0,20, 1):
            fdp = integrate(fdx)    # Realiza la integral de nuestra función de velocidad "fdx"
            pos.append(fdp.subs(x,k))   # Ingresa los valores a la lista "pos", haciendo las sustituciones en el polinomio
            self.tabla_pos.setItem(k, 0, QtWidgets.QTableWidgetItem(str(k)))    # Mete los valores a la tabla llamada "tabla_pos" en la columna Tiempo
            self.tabla_pos.setItem(k, 1, QtWidgets.QTableWidgetItem(str(pos[k])))   # Mete los valores a la tabla llamada "tabla_pos" en la columna Posición

        ##Creación y llenado de la tabla de Aceleraciones
        # La aceleración es la segunda derivada de nuestro polinomio o la derivada de la velocidad.
        fdx2 = sym.diff(fdx,x,1)    # realizamos la derivada de la velocidad.
        ace = []    # Lista para guardar los valores de la aceleración
        for j in range(0,20, 1):
            ace.append(fdx2.subs(x,j))  # Ingresa los valores a la lista "ace", haciendo las sustituciones en el polinomio
            self.tabla_ace.setItem(j, 0, QtWidgets.QTableWidgetItem(str(j)))    # Mete los valores a la tabla llamada "tabla_ace" en la columna Tiempo
            self.tabla_ace.setItem(j, 1, QtWidgets.QTableWidgetItem(str(ace[j])))   # Mete los valores a la tabla llamada "tabla_ace" en la columna Aceleración

        ##Distancia Total
        # se obtiene con la integral del polinomio de la velocidad
        desplazamiento = integrate(fdx, (x, int(t[0]), int(t[19])))     # realiza la integran definida en el tiempo definido
        self.distancia.setText(str(desplazamiento))     # Asigna el valor al recuadro "distancia"

        ##Graficación
        # Dado que Qt Designer no cuenta con un botón específico para matplotlib, debemos crear una nueva clase y agregar nuevas funciones a un Layout de la aplicación.
        self.graficaPosNor = Canvas_grafica()   # Creamos un Canvas para cada una de las gráficas.
        self.graficaVelNor = Canvas_grafica()   
        self.graficaAceNor = Canvas_grafica()
        self.graficaPosVec = Canvas_grafica()
        self.graficaVelVec = Canvas_grafica()
        self.graficaAceVec = Canvas_grafica()

        self.graficaPosNor.graficarPosicionNormal(t, pos)       # Hacemos la graficación según lo que buscamos
        self.graficaVelNor.graficarVelocidadNormal(t, vel)
        self.graficaAceNor.graficarAceleracionNormal(t, ace)
        self.graficaPosVec.graficarPosicionVector(t, pos)
        self.graficaVelVec.graficarVelocodadVector(t, vel)
        self.graficaAceVec.graficarAceleracionVector(t, ace)  

        self.pb_abrir_graf01.setEnabled(True)  # Habilita el botón de ver nuestras gráficas con animaciones
        self.pb_abrir_graf02.setEnabled(True)  
        self.pb_abrir_graf03.setEnabled(True)  
        self.pb_abrir_graf04.setEnabled(True)  
        self.pb_abrir_graf05.setEnabled(True)  
        self.pb_abrir_graf06.setEnabled(True)  

    #-------- Funciónes para abrir los Gif ----------------------------------------
    
    def ver_graf_01(self):
        wb.open_new('Practica01_grafs\Posicion01.gif')

    def ver_graf_02(self):
        wb.open_new('Practica01_grafs\PosicionVect.gif')

    def ver_graf_03(self):
        wb.open_new('Practica01_grafs\Velocodad01.gif')

    def ver_graf_04(self):
        wb.open_new('Practica01_grafs\VelocidadVect.gif')

    def ver_graf_05(self):
        wb.open_new('Practica01_grafs\Aceleracion01.gif')

    def ver_graf_06(self):
        wb.open_new('Practica01_grafs\AceleracionVect.gif')

    #-------- Funciónes para abrir los Gif (FIN) ----------------------------------

    #-------- Función para la graficación (FIN) ---------------------------------
        
#------------ Clase para el Canvas ----------------------------------------------------------------------------------#
class Canvas_grafica(FigureCanvas):
    #------------------ Función Inicial------------------------------------------
    def __init__(self, figure=None):

        self.fig, self.ax = plt.subplots()  # Se crea la tabla
        super().__init__(self.fig)

    #------------ Grafica de Posición (Puntos) ----------------------------------
    def graficarPosicionNormal(self, tiem01, pos01):    # Se piden las variables de otra clase para poder trabajarlos.
        x_data1 = []    # Se crea un array vacio para insertar los valores de la lista "tiem01" -> "t"
        y_data1 = []    # Se crea un array vacio para insertar los valores de la lista "pos01" -> "pos"

        self.ax.set_title('Gráfica de Posiciones ', loc = "center", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})    # Título de la Gráfica
        #self.ax.set_xlabel("Tiempo", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})   # Inserta el nombre al eje X
        self.ax.set_ylabel("Posición (Y)", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})     # Inserta un nombre al eje Y
        self.ax.grid(axis = 'y', color = 'gray', linestyle = 'dashed')  # Asigna la cudarícula

        self.ax.set_xlim(int(tiem01[0]), int(tiem01[19]))   # Inserta límites al eje X
        self.ax.set_ylim(int(pos01[0]), int(pos01[19]))     # Inserta límites al eje Y
        line, = self.ax.plot(0, 0, color = 'red', marker = 'o')  # Grafica los puntos con "o" (círculos)

        def animation_frame_Pos01(i):     # Función para realizar los frames de la animación
            x_data1.append(int(tiem01[i]))  # Inserta punto a punto los valores a las listas vacias.
            y_data1.append(int(pos01[i]))

            line.set_xdata(x_data1)
            line.set_ydata(y_data1)
            return line,

        animationPos01 = FuncAnimation(self.fig, func=animation_frame_Pos01, frames=np.arange(0, 19, 1), interval=200, repeat = False) # Función para aplicar la animación
        animationPos01.save('Practica01_grafs\Posicion01.gif')   # Guarda la animación en un archivo de tipo ".gif"
    #------------ Grafica de Posición (FIN) -------------------------------------

    #------------ Grafica de Posición (Vectores) --------------------------------
    def graficarPosicionVector(self, tiem01, pos01):
        x_data01 = []
        y_data01 = []
        
        self.ax.set_title('Gráfica de Posiciones (Vectores)', loc = "center", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'}) # Título de la Gráfica
        self.ax.set_ylabel("Posición (Y)", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})  # Inserta un nombre al eje Y
        self.ax.grid(axis = 'y', color = 'gray', linestyle = 'dashed')  # Asigna la cudarícula
        plt.axis([0, int(tiem01[19]), 0, int(pos01[19])])   # Asigna los límite a las gráfica
        plt.axis('on')
        plt.grid('True')

        self.ax.set_xlim(int(tiem01[0]), int(tiem01[19]))   # Inserta límites al eje X
        self.ax.set_ylim(int(pos01[0]), int(pos01[19]))     # Inserta límites al eje Y
        line, = self.ax.plot(0, 0, color = 'purple')  # Grafica

        for i in range(0,19):   # Se realiza tantos valores hay en la tabla_pos
            self.ax.quiver(int(tiem01[i]), int(pos01[i]), int(tiem01[i+1]), int(pos01[i+1]), color= ['blue'])   # Hace los vectores en la gráfica

        def animation_frame_Pos02(i):     # Función para realizar los frames de la animación
            x_data01.append(int(tiem01[i]))  # Inserta punto a punto los valores a las listas vacias.
            y_data01.append(int(pos01[i]))

            line.set_xdata(x_data01)
            line.set_ydata(y_data01)
            return line,

        animationPos02 = FuncAnimation(self.fig, func=animation_frame_Pos02, frames=np.arange(0, 19, 1), interval=200, repeat = False) # Función para aplicar la animación
        animationPos02.save('Practica01_grafs\PosicionVect.gif')   # Guarda la animación en un archivo de tipo ".gif"
    #------------ Grafica de Posición Vectores (FIN) -------------------------------

    #------------ Grafica de Velocidad (Puntos) ------------------------------------
    def graficarVelocidadNormal(self, tiem01, vel01):
        x_data3 = []    # Se crea un array vacio para insertar los valores de la lista "tiem01" -> "t"
        y_data3 = []    # Se crea un array vacio para insertar los valores de la lista "vel01" -> "vel"

        self.ax.set_title('Gráfica de Velocidades ', loc = "center", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})   # Título de la Gráfica
        self.ax.set_ylabel("Velocidad (Y)", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})    # Inserta un nombre al eje Y
        self.ax.grid(axis = 'y', color = 'gray', linestyle = 'dashed')  # Asigna la cudarícula

        self.ax.set_xlim(int(tiem01[0]), int(tiem01[19]))   # Inserta límites al eje X
        self.ax.set_ylim(int(vel01[0]), int(vel01[19]))     # Inserta límites al eje Y
        line, = self.ax.plot(0, 0, color = 'blue', marker = 'o')  # Grafica los puntos con "o" (círculos)

        def animation_frame_Vel01(i):     # Función para realizar los frames de la animación
            x_data3.append(int(tiem01[i]))  # Inserta punto a punto los valores a las listas vacias.
            y_data3.append(int(vel01[i]))

            line.set_xdata(x_data3)
            line.set_ydata(y_data3)
            return line,

        animationVel01 = FuncAnimation(self.fig, func=animation_frame_Vel01, frames=np.arange(0, 19, 1), interval=200, repeat = False) # Función para aplicar la animación
        animationVel01.save('Practica01_grafs\Velocodad01.gif')   # Guarda la animación en un archivo de tipo ".gif"
    #------------ Grafica de Velocidad (FIN) ----------------------------------------

    #------------ Grafica de Velocidad (Vectores) -----------------------------------
    def graficarVelocodadVector(self, tiem01, vel01):
        x_data02 = []
        y_data02 = []

        self.ax.set_title('Gráfica de Velocidades (Vectores)', loc = "center", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'}) # Título de la Gráfica
        self.ax.set_ylabel("Velocidad (Y)", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})    # Inserta un nombre al eje Y
        self.ax.grid(axis = 'y', color = 'gray', linestyle = 'dashed')  # Asigna la cudarícula
        plt.axis([0, int(tiem01[19]), 0, int(vel01[19])])   # Asigna los límite a las gráfica
        plt.axis('on')
        plt.grid('True')

        self.ax.set_xlim(int(tiem01[0]), int(tiem01[19]))   # Inserta límites al eje X
        self.ax.set_ylim(int(vel01[0]), int(vel01[19]))     # Inserta límites al eje Y
        line, = self.ax.plot(0, 0, color = 'pink')  # Grafica 

        for i in range(0,19):   # Se realiza tantos valores hay en la tabla_vel
            self.ax.quiver(int(tiem01[i]), int(vel01[i]), int(tiem01[i+1]), int(vel01[i+1]), color= ['green'])  # Hace los vectores en la gráfica

        def animation_frame_Vel02(i):     # Función para realizar los frames de la animación
            x_data02.append(int(tiem01[i]))  # Inserta punto a punto los valores a las listas vacias.
            y_data02.append(int(vel01[i]))

            line.set_xdata(x_data02)
            line.set_ydata(y_data02)
            return line,

        animationVel02 = FuncAnimation(self.fig, func=animation_frame_Vel02, frames=np.arange(0, 19, 1), interval=200, repeat = False) # Función para aplicar la animación
        animationVel02.save('Practica01_grafs\VelocidadVect.gif')   # Guarda la animación en un archivo de tipo ".gif"
    #------------ Grafica de Velocidad Vectores (FIN) -------------------------------

    #------------ Grafica de Aceleración (Puntos) -----------------------------------
    def graficarAceleracionNormal(self, tiem01, ace01):
        x_data5 = []    # Se crea un array vacio para insertar los valores de la lista "tiem01" -> "t"
        y_data5 = []    # Se crea un array vacio para insertar los valores de la lista "ace01" -> "ace"

        #self.ax.plot(x, y, marker = 'o')    # Grafica los puntos x & y con "o" (círculos)
        self.ax.set_title('Gráfica de Aceleraciones ', loc = "center", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'}) # Título de la Gráfica
        #self.ax.set_xlabel("Tiempo", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})  # Inserta el nombre al eje X
        self.ax.set_ylabel("Aceleración (Y)", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})  # Inserta un nombre al eje Y
        self.ax.grid(axis = 'y', color = 'gray', linestyle = 'dashed')  # Asigna la cudarícula

        self.ax.set_xlim(int(tiem01[0]), int(tiem01[19]))   # Inserta límites al eje X
        self.ax.set_ylim(int(ace01[0]), int(ace01[19]))     # Inserta límites al eje Y
        line, = self.ax.plot(0, 0, color = 'green', marker = 'o')  # Grafica los puntos con "o" (círculos)

        def animation_frame_Ace01(i):     # Función para realizar los frames de la animación
            x_data5.append(int(tiem01[i]))  # Inserta punto a punto los valores a las listas vacias.
            y_data5.append(int(ace01[i]))

            line.set_xdata(x_data5)
            line.set_ydata(y_data5)
            return line,

        animationAce01 = FuncAnimation(self.fig, func=animation_frame_Ace01, frames=np.arange(0, 19, 1), interval=200, repeat = False) # Función para aplicar la animación
        animationAce01.save('Practica01_grafs\Aceleracion01.gif')   # Guarda la animación en un archivo de tipo ".gif"s
    #------------ Grafica de Aceleración (FIN) --------------------------------------

    #------------ Grafica de Aceleración (Vectores) ---------------------------------
    def graficarAceleracionVector(self, tiem01, ace01):
        x_data03 = []
        y_data03 = []

        self.ax.set_title('Gráfica de Aceleraciones (Vectores)', loc = "center", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})   # Título de la Gráfica
        self.ax.set_ylabel("Aceleración (Y)", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})   # Inserta un nombre al eje Y
        self.ax.grid(axis = 'y', color = 'gray', linestyle = 'dashed')  # Asigna la cudarícula
        plt.axis([0, int(tiem01[19]), 0, int(ace01[19])])    # Asigna los límite a las gráfica
        plt.axis('on')
        plt.grid('True')

        self.ax.set_xlim(int(tiem01[0]), int(tiem01[19]))   # Inserta límites al eje X
        self.ax.set_ylim(int(ace01[0]), int(ace01[19]))     # Inserta límites al eje Y
        line, = self.ax.plot(0, 0, color = 'brown')  # Grafica 

        for i in range(0,19):   # Se realiza tantos valores hay en la tabla_vel
            self.ax.quiver(int(tiem01[i]), int(ace01[i]), int(tiem01[i+1]), int(ace01[i+1]), color= ['red'])     # Hace los vectores en la gráfica

        def animation_frame_Ace02(i):     # Función para realizar los frames de la animación
            x_data03.append(int(tiem01[i]))  # Inserta punto a punto los valores a las listas vacias.
            y_data03.append(int(ace01[i]))

            line.set_xdata(x_data03)
            line.set_ydata(y_data03)
            return line,

        animationVel02 = FuncAnimation(self.fig, func=animation_frame_Ace02, frames=np.arange(0, 19, 1), interval=200, repeat = False) # Función para aplicar la animación
        animationVel02.save('Practica01_grafs\AceleracionVect.gif')   # Guarda la animación en un archivo de tipo ".gif"
    #------------ Grafica de Velocidad Vectores (FIN) -------------------------------

        
#------------- Abre la aplicación ---------------------------------
if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
