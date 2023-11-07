# CARA 1: Menggunakan Index [::-1]
def palindrom(kata: str) -> str:
    kata = kata.replace(' ', '').lower()

    if kata == kata[::-1]:
        return 'Palindrom'
    else:
        return 'Bukan Palindrom'
    
word = input('Masukkan Kata : ')
print(palindrom(word))

# CARA 2: Menggunakan Methode .join(reversed())
def palindrom(kata: str) -> str:
    kata = kata.replace(' ', '').lower()

    if kata == ''.join(reversed(kata)):
        return 'Palindrom'
    else:
        return 'Bukan Palindrom'
    
word = input('Masukkan Kata : ')
print(palindrom(word))