m = int(input())
c100 = (m/100)
c5 = (m%100)
c50 = (c5/50)
c2 = (c5%50)
c20 = (c2/20)
c1 = (c2%20)
c10 = (c1/10)
c05 = (c1%10)
c5 = (c05/5)
c02 = (c05%5)
c2 = (c02/2)
c01 = (c02%2)
c1 = (c01/1)
print (m)
print ("%i nota(s) de R$ 100,00" %c100)
print ("%i nota(s) de R$ 50,00" %c50)
print ("%i nota(s) de R$ 20,00" %c20)
print ("%i nota(s) de R$ 10,00" %c10)
print ("%i nota(s) de R$ 5,00" %c5)
print ("%i nota(s) de R$ 2,00" %c2)
print ("%i nota(s) de R$ 1,00" %c1)