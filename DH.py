import numpy as np # Importamos numpy como el alias np
import math


def traslacion(alpha,a,d,theta):
    tras = np.array([[math.cos(alpha),-1*math.cos(theta)*math.sin(alpha),math.sin(theta)*math.sin(alpha),a*math.cos(alpha)],
                    [math.sin(alpha),math.cos(theta)*math.cos(alpha),-1*math.sin(theta)*math.cos(alpha),a*math.sin(alpha)],
                    [0,math.sin(theta),math.cos(theta),d],
                    [0,0,0,1]])
    return tras

alpha = float(input("Ingrese Alpha: "))
a = int(input("Ingrese a: "))
d = int(input("Ingrese d: "))
theta = int(input("Ingrese theta: "))

Matriz= traslacion(alpha,a,d,theta)
print (Matriz)