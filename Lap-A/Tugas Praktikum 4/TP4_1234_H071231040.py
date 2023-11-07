# Soal 1 :
def permutasi_kata(kata):
    try:
        if not isinstance(kata, str):
            raise TypeError("Input harus berupa string")
        
        permutasi = [kata]
        n = len(kata)
        for i in range(n-1):
            perpindahankata = kata[1:] + kata[0]
            permutasi.append(perpindahankata)
            kata = perpindahankata

        print(' | '.join(reversed(permutasi)), '|')
    except TypeError as msg:
        print(f"Terjadi kesalahan: {msg}")

kata = input('Masukkan kata : ')
permutasi_kata(kata)
permutasi_kata(1234)


# Soal 2
def palindrom(kata: str) -> str:
    kata = kata.replace(' ', '').lower()

    if kata == kata[::-1]:
        return 'Palindrom'
    else:
        return 'Bukan Palindrom'
    
word = input('Masukkan Kata : ')
print(palindrom(word))


# Soal 3
def maksimum(*angka):
    maks = angka[0]
    for angka_terbesar in angka:
        if angka_terbesar > maks:
            maks = angka_terbesar
    
    return maks

print(f'>> {maksimum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}')

# Soal 4
def catAndMouse(catA, catB, mosC):
    A = abs(mosC - catB)
    B = abs(mosC - catA)

    if A > B :
        return "Cat A"
    elif B > A :
        return "Cat B"
    else:
        return "Mouse C"
    
catA = int(input('Cat A : '))
catB = int(input('Cat B : '))
mosC = int(input('Mouse C : '))
print(catAndMouse(catA=catA, catB=catB, mosC=mosC))