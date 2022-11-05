x,y=input("The point (x,y)").split()
x=int(x)
y=int(y)
if x>0 and y>0 :
    print("Position:First Quadrant")
if x<0 and y>0 :
    print("Position:Second Quadrant")
if x<0 and y<0 :
    print("Position:Third Quadrant")
if x>0 and y<0 :
    print("Position:Forth Quadrant")
if x==0 :
    print("Position:Y Axis")
if y==0 :
    print("Position:X Axis")
