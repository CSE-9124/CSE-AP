def maksimum(*angka):
    maks = angka[0]
    for angka_terbesar in angka:
        if angka_terbesar > maks:
            maks = angka_terbesar
    
    return maks

def minimum(*angka):
    mini = angka[0]
    for angka_terkecil in angka:
        if angka_terkecil < mini:
            mini = angka_terkecil
    
    return mini

N = list(map(int, input().split(' ')))

print(f'{minimum(*N)} {maksimum(*N)}')