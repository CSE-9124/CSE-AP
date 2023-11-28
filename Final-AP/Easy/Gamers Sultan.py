# ======================== Information ========================
# Direct Link: https://www.hackerrank.com/contests/ujian-praktikum-ap-sesi-2-gojo/challenges/
# Difficulty: Easy

# ======================== Solusi ========================

b, bk, bm= map(int, input().split())
k = list(map(int, input().split()))
m = list(map(int, input().split()))

def Kombinasi_Harga_Termahal(b, bk, bm, k, m):
    max_cost = -1

    for i in range(bk):
        for j in range(bm):

            total_harga = k[i] + m[j]
            if total_harga <= b and total_harga > max_cost:
                max_cost = total_harga

    return max_cost

print(Kombinasi_Harga_Termahal(b, bk, bm, k, m))


# ======================== Test Case ========================
''' Test Case 0 '''
b, bk, bm = 10, 2, 3
k = [3, 1]
m = [5, 2, 8]
print(Kombinasi_Harga_Termahal(b, bk, bm, k, m))

''' Test Case 1 '''
b, bk, bm = 5, 1, 1
k = [4]
m = [5]
print(Kombinasi_Harga_Termahal(b, bk, bm, k, m))

''' Test Case 2 '''
b, bk, bm = 100000, 10, 12
k = [134, 1999, 2890, 760, 150000, 12345, 99999, 89765, 7543, 12]
m = [9, 95200, 145, 89999, 65498, 18888, 100000, 19876, 15009, 100, 13578, 2]
print(Kombinasi_Harga_Termahal(b, bk, bm, k, m))