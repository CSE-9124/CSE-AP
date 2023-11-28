# ======================== Information ========================
# Direct Link: https://www.hackerrank.com/contests/ujian-praktikum-ap-sesi-2-gojo/challenges/hitung-karakter-1/problem
# Difficulty: Easy

# ======================== Solusi ========================

N = int(input())

Karakter = input().split()

def Hitung_Karakter(cari_karakter):
    banyak = Karakter.count(cari_karakter)

    print(f'Karakter {cari_karakter} muncul sebanyak {banyak} kali')

cari_karakter = input().lower()
Hitung_Karakter(cari_karakter)


# ======================== Test Case ========================
''' Test Case 0 '''
N = 5
Karakter = ['a', 'b', 'c', 'd', 'a']
cari_karakter = 'a'
Hitung_Karakter(cari_karakter)

''' Test Case 1 '''
N = 5
Karakter = ['dan', 'waktu', 'pikiran', 'dan', 'air']
cari_karakter = 'dan'
Hitung_Karakter(cari_karakter)