# ======================== Information ========================
# Direct Link: https://www.hackerrank.com/contests/ujian-praktikum-ap-sesi-2-gojo/challenges/mari-berhitung-1-1
# Difficulty: Easy
# Soal : Piramid Angka Berderet

# ======================== Solusi ========================

def Pattern(n):
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        numbers = (''.join(str(j) for j in range(1, i+1)))
        print(spaces + numbers)

n = int(input())

Pattern(n)


# ======================== Test Case ========================
