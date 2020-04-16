dados = input().split(' ')
A, B, C = dados
A = float(A)
B = float(B)
C = float(C)
if (A>B and A>C):
  print ("%.0f eh o maior" %A)
elif (B>A and B>C):
  print ("%0.f eh o maior" %B) 
elif (C>A and C>B):
  print ("%.0f eh o maior"%C)