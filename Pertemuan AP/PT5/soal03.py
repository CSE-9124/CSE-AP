# CARA 1:
def pola(a):
    a = int(a)
    for b in range (a):
        if b % 2 == 0:
            for c in range(b + 1):
                if c % 2 == 0:
                    print('+', end='')
                else:
                    print('-', end='')
        elif b % 2 != 0:
            for c in range(b + 1):
                if c % 2 == 0:
                    print('-', end='')
                else:
                    print('+', end='')
        print()

x = int(input())
if 1 <= x <= 10:
    print(pola(x))
else: print('Error!!!')


# CARA 2:
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


# CARA 3 :
def piramida():
    for baris in range (1, meow + 1):
        for kolom in range (baris):
            if (baris + kolom) % 2 == 0:
                print('-', end='')
            else:
                print('+', end='')
        print()

meow = int(input())
if 1 <= meow <= 10:
    piramida()
else:
    print('error')