a = float(input())

if (a >= 0 and a <= 25.0000):
  print ("Intervalo [0,25]")

elif (a >= 25.00000 and a <= 50.0000):
  print ("Intervalo (25,50]")

elif (a >= 50.00000 and a <= 75.0000):
  print ("Intervalo (50,75]")

elif (a >= 75.00000 and a <= 100.0000):
  print ("Intervalo (75,100]")

elif (a < 0 or a > 100.0000):
  print ("Fora de intervalo")