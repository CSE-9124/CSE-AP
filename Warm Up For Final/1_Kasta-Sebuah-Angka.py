N = int(input())
Kelas = ''
Kluster = ''

# Cari Kelas
if N <= 0 :
    Kelas += 'A'
elif 0 < N <= 100 :
    Kelas += 'B'
elif 100 < N <= 200 :
    Kelas += 'C'
else:
    Kelas += 'D'

# Cari Kluster
if N % 3 == 0 :
    Kluster += '1'
elif N % 3 == 1 :
    Kluster += '2'
elif N % 3 == 2 :
    Kluster += '3'

print(Kelas + Kluster)