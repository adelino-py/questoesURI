N = int(input())
listNomes = list()
listNotas = list()
for i in range(N):
    listNomes.append(input())
    dificuldade = float(input())
    nota = list(map(float,input().split()))
    nota.sort()
    nota = nota[1:6]
    listNotas.append(sum(nota)*dificuldade)
for i in range(N):
    print("%s %.2f"%(listNomes[i],listNotas[i]))