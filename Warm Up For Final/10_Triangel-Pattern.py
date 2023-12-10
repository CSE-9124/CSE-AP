N = int(input())

''' PIRAMID KIRI '''
for i in range(N):
    for _ in range(i+1):
        print('*',end='')
    print()

''' PIRAMID KANAN '''
for i in range(N):
    for j in range(N-i-1):
        print(' ',end='')
            
    for j in range(i+1):
        print('* ',end='')        
    print()

''' PIRAMID TENGAH '''
for i in range(N, 0, -1):
    print(" " * (i - 1) + "*" * ((N + 1) - i) + "*" * (N - i))