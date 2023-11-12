i = int(input())
j = int(input())

if i < 0 or j < 0 or i > j:
    print('Inputan harus >= 0 dan i < j')
else:
    k = 0
    for x in range(i, j+1):
        if x % 2 != 0:
            k += x
    print(f'Total hasil penjumlahan setiap bilangan ganjil antara {i} dan {j} adalah {k}')