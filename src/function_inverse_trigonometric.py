import numpy as np
def arcsin_d(a):
    x=np.arcsin(a)
    y=np.degrees(x)
    return y
def arccos_d(a):
    x=np.arccos(a)
    y=np.degrees(x)
    return y
def arctan_d(a):
    x=np.arctan(a)
    y=np.degrees(x)
    return y
x=input("The value:")
x=float(x)
a=arcsin_d(x)
b=arccos_d(x)
c=arctan_d(x)
print(f"Sin-1(x):{a}\nCos-1(x):{b}\nTan-1(x):{c}")
