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
        print('*',end='')        
    print()