# ======================== Information ========================
# Direct Link: https://www.hackerrank.com/contests/ujian-praktikum-ap-sesi-2-gojo/challenges/bunga-bunga
# Difficulty: Easy

# ======================== Solusi ========================

N = int(input())

arr = map(int, input().split())

def Maks(arr):
    maks = 0
    for angka_besar in arr:
        if angka_besar > maks:
            maks = angka_besar
            
    return f'Tinggi bunga tertinggi yang dimiliki Andi: {maks}'

print(Maks(arr))


# ======================== Test Case ========================
''' Test Case 0 '''
N = 6
arr = [40, 25, 35, 50, 30, 45]
print(Maks(arr))

''' Test Case 1 '''
N = 8
arr = [20, 15, 30, 25, 40, 10, 35, 5]
print(Maks(arr))

''' Test Case 2 '''
N = 5
arr = [10, 20, 30, 40, 50]
print(Maks(arr))

''' Test Case 3 '''
N = 7
arr = [12, 18, 22, 15, 25, 20, 30]
print(Maks(arr))