Angka = list(map(int, input('Masukkan beberapa angka: ').split(' ')))

# CARA 1:
Kelompok1 = []
Kelompok2 = []
Kelompok3 = []

for Num in Angka:
    if Num % 2 == 0:
        Kelompok1.append(Num)
    else:
        Kelompok2.append(Num)

    if Num % 5 == 0:
        Kelompok3.append(Num)

print(f'''
Angka Genap: {Kelompok1}
Angka Ganjil: {Kelompok2}
Angka yang habis dibagi 5: {Kelompok3}''')


# CARA 2: Menggunakan List Comprehension
Klmpk1 = [x for x in Angka if x % 2 == 0]
Klmpk2 = [x for x in Angka if x % 2 != 0]
Klmpk3 = [x for x in Angka if x % 5 == 0]

print(f'''
Angka Genap: {Klmpk1}
Angka Ganjil: {Klmpk2}
Angka yang habis dibagi 5: {Klmpk3}''')