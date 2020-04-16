S,T,F = map(int,input().split())
if S==0:
    S=24
cheg= S+T+F
if cheg>24:
    cheg=cheg-24
    print(cheg)
elif cheg==24:
    cheg=0
    print(cheg)
else:
    print(cheg)