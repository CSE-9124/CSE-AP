# Study Case 1
def faktorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * faktorial(x - 1)

def Kombinasi(n, r):
    if n < r:
        return 0
    else:
        return faktorial(n) // (faktorial(r) * faktorial(n-r))

n = int(input('n = '))
r = int(input('r = '))

print(Kombinasi(n, r))


# Study Case 2
def konversi(A):
    try:
        x = int(A)
        print(f'{x} bertipe data {type(x)}')
    except ValueError as msg:
        print(f'Error karena {msg}')

Angka = input('input : ')
konversi(Angka)


# Study Case 3
def Volume_Kubus(S):
    s = float(S)
    if s < 0:
        print('Terjadi Kesalahan: Panjang sisi tidak boleh negatif')
        exit()
    return s**3
    
try:
    S = input('Masukkan panjang sisi: ')
    print(f'Volume = {Volume_Kubus(S):.2f}')
except ValueError as msg:
    print(f'Terjadi Kesalahan: {msg}')
except Exception as msg:
    print(f'Terjadi Kesalahan tak terduga: {msg}')
