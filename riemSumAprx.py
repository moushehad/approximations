"""
A script for approximating the signed area of a curve
bound between two points and the x axis
using a Riemann Sum.

(1)import np and plt  (2)what the f is    (3)bounds, limits, delta x
(4)y in terms of x    (5)compute the sum  (6)build the plane, plot the graph
(7)add the rectangles (8)fill the graph   (9)print
"""

#(1)import np and plt
import numpy as np
import matplotlib.pyplot as plt

#(2)what the f is
def f(x): #func takes parameter x, needs return
    return np.sin(x)

#(3)bounds, limits, delta x
a = -np.pi
b = np.pi
n = 15
Dx = (b-a) / n


#(4)y in terms of x
x = np.linspace(a, b, n+1)#solves for the xs we need
y = f(x) #plugs each x into f

#(5)compute the sum
area = Dx * np.sum(y[:-1])

#(6)build the plane, plot the graph
xGrid = np.linspace(a, b, 1000)
yGrid = f(xGrid)
plt.plot(xGrid, yGrid, color = 'red')

#(7)add the rectangles
for i in range(n):
    xRect = [x[i], x[i], x[i+1], x[i+1]]
    yRect = [0, y[i], y[i], 0]
    plt.fill(xRect, yRect, color='lightblue', alpha=0.5, edgecolor='black')

#(8)label and fill the graph
plt.grid(True)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Riemann Sum of f(x) = sin(x)")

#(9)print
print("A = ", area)
plt.show()
