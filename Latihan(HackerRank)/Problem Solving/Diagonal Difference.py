# ======================== Information ========================
# Direct Link: https://www.hackerrank.com/challenges/diagonal-difference/problem
# Difficulty: Easy

# ======================== Solution ========================
# CARA 1 :
n = int(input())

matrix = []
for _ in range(n):
    x = list(map(int, input().split()))
    matrix.append(x)

d_utama = [matrix[i][i] for i in range(n)]
d_samp = [matrix[i][n-i-1] for i in range(n)]

s_utama = sum(d_utama)
s_samp = sum(d_samp)

print(abs(s_utama-s_samp))


# CARA 2 :
def diagonalDifference(M):
    n = len(M)
    u = sum([M[i][i] for i in range(n)])
    v = sum([M[i][n-i-1] for i in range(n)])

    return abs(u-v)

n = int(input())

arr = []
for i in range(n):
    x = list(map(int, input().split()))
    arr.append(x)

print(diagonalDifference(arr))


# ======================== Test Case ========================
n = 3
arr = [[11, 2, 4],
[4, 5, 6],
[10, 8, -12]]
print(diagonalDifference(arr))