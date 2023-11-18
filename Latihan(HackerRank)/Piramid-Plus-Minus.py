def pola():
    for i in range(1, n+1):
        for j in range(i):
            if (j + i) % 2 == 0:
                print('-', end='')
            else:
                print('+', end='')
        print()

n = int(input())
if 1 <= n <= 10:
    pola()
else:
    print('Error!!')