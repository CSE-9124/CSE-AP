N = int(input())

if N <= 0:
    kelas = "A"
elif 0 < N <=100:
    kelas = "B"
elif 100 < N <= 200:
    kelas = "C"
elif N > 200:
    kelas = "D"

if N % 3 == 0:
    kluster = 1
elif N % 3 == 1:
    kluster = 2
elif N % 3 == 2:
    kluster = 3

kelaskluster = kelas + str(kluster)
print(kelaskluster)