# Soal Nomor 3 : Menghitung Solusi Persamaan Kuadrat
# CARA 1
a = float(input('Input a = '))
if a == 0:
    print('Error!! Input nilai a ≠ 0')
    exit()

b = float(input('Input b = '))
c = float(input('Input c = '))

x1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
x2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)

print(f'x1 = {x1:.2f}')
print(f'x2 = {x2:.2f}')

# CARA 2
import math
A = int(input('Input a = '))
if A == 0:
    print('Error!! Input nilai a ≠ 0')
    exit()
B = int(input('Input b = '))
C = int(input('Input c = '))

akar = math.sqrt(B**2 - 4*A*C)
X1 = -B + akar / (2*A)
X2 = -B - akar / (2*A)

print(f'X1 = {X1:.2f}'
f'X2 = {X2:.2f}')