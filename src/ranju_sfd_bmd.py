l1=float(input("L1(in meter):"))
l2=float(input("L2(in meter):"))
l3=float(input("L3(in meter):"))
l4=float(input("L4(in meter):"))
l5=float(input("L5(in meter):"))
w=float(input("UDL(KN/m):"))
p1=float(input("P1(KN):"))
p2=float(input("P2(KN):"))
b=l2+(l3/2)
c=l2+l3+l4
d=l2+l3+l4+l5
rb=((w*l3*b)+(p2*c)-(p1*l1))/d
ra=p1+p2+(w*l3)-rb
print(f"Reaction at A:{ra}\nReaction at B:{rb}")