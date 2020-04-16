dados = input().split(' ')
N1, N2, N3, N4 = dados
N1 = float(N1)
N2 = float(N2)
N3 = float(N3)
N4 = float(N4)
media = ((N1*2.0) + (N2*3.0) + (N3*4.0) + (N4*1.0)) / 10.0
print ("Media: %.1f" %media)

if (media >= 7.0):
    print ("Aluno aprovado.")

elif (media < 5.0):
    print ("Aluno reprovado.")

elif (media >= 5.0 and media <= 6.9):
    print ("Aluno em exame.")
    notaExame = float(input())
    print ("Nota do exame: %s" %notaExame)
    novaMedia = ((media + notaExame) / 2.0)
    if (novaMedia >= 5.0):
        print ("Aluno aprovado.")
    elif (novaMedia <= 4.9):
        print ("Aluno reprovado.")
    print ("Media final: %s" %novaMedia)