# # Soal Nomor 1 : Menghitung BMI yang dibedakan berdasarkan gendernya
# print('''Pilih Gender Anda
# 1. Pria 
# 2. Wanita''')
# choice = int(input('= '))
# if choice != 1 and choice != 2:
#     print('Gender Tidak Valid')
#     exit() 

# Tinggi = float(input('Masukkan tinggi badan (cm) : '))
# Berat = float(input('Masukkan berat badan (kg) : '))

# Tinggi /= 100 # Ubah Tinggi badan dari cm ke m

# BMI = Berat / (Tinggi)**2

# print()
# if choice == 1:
#     if BMI < 18:
#         print(f'Anda Tergolong Underweight dengan BMI {BMI:.2f}')
#     elif 18 <= BMI <= 23.9:
#         print(f'Anda Tergolong Normal dengan BMI {BMI:.2f}')
#     elif 24 <= BMI < 26.9:
#         print(f'Anda tergolong Overweight dengan BMI {BMI:.2f}')
#     else:
#         print(f'Anda tergolong Obese dengan BMI {BMI:.2f}')
# elif choice == 2:
#     if BMI < 17:
#         print(f'Anda Tergolong Underweight dengan BMI {BMI:.2f}')
#     elif 17 <= BMI < 23.9:
#         print(f'Anda Tergolong Normal dengan BMI {BMI:.2f}')
#     elif 24 <= BMI < 27.9:
#         print(f'Anda tergolong Overweight dengan BMI {BMI:.2f}')
#     else:
#         print(f'Anda tergolong Obese dengan BMI {BMI:.2f}')
# else:
#     print('Gender Tidak Valid')

# # Soal Nomor 2 :
# First = input('Masukkan Input Pertama : ')
# Second = input('Masukkan Input Kedua : ')
# Third = input('Masukkan Input Ketiga : ')

# print()
# if First == 'vertebrado':
#     if Second == 'ave':
#         if Third == 'carnivoro':
#             print('aguia')
#         elif Third == 'onivoro':
#             print('pomba')
#         else:
#             print('Invalid Input')
#     elif Second == 'mamifero':
#         if Third == 'onivoro':
#             print('homem')
#         elif Third == 'herbivoro':
#             print('vaca')
#         else:
#             print('Invalid Input')
#     else:
#         print('Invalid Input')
# elif First == 'invertebrado':
#     if Second == 'inseto':
#         if Third == 'hematofago':
#             print('pulga')
#         elif Third == 'herbivoro':
#             print('lagarta')
#         else:
#             print('Invalid Input')
#     elif Second == 'anilideo':
#         if Third == 'hematofago':
#             print('sanguessuga')
#         elif Third == 'onivoro':
#             print('minhoca')
#         else:
#             print('Invalid Input')
#     else:
#         print('Invalid Input')
# else:
#     print('Invalid Input')

# # Soal Nomor 3 :
# Golongan = input('Golongan = ')
# Daya = float(input('Daya = '))
# Pemakaian = float(input('Pemakaian = '))

# print()
# match Golongan:
#     case 'R1':
#         if Daya == 900:
#             tagihan = Pemakaian * 1352
#             print(f'Jumlah tagihan anda sebesar : Rp. {tagihan:,.1f}')
#         elif Daya == 1300:
#             tagihan = Pemakaian * 1444.70
#             print(f'Jumlah tagihan anda sebesar : Rp. {tagihan:,.1f}')
#         elif Daya == 2200:
#             tagihan = Pemakaian * 1444.70
#             print(f'Jumlah tagihan anda sebesar : Rp. {tagihan:,.1f}')
#         else:
#             print('data tidak valid')
#     case 'R2':
#         if 3500 <= Daya <= 5500:
#             tagihan = Pemakaian * 1699.53
#             print(f'Jumlah tagihan anda sebesar : Rp. {tagihan:,.1f}')
#         else:
#             print('data tidak valid')
#     case 'R3':
#         if Daya >= 6600:
#             tagihan = Pemakaian * 1699.53
#             print(f'Jumlah tagihan anda sebesar : Rp. {tagihan:,.1f}')
#         else:
#             print('data tidak valid')
#     case 'B2':
#         if 6600 <= Daya <= 200000:
#             tagihan = Pemakaian * 1444.70
#             print(f'Jumlah tagihan anda sebesar : Rp. {tagihan:,.1f}')
#         else:
#             print('data tidak valid')
#     case 'B3':
#         if Daya > 200000:
#             tagihan = Pemakaian * 1114.74
#             print(f'Jumlah tagihan anda sebesar : Rp. {tagihan:,.1f}')
#         else:
#             print('data tidak valid')
#     case 'I3':
#         if Daya >= 200000:
#             tagihan = Pemakaian * 1314.12
#             print(f'Jumlah tagihan anda sebesar : Rp. {tagihan:,.1f}')
#         else:
#             print('data tidak valid')
#     case 'P1':
#         if 6600 <= Daya <= 200000:
#             tagihan = Pemakaian * 1523.28
#             print(f'Jumlah tagihan anda sebesar : Rp. {tagihan:,.1f}')
#         else:
#             print('data tidak valid')

# Soal Nomor 3 : (Alternative)
Golongan = input('Golongan = ')
Daya = int(input('Daya = '))
Pemakaian = int(input('Pemakaian = '))

print()
match Golongan:
    case 'R1':
        if Daya == 900:
            kwh = 1352
        elif Daya == 1300:
            kwh = 1444.70
        elif Daya == 2200:
            kwh = 1444.70
        else:
            print('data tidak valid')
    case 'R2':
        if 3500 <= Daya <= 5500:
            kwh = 1699.53
        else:
            print('data tidak valid')
    case 'R3':
        if Daya >= 6600:
            kwh = 1699.53
        else:
            print('data tidak valid')
    case 'B2':
        if 6600 <= Daya <= 200000:
            kwh = 1444.70
        else:
            print('data tidak valid')
    case 'B3':
        if Daya > 200000:
            kwh = 1114.74
        else:
            print('data tidak valid')
    case 'I3':
        if Daya >= 200000:
            kwh = 1314.12
        else:
            print('data tidak valid')
    case 'P1':
        if 6600 <= Daya <= 200000:
            kwh = 1523.28
        else:
            print('data tidak valid')

tagihan = Pemakaian * kwh

tagihan_STR = str(round(tagihan,1))
if "." in tagihan_STR:
    nobulat, decimal = (tagihan_STR).split(".")
    print (f"{int(nobulat):,.0f}".replace("," , ".")+","+ decimal)
else:
    print (f"{int(tagihan_STR):,.0f}".replace(",","."))