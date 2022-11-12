import numpy as np
x=float(input("The value:"))
s=np.arcsin(x)
c=np.arccos(x)
t=np.arctan(x)
s=(180/np.pi)*s
c=(180/np.pi)*c
t=(180/np.pi)*t
print(f"Sin-1(x):{s}\nCos-1(x):{c}\nTan-1(x):{t}")