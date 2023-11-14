

# CARA 1 : Menggunakan Import per
from itertools import permutations

n, k = map(int, input().split())

pos = list(range(1, n+1))

# Cari permutasi absolut terkecil
found = False
for p in permutations(pos):
    is_absolut = True
    for i in range(n):
        if abs(p[i] - (i+1)) != k:
            is_absolut = False
            break
    if is_absolut:
        print(*p)
        found = True
        break

# Jika tidak ada permutasi absolut yang ditemukan, cetak -1
if not found:
    print(-1)


# CARA 2 :
n, k = map(int, input().split())

def Permutasi_Absolut(n, k):
    pos = [0] * n
    
    for i in range(n):
        if i - k >= 0 and pos[i - k] == 0:
            pos[i - k] = i + 1
        elif i + k < n and pos[i + k] == 0:
            pos[i + k] = i + 1
        else:
            print('-1')
            break
    else:
        for i in pos:
            print(i, end=' ')

if k >= n :
    print('-1')
else:
    Permutasi_Absolut(n, k)