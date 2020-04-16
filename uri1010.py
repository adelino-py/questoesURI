dados = input().split(' ')
dados2 = input().split(' ')
cp1, np1, vp1 = dados
cp2, np2, vp2 = dados2
np1 = int(np1)
vp1 = float(vp1)
np2 = int(np2)
vp2 = float(vp2)
FINAL = (vp1*np1+vp2*np2)
print ("VALOR A PAGAR: R$ %.2f" %FINAL)