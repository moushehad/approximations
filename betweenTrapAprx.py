"""
A script for approximating the signed area bound
between two curves using the Trapezoid Rule.

(1)import np and plt
(2)the f and g
(3)bounds, limits, Dx
(4)compute sum
(5)plot f and g
(6)add the traps
(7)label graph
(8)print
""" 

#(1)import np and plt
import numpy as np
import matplotlib.pyplot as plt

#(2)the f and g
def f(x): 
    return np.sin(x)
def g(x):
    return np.cos(x)

#(3)bounds, limits, Dx
a = -3 * np.pi / 4 
b =  5 * np.pi / 4
n = 10
Dx = (b-a) / n

#(4)compute sum
xi = np.linspace(a, b, n+1)
Dy = f(xi) - g(xi)
area = (Dx/2) * (Dy[0] + Dy[-1] + 2*np.sum(Dy[1:-1]))

#(5)plot f and g
xGrid = np.linspace(a, b, 1000)
plt.plot(xGrid, f(xGrid), label = 'sin(x)', color = 'red')
plt.plot(xGrid, g(xGrid), label = 'cos(x)', color = 'blue')

#(6)add the traps
yf = f(xi)
yg = g(xi)
for i in range(n):
    xRect = [xi[i], xi[i], xi[i+1], xi[i+1]]
    yRect = [yg[i], yf[i], yf[i+1], yg[i+1]]
    plt.fill(xRect, yRect, color='violet', alpha=0.15, edgecolor='black')

#(7)label graph
plt.grid(True)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Trapezoid Rule: Area Between sin(x) and cos(x)")
plt.legend()

#(9)print
print("The approximate area is A =  ", area)
plt.show()

