def maksimum(*angka):
    angka = list(angka)
    try:
        for i in range(3):
            maks = angka[0]
            for angka_terbesar in angka:
                if angka_terbesar > maks:
                    maks = angka_terbesar
            angka.remove(angka_terbesar)
    except:
        return 'Parameter Kurang'
    return maks

print(f'>> {maksimum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}')
print(f'>> {maksimum(37, 84, 29, 51, 12)}')
print(f'>> {maksimum(57, 62)}')
print(f'>> {maksimum(0, 23, 54, 3, 28, 95)}')
print(f'>> {maksimum(56, 79)}')