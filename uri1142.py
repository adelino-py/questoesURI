N = int(input())
for i in range (0, N):
  l = (i*4)+1 
  while (l%4 != 0):
    print ("%i" %l, end= " ")
    l = l +1
  print ("PUM")