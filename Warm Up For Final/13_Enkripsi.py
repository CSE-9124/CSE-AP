'''Soal : Sebuah pesan rahasia s perlu dienkripsi untuk kepentingan negara. Pertama, pesan tersebut dihapus
spasinya. Kemudian, P merupakan panjang dari pesan tersebut. Dimana akar P sebagai baris (pembulatan ke 
bawah) dan kolom (pembulatan ke atas).'''

# CARA 1 : (Kurang Tepat)
from math import floor, ceil, sqrt

s = input().replace(' ', '')

P = len(s)

row = floor(sqrt(P))
column = ceil(sqrt(P))

if 1 <= P <= 81:
    for i in range(column):
        for j in range(row):
            index = j * column + i

            if index < P:
                print(s[index], end="")

        print(" ", end="")
else:
    print('None')


# CARA 2:
s = input().replace(" ", "")

P = len(s)

row = floor(sqrt(P))
colum = ceil(sqrt(P))

if row * colum < P:
    row = colum

matriks = []
indeks = 0

for i in range(row):
    matriks.append(s[indeks:indeks+colum])
    indeks += colum

simpan = ""
for i in range(colum):
    for j in range(row):
        if i < len(matriks[j]):
            simpan += matriks[j][i]
    if i < colum - 1:
        simpan += " "

print(simpan)