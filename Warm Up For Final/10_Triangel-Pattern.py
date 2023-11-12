N = int(input())

# Piramid Kiri
for i in range(N):
    for _ in range(i+1):
        print('*',end='')
    print()

# Piramid Kanan
for i in range(N):
    for j in range(N-i-1):
        print(' ',end='')
            
    for j in range(i+1):
        print('*',end='')        
    print()