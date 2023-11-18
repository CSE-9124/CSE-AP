# Study Case 1
x = input('input = ')
res = []

for i in x.split('.'):
    y = str(int(i))
    res.append(y)
res = '.'.join(res)

print(res)


# Study Case 2
x = input()
h = len(x)

if h % 2 == 0:
    print(x.lower())
else:
    print(x.upper())


# Study Case 3
K = input('Masukkan Kalimat: ')
count = 0

for i in range(10):
    banyak = K.count(str(i))
    count += banyak

print(count)


# Study Case 4
x = input('')
kap = ''
low = ''
dig = ''
for i in x:
    if i.isupper():
        kap += i
    elif i.islower():
        low += i
    elif i.isdigit():
        dig += i

print(kap, low, dig)