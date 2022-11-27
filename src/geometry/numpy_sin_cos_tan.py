import numpy as np
import math as m
a1=float(input("Angle In Degree:"))
a=np.radians(a1)
x=np.sin(a)
y=np.cos(a)
z=np.tan(a)
print(f"Sin{a1}=",x)
print(f"Cos{a1}=",y)
if a1%90==0:
    print(f"Tan{a1}=Infinite")
else:
    print(f"Tan{a1}=",z)
