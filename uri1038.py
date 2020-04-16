dados = input().split(" ")
C, Q = dados
C = int(C)
Q = int(Q)
if C == 1:
  print("Total: R$ %.2f" %(4.00*Q))
elif C == 2:
  print("Total: R$ %.2f" %(4.50*Q))
elif C == 3:
  print("Total: R$ %.2f" %(5.00*Q))
elif C == 4:
  print("Total: R$ %.2f" %(2.00*Q))
elif C == 5:
  print("Total: R$ %.2f" %(1.50*Q))