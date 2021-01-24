import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib
## DETERMINAMOS O LAÇO A SER FEITO
def factorial( n ):
    if n == 0:
        return 1
    fact = 1
    for i in range( 1, n+1 ):
        fact *= i
    return fact
def y(t):
  return (-1/t)
def taylor_mthd( f, a, b, N, IV ):
    h = (b-a)/float(N)                 
    t = np.arange( a, b+h, h )          
    w = np.zeros((N+1,))                
    t[0], w[0] = IV                     
    for i in range(1,N+1):             
        T = 0
        for j in range(len(f)):
            h_factor = h**(j)/float(factorial(j+1))
            T += h_factor * f[j]( t[i-1], w[i-1] )
        w[i] = w[i-1] + h * T
    return w
##Determinamos o critério inicial e o de parada, 1=<t=<2    
a, b = 1.0, 2.0
##Determinamos a quantidade de vetores             
N = 10
##Os passos                     
h = 0.1                     
IV = ( 1, -1 )
t = np.arange( a, b+h, h )
##f = y' do enunciado, ou seja, (1/t**2) - (y/t) - y**2 
f   = lambda t, y: (1/t**2) - (y/t) - y**2
##Derivamos a funçao f && sobrepomos o valor encontrado na função f, denominamos de ff     
ff  = lambda t, y: (1/t**2) - (y/t) - (y**2)+ (-2+y*t)/t**3
##Derivamos a funçao ff && sobrepomos o valor encontrado na função f, denominamos de fff  
fff = lambda t, y: (1/t**2) - (y/t) - (y**2)- (-2+y*t)/t**3 - (-6+2*y*t)/t**4
 
w2 = taylor_mthd( [ f, ff ], a, b, N, IV )
print(taylor_mthd([ f, ff ], a, b, N, IV ))
w3 = taylor_mthd( [ f, ff, fff ], a, b, N, IV )
##Plotamos no gráfico para fazer uma comparação com o método de lagrange && verificar o valor da segunda ordem com o valor exato
plt.plot( t, w2, label='2nd ordem' )
plt.plot( t, y(t), label='valor exato' )
plt.title( "Método de Taylor, N="+str(N) )
plt.xlabel('t') 
plt.ylabel('y(t)')
plt.legend(loc=4)
