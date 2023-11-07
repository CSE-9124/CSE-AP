# CARA 1 :
Tahun = int(input('Tahun = '))
if (Tahun % 4 == 0 and Tahun % 100 != 0) or (Tahun % 400 == 0):
    print(f'{Tahun} adalah Tahun Kabisat')
else:
    print(f'{Tahun} bukan Tahun Kabisat')

# CARA 2 (3 Baris):
tahun = int(input('Tahun : '))
Tahun = 'adalah tahun kabisat' if tahun%4 == 0 and tahun%100 != 0 or tahun%400 == 0 else 'bukan tahun kabisat'
print(Tahun)

# CARA 3 (Menggunakan Nested If) :
year = int(input('Tahun = '))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('leap year')
        else: 
            print('not leap year')
    else: 
        print('leap year')
else: 
    print('not leap year')