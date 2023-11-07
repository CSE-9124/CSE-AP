Suku = int(input())
U1 = 0
U2 = 1

if Suku > 0:
    for i in range(Suku):
        print(U1, end=' ')
        Un = U1 + U2
        U1 = U2
        U2 = Un
elif Suku == 1:
    print(U1)
else:
    print('Input bilangan Positif')