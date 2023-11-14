'''Soal :  menghitung jumlah bilangan ganjil antara dua angka, yaitu angka awal ( i ) dan angka akhir ( j )
yang diberikan. Program kemudian harus mencetak total hasil penjumlahan dari setiap bilangan ganjil 
berdasarkan rentang awal dan akhir yang diberikan.'''

i = int(input())
j = int(input())

if i < 0 or j < 0 or i > j:
    print('Inputan harus >= 0 dan i < j')
else:
    k = 0
    for x in range(i, j+1):
        if x % 2 != 0:
            k += x
    print(f'Total hasil penjumlahan setiap bilangan ganjil antara {i} dan {j} adalah {k}')