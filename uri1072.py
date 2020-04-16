N = int(input())
c = 0
d = 0
f = 0
while (c<N):
 a = int(input())
 c = c + 1
 if (a >= 10 and a <= 20):
  d = d +1
 else:
  f = f + 1
print ("%i in" %d)
print ("%i out" %f)