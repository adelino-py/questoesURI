dados = input().split(' ')
A, B, C = dados
A = float(A)
B = float(B)
C = float(C)

if (((B - C) < A) and (A < (B + C))):
    if (((A - C) < B) and (B < (A + C))):
        if (((A - B) < C) and (C < (A + B))):
            perimetro = (A + B + C)
            print ("Perimetro = %.1f" %perimetro)
else:
    area = (((A + B) * C) / 2)
    print ("Area = %.1f" %area)