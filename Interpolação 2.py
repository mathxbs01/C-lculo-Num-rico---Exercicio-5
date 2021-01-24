import numpy as np
from sympy import Symbol
import sympy as sym
#t = (1.052)/ t =  (1.555)/ t =  (1.978)
#x = 1=<t=<2, no intervalo de 10, ou seja, x = t
#y = imagem de y(t)
y=-0.9505703422053231,-0.6430868167202572,-0.5055611729019212
x=1.052,1.555,1.978;
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