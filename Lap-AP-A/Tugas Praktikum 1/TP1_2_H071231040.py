# Soal Nomor 2 : Mengkonversi Suhu Celcius ke Kelvin, Reamur, dan Fahrenheit
print('Konversi Suhu dari Celcius ke Kelvin, Reamur dan Fahrenheit')
C = int(input('Masukkan Suhu dalam Celcius : '))

K = int(C + 273)
R = int(4/5 * C)
F = int((C * 9/5) + 32)

print (f'Hasil konversi dari suhu {C} derajat Celcius ke Kelvin adalah : {K}K')
print (f'Hasil konversi dari suhu {C} derajat Celcius ke Reamur adalah : {R}R')
print (f'Hasil konversi dari suhu {C} derajat Celcius ke Fahrenheit adalah {F}F')