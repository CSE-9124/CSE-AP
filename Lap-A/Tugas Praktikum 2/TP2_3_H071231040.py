# Soal Nomor 3 :
Golongan = input('Golongan = ')
Daya = float(input('Daya = '))
Pemakaian = float(input('Pemakaian = '))

print()
match Golongan:
    case 'R1':
        if Daya == 900:
            tagihan = Pemakaian * 1352
            print(f'Jumlah tagihan anda sebesar : Rp. {tagihan:,.1f}')
        elif Daya == 1300:
            tagihan = Pemakaian * 1444.70
            print(f'Jumlah tagihan anda sebesar : Rp. {tagihan:,.1f}')
        elif Daya == 2200:
            tagihan = Pemakaian * 1444.70
            print(f'Jumlah tagihan anda sebesar : Rp. {tagihan:,.1f}')
        else:
            print('data tidak valid')
    case 'R2':
        if 3500 <= Daya <= 5500:
            tagihan = Pemakaian * 1699.53
            print(f'Jumlah tagihan anda sebesar : Rp. {tagihan:,.1f}')
        else:
            print('data tidak valid')
    case 'R3':
        if Daya >= 6600:
            tagihan = Pemakaian * 1699.53
            print(f'Jumlah tagihan anda sebesar : Rp. {tagihan:,.1f}')
        else:
            print('data tidak valid')
    case 'B2':
        if 6600 <= Daya <= 200000:
            tagihan = Pemakaian * 1444.70
            print(f'Jumlah tagihan anda sebesar : Rp. {tagihan:,.1f}')
        else:
            print('data tidak valid')
    case 'B3':
        if Daya > 200000:
            tagihan = Pemakaian * 1114.74
            print(f'Jumlah tagihan anda sebesar : Rp. {tagihan:,.1f}')
        else:
            print('data tidak valid')
    case 'I3':
        if Daya >= 200000:
            tagihan = Pemakaian * 1314.12
            print(f'Jumlah tagihan anda sebesar : Rp. {tagihan:,.1f}')
        else:
            print('data tidak valid')
    case 'P1':
        if 6600 <= Daya <= 200000:
            tagihan = Pemakaian * 1523.28
            print(f'Jumlah tagihan anda sebesar : Rp. {tagihan:,.1f}')
        else:
            print('data tidak valid')
    case _:
        print('data tidak valid')

