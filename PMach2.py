from math import sqrt
import numpy as np
display('First Coordinates:')
X1 = int(input('Coordinate x1: '))
Y1 = int(input('Coordinate y1: '))
display('Second Coordinates:')
X2 = int(input('Coordinate x2: '))
Y2 = int(input('Coordinate y2: '))
display('Third Coordinates:')
X3 = int(input('Coordinate x3: '))
Y3 = int(input('Coordinate y3: '))

F = 1; 
U = np.array([[2*X1, 2*Y1, F], [2*X2, 2*Y2, F], [2*X3, 2*Y3, F]])
M1 = -((X1*X1)+(Y1*Y1))
M2 = -((X2*X2)+(Y2*Y2))
M3 = -((X3*X3)+(Y3*Y3))
FM = np.array([[M1], [M2], [M3]])

dd = np.linalg.solve(U,FM)
D = dd[0]
E = dd[1]
F = dd[2]

vector = [D,E,F]

display('Following are the parameters of the circle: ')
print('Center (h,k): (',float(-D),',',float(-E),')',sep='')
print('Radius, r: ', sqrt((D)*(D)+(E)*(E)-F))
print('Vector [D,E,F]: (',float(D),'),(',float(E),'),(',float(F),')',sep='')
