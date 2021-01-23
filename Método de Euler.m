##Inicialmetne calculamos a derivada de primeira e segunda ordem de epslon por software online
##Aplicamos na função 
f=@(t,i)(0.3*((3.9644*(e^(-0.06*pi*t))*sin(2*t))+((0.75398*e^(-0.06*pi*t))*cos(2*t))))+(1/1.4)*((e^((-3*pi*t)/50)*(sin(2*t)-100*cos(2*t)))/50)+1/1.7*((e^(-0.06*pi*t))*sin(2*t-pi));
##Definimos o intervalo das variáveis
x0=0;
x1=10;
y0=0;
h=0.1;
xn=x0;
yn=y0;
##Agora iremos criar um laço atribuindo os valores do intervalo de 0,1
##Após gerar os valores de xn será plotado no gráfico
while (xn<x1)
  yn1=yn+h*f(xn,yn);
  yn=yn1;
  xn=xn+h;
  disp(yn);
  plot(xn,yn,"o", "markersize", 15);
  
  hold on;
endwhile
hold off;
