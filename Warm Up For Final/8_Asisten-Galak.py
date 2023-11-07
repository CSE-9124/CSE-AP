N = int(input())

for i in range(N):
    K1, K2 = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))

    on_time = sum(1 for a in A if a >= 0)


    if K1 - on_time > K2:
        print("DIBATALKAN")
    else:
        print("LANJUT ASISTENSI")