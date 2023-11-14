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


# Berputar 