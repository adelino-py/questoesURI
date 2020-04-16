d = input().split (' ')
d2 = input().split (' ')
x1, y1 = d
x1 = float(x1)
y1 = float(y1)
x2, y2 = d2
x2 = float(x2)
y2 = float(y2)
dist = ((x1-x2)**2+(y1-y2)**2)**(1/2)
print ("%.4f"%dist)