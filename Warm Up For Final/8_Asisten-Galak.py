# CARA 1:
N = int(input())

for i in range(N):
    K1, K2 = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))

    on_time = sum(1 for a in A if a <= 0)


    if K1 - on_time > K2:
        print("DIBATALKAN")
    else:
        print("LANJUT ASISTENSI")


# CARA 2
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


# CARA 3
n = int(input())

status = []
for i in range(n):
    k1, k2 = map(int, input().split())
    a = list(map(int,input().split()))


    datang_awal = [i for i in a if i <= 0]

    if len(datang_awal) >= k2:
        print("DILANJUTKAN")
    elif len(datang_awal) < k2:
        print("DIBATALKAN")