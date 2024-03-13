import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon
import shapely.geometry as sg
import shapely.ops as so
a=int(input("Enter no. of sides : "))
sx=int(input("Enter  x shear :"))
sy=int(input("Enter y shear : "))
d=[]
n=[] 
for i in range(a):
    x=int(input("Enter x coordinate : "))
    y=int(input("Enter y coordinat : "))
    d.append([x,y])
print(d)
u=np.array(d)
for i in u:
    x1=i[0]
    y1=i[1]
    x2=x1*(1+sx)
    y2=y1*(1+sy)
    n.append([x2,y2])
print(n)
z=np.array(n)

r1 = sg.Polygon(u)
r2 = sg.Polygon(z)

new_shape = so.unary_union([r1,r2])
fig, axs = plt.subplots()
axs.set_aspect('equal', 'datalim')

for geom in new_shape.geoms:    
    xs, ys = geom.exterior.xy    
    axs.fill(xs, ys, alpha=0.5, fc='r', ec='none')
plt.show()
