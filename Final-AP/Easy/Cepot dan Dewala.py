# ======================== Information ========================
# Direct Link: https://www.hackerrank.com/contests/ujian-praktikum-ap-sesi-2-gojo/challenges/cepot-dan-dewala/problem
# Difficulty: Easy

# ======================== Solusi ========================
# CARA 1 :
S = input()

def Meet(S):
    langkah = len(S) - 2

    if '|' in S:
        print('Cepot tidak ketemu Dewala')
    else:
        print(f'Cepot beretemu Dewala dalam {langkah} langkah')

Meet(S)


# CARA 2 :
S = input().lower()

def Ketemuan(s):
    index_Novi = s.index("n")
    index_Dilla = s.index("d")

    if "|" in s[index_Novi:index_Dilla]:
        return "Novi tidak ketemuan dengan Dilla"
    else:
        langkah = abs(index_Novi - index_Dilla) - 1
        return f"Novi ketemuan dengan Dilla dalam {langkah} langkah"

print(Ketemuan(S))


# ======================== Test Case ========================
''' Test Case 0 '''
S = 'd       c'
Meet(S)

''' Test Case 1 '''
S = 'd     | c'
Meet(S)