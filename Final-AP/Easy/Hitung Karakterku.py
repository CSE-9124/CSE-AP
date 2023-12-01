# ======================== Information ========================
# Direct Link: https://www.hackerrank.com/contests/ujian-praktikum-ap-sesi-2-gojo/challenges/hitung-karakterku
# Difficulty: Easy

# ======================== Solusi ========================

Kalimat = str(input('Input: '))

def Hitung_Karakter(kalimat):
    kalimat = kalimat.lower()

    frekuensi_karakter = {}

    for karakter in kalimat:
        if karakter.isalpha() or karakter.isnumeric():
            if karakter in frekuensi_karakter:
                frekuensi_karakter[karakter] += 1

            else:
                frekuensi_karakter[karakter] = 1

    return frekuensi_karakter

hasil = Hitung_Karakter(Kalimat)
print(f'Output: {hasil}')


# ======================== Test Case ========================
''' Test Case 0 '''
Kalimat = 'Hello, World!'
print(f'Output: {Hitung_Karakter(Kalimat)}')

''' Test Case 1 '''
Kalimat = 'Programming is fun!'
print(f'Output: {Hitung_Karakter(Kalimat)}')

''' Test Case 2 '''
Kalimat = 'OpenAI GPT-3'
print(f'Output: {Hitung_Karakter(Kalimat)}')

''' Test Case 3 '''
Kalimat = 'Testing 123'
print(f'Output: {Hitung_Karakter(Kalimat)}')