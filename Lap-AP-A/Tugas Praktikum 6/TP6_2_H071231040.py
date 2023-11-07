# CARA 1:
array1 = map(int, input('Input array ke-1: ').split(' '))
array2 = map(int, input('Input array ke-2: ').split(' '))

set1 = set(array1)
set2 = set(array2)

duplikat = tuple(set1 & set2)
banyak = len(duplikat)

print(f'Terdapat {banyak} buah duplikat yaitu {duplikat}')


# CARA 2: Menggunakan Dictionary
Angka = {
    "array1": set(map(int, input('Input array ke-1: ').split(' '))),
    "array2": set(map(int, input('Input array ke-2: ').split(' ')))
}

duplikat = tuple(Angka['array1'] & Angka['array2'])
banyak = len(duplikat)

print(f'Terdapat {banyak} buah duplikat yaitu {duplikat}')