x1=int(input("enter x1:"))
y1=int(input("enter y1:"))
x2=int(input("enter x2:"))
y2=int(input("enter y2:"))
x3=int(input("enter x3:"))
y3=int(input("enter y3:"))
x4=int(input("enter x4:"))
y4=int(input("enter y4:"))
A=0.5*((x1-x3)*(y2-y1)-(x1-x2)*(y3-y1))
A1=0.5*((x1-x4)*(y2-y1)-(x1-x2)*(y4-y1))
A2=0.5*((x1-x3)*(y4-y1)-(x1-x4)*(y3-y1))
A3=0.5*((x4-x3)*(y2-y1)-(x1-x2)*(y4-y1))
if A==A1+A2+A3:
    print("this point lies inside of triangle")
else:
    print("this point lies outside of triangle")
