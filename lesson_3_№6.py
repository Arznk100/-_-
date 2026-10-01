import numpy
import numpy as np

def MNK(a,b):
    x = sum(a)/len(a)
    y = sum(b)/len(b)
    xy = sum([a[i]*b[i] for i in range(len(a))])/len(a)
    x2 = sum([a[i]**2 for i in range(len(a))])/len(a)
    y2 = sum([b[i]**2 for i in range(len(b))])/len(b)
    k = (xy - x*y)/(x2 - x**2)
    b = y - k*x
    return k,b
x = np.array(list(map(float,input().split())))
y = np.array(list(map(float,input().split())))
print(len(x))
print(MNK(x,y))