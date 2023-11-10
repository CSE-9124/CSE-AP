# CARA 1 :
N = int(input())

for i in range(N):
    K1, K2 = map(int, input().split())
    A = list(map(int,input().split()))


    datang_awal = [i for i in A if i <= 0]

    if len(datang_awal) >= K2:
        print("LANJUTKAN ASISTENSI")
    elif len(datang_awal) < K2:
        print("DIBATALKAN")


# CARA 2 :
n = int(input())

status = []
for i in range(n):
    k1, k2 = map(int, input().split())
    a = list(map(int,input().split()))

    terlambat = 0
    for i in a:
        if i <= 0:
            terlambat +=1
    
    if terlambat > (k1-k2):
        status.append("LANJUT ASISTENSI")
    else:
        status.append("DIBATALKAN")

for i in status:
    print(i)


# CARA 3 :
telat, nontelat = 0, 0
jadi = []

N = int(input())

for i in range(N):
    K1, K2 = map(int, input().split())
    A = list(map(int, input().split()))

    for j in range(K1):
        if A[j] <= 0:
            nontelat += 1
        else:
            telat += 1

    if nontelat >= K2:
        jadi.append('LANJUT ASISTENSI')
    else:
        jadi.append('DIBATALKAN')

for x in jadi:
    print(x)