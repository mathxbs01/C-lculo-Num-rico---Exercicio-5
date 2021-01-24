import numpy as np
from sympy import Symbol
import sympy as sym
#x = 1=<t=<2, no intervalo de 10, ou seja, x = 1*h
#y = imagem da EDO do método de Taylor
x=1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2;  
y= -1,-0.91,-0.83458348,-0.77046126,-0.71526176,-0.6672326,-0.62505129,-0.58770124,-0.5543883,-0.52448316,-0.49748074;
xp=Symbol('x')
arrayLen=len(x)
l=[]
for i in range(arrayLen):
    arrayaux=np.arange(arrayLen)
    arrayaux=list(arrayaux)
    arrayaux.remove(i)
    numLi=1
    denli=1
    for j in arrayaux:
        numLi=numLi*(xp-x[j])
        denli=denli*(x[i]-x[j])
#Determinando o produtório de todas as entradas
    Li=numLi/denli
    l.append(sym.expand(Li))
#Agora iremos determinar o grau do polinomio
p=np.sum(y*np.array(l))
print("Polinômio=")
print(p)
