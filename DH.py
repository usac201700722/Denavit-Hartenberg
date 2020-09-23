import numpy as np # Importamos numpy como el alias np
import math
"""
Este programa sirve para determinar las matrices A de la tabla de Denavit-Hartenberg

para crear una matriz A tenemos que definir una variable de la siguiente manera:
A_01=traslacion(a,alpha,d,theta) 
(a, alpha, d,theta) son los valores de la tabla de DH correspondiente para la matriz A_01

Despúes de haber ingresado los 4 valores el programa muestra la matriz A_01 y almacena en A_01
la matriz correspondiente.

Para encontrar la matriz T debemos tener varias matrices A y multiplicarlas.
por ejemplo:
A_01 = traslacion(1,math.pi/2,0,math.pi)
A_12 = traslacion(0,0,2,math.pi/3)
A_23 = traslacion(1,math.pi/2,1,0)

T=A_01*A_12*A_23
print(T)    #Esto imprime la matriz T   
"""

def traslacion(a,alpha,d,theta):
    tras = np.array([[math.cos(theta),-1*math.cos(alpha)*math.sin(theta),math.sin(theta)*math.sin(alpha),a*math.cos(theta)],
                    [math.sin(theta),math.cos(theta)*math.cos(alpha),-1*math.sin(alpha)*math.cos(theta),a*math.sin(theta)],
                    [0,math.sin(alpha),math.cos(alpha),d],
                    [0,0,0,1]])
    print("*********Matriz A creada************")
    print(tras)
    print("*******************************")
    return tras

#traslacion(a,alpha,d,theta)
A_01 = traslacion(1,math.pi/2,0,math.pi)
A_12 = traslacion(0,0,2,math.pi/3)
A_23 = traslacion(1,math.pi/2,1,0)

T=A_01*A_12*A_23
print("\n")
print("************RESULTADO**************")
print(T)    #Esto imprime la matriz T 