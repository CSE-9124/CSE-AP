# Soal : Membuat program untuk mengetahui ukuran ordo sebuah matriks

Matriks = []
while True :
    x = input().split()

    if x[0] == 'end' :
        break
    else:
        Matriks.append(x)

for i in Matriks :
    for j in i :
        try :
            j = float(j)
        except ValueError :
            print('Bukan Matriks')
            exit()

b = len(Matriks)
k = len(Matriks[0])

salah = []
for i in Matriks :
    if len(i) != k :
        salah.append(1)

if sum(salah) > 0 or b > k :
    print('Bukan Matriks')
else :
    print(f'Matriks {b} x {k}')