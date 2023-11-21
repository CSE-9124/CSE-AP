# Soal 1 : Menghasilkan Jumlah Suku Fibonacci

# CARA 1 : Menggunakan While Loop
Suku = int(input())
n1 = 0
n2 = 1
s = 0

if Suku > 0 :
    while s < Suku :
        print(n1, end=" ")
        Un = n1 + n2
        n1 = n2 
        n2 = Un
        s += 1        
elif Suku == 1:
    print(n1)
else:
    print('Input Bilangan Positif')


# CARA 2 : Menggunakan For Loop
print()
suku = int(input())
U1 = 0
U2 = 1

if suku > 0:
    for n in range(suku):
        print(U1, end=" ")
        U3 = U1 + U2
        U1 = U2
        U2 = U3
elif suku == 1:
    print(U1)
else:
    print('Input Bilangan Positif')