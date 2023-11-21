# Soal 1 : Membuat Fungsi yang Menerima String sebagai Inputan dan Menghasilkan Deret Permutasi dari Kata Tersebut.
# CARA 1 : Tanpa Input
def stringpermutation(Kata):
    try:
        permutasi = []
        n = len(Kata)
        for i in range(n):
            move = Kata[i:] + Kata[:i] 
            permutasi.append(move)
        print(' | '.join(reversed(permutasi)), '|')
    except TypeError:
        print('Terjadi Kesalahan: Input harus berupa string')

stringpermutation('Mobil')
stringpermutation(123)
stringpermutation('Ayam')


# CARA 2 : Jika meminta Inputan
def stringPermutation(Kata):
    if type(Kata) == str:
        if Kata.isnumeric():
            print('Terjadi Kesalahan: Input harus berupa string')
            exit()
    try:
        huruf = Kata
        n = len(Kata)
        for i in range(n):
            move = huruf[-1] + huruf[:-1]
            print(move, end=" | ")
            huruf = move
    except TypeError as msg:
        print(f'\n Terjadi Kesalahan: {msg}')
 
x = input('Masukkan Kata: ')
stringPermutation(x)