''' MINI DIAMOND '''
def Diamond(rows):
    for i in range(1, rows + 1):
        print(' ' * (rows - i) + '*' * (2 * i - 1))

    for i in range(rows - 1, 0, -1):
        print(' ' * (rows - i) + '*' * (2 * i - 1))

rows = int(input())
Diamond(rows)


''' BIG DIAMOND '''
def Diamond(rows):
    k = 2 * rows - 2
    for i in range(rows):
        for j in range(k):
            print(end=' ')
        k -= 1
        for j in range(i + 1):
            print('*', end=' ')
        print('\r')
    
    k = rows - 2
    for i in range(rows, -1, -1):
        for j in range(k, 0, -1):
            print(end=' ')
        k += 1
        for j in range(i + 1):
            print('*', end=' ')
        print('\r')

rows = int(input())
Diamond(rows)