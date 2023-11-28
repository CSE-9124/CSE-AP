# ======================== Information ========================
# Direct Link: https://www.hackerrank.com/contests/ujian-praktikum-ap-sesi-2-gojo/challenges/berapa-ya-jumlahnya-1
# Difficulty: Easy
# Soal : Hitung Banyak Kata

# ======================== Solusi ========================

tampung = {}

N = int(input())

for i in range(N):
    Kata = input()

    if Kata in tampung:
        tampung[Kata] += 1
    else:
        tampung.update({Kata: 1})

print(len(tampung))
for i in tampung:
    print(tampung[i], end=" ")


# ======================== Test Case ========================
''' Test Case 0 '''
N = 5
Kata = '''appel
        pisang
        appel
        jeruk
        pisang'''
Output = '''3
        2 2 1'''

''' Test Case 1 '''
N = 4
Kata = '''bcdef
        abcdefg
        bcde
        bcdef'''
Output = '''3
        2 1 1'''