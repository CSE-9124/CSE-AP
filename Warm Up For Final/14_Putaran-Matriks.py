# Berputar Searah Jarum Jam
def Putaran_Matriks(Matriks, Putaran):
    for _ in range(Putaran):
        Matriks = list(zip(*Matriks[::-1]))
    return Matriks

Matriks = []
for i in range(3):
    Baris = input().split()
    Matriks.append(Baris)

Putaran = int(input())

Hasil = Putaran_Matriks(Matriks, Putaran)

for j in Hasil:
    print(' '.join(j))


# Berputar Berlawanan Arah Jarum Jam
x = input().split()
y = input().split()
z = input().split()
Putaran = int(input())

if Putaran == 1 or Putaran == 2 :
    x = x[::-1]
    y = y[::-1]
    z = z[::-1]

    if Putaran == 1 :
        for a, b, c in zip(x,y,z):
            print(a, b, c)
    elif Putaran == 2 :
        a = [z, y, x]
        for i in a:
            print(*i)

elif Putaran == 3 :
    for a, b, c in zip(x,y,z):
        print(c, b, a)

else :
    a = [x, y, z]
    for i in a:
        print(*i)