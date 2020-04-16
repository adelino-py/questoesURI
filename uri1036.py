dados = input().split(" ")
A, B, C = dados
A = float(A)
B = float(B)
C = float(C)
if ( A != 0):
  delt = ((B**2) - 4.0 * A *C)
  if (delt > 0):
    raiz1 = (-B + (delt**0.5))/(2.0*A) 
    raiz2 = (-B - (delt**0.5))/(2.0*A)
    print ("R1 = %.5f" %raiz1)
    print ("R2 = %.5f" %raiz2)
  elif (delt < 0):
   print ("Impossivel calcular") 
else:
  print ("Impossivel calcular") 