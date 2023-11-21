# Soal Nomor 3 : Menginput Informasi Daya Listrik dan Menghitung Total Tagihan Listrik
# CARA 1 :
Golongan = input('Golongan = ')
Daya = float(input('Daya = '))
Pemakaian = float(input('Pemakaian = '))

print()
match Golongan:
    case 'R1':
        if Daya == 900:
            tagihan = Pemakaian * 1352
            print(f'Jumlah tagihan anda sebesar : Rp. {f"{tagihan:,.1f}".replace(",", " ").replace(".", ",").replace(" ", ".")}')
        elif Daya == 1300:
            tagihan = Pemakaian * 1444.70
            print(f'Jumlah tagihan anda sebesar : Rp. {f"{tagihan:,.1f}".replace(",", " ").replace(".", ",").replace(" ", ".")}')
        elif Daya == 2200:
            tagihan = Pemakaian * 1444.70
            print(f'Jumlah tagihan anda sebesar : Rp. {f"{tagihan:,.1f}".replace(",", " ").replace(".", ",").replace(" ", ".")}')
        else:
            print('data tidak valid')
    case 'R2':
        if 3500 <= Daya <= 5500:
            tagihan = Pemakaian * 1699.53
            print(f'Jumlah tagihan anda sebesar : Rp. {f"{tagihan:,.1f}".replace(",", " ").replace(".", ",").replace(" ", ".")}')
        else:
            print('data tidak valid')
    case 'R3':
        if Daya >= 6600:
            tagihan = Pemakaian * 1699.53
            print(f'Jumlah tagihan anda sebesar : Rp. {f"{tagihan:,.1f}".replace(",", " ").replace(".", ",").replace(" ", ".")}')
        else:
            print('data tidak valid')
    case 'B2':
        if 6600 <= Daya <= 200000:
            tagihan = Pemakaian * 1444.70
            print(f'Jumlah tagihan anda sebesar : Rp. {f"{tagihan:,.1f}".replace(",", " ").replace(".", ",").replace(" ", ".")}')
        else:
            print('data tidak valid')
    case 'B3':
        if Daya > 200000:
            tagihan = Pemakaian * 1114.74
            print(f'Jumlah tagihan anda sebesar : Rp. {f"{tagihan:,.1f}".replace(",", " ").replace(".", ",").replace(" ", ".")}')
        else:
            print('data tidak valid')
    case 'I3':
        if Daya >= 200000:
            tagihan = Pemakaian * 1314.12
            print(f'Jumlah tagihan anda sebesar : Rp. {f"{tagihan:,.1f}".replace(",", " ").replace(".", ",").replace(" ", ".")}')
        else:
            print('data tidak valid')
    case 'P1':
        if 6600 <= Daya <= 200000:
            tagihan = Pemakaian * 1523.28
            print(f'Jumlah tagihan anda sebesar : Rp. {f"{tagihan:,.1f}".replace(",", " ").replace(".", ",").replace(" ", ".")}')
        else:
            print('data tidak valid')
    case _:
        print('data tidak valid')


# CARA 2 :
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