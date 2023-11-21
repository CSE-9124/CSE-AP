# Soal Nomor 2 : Mengkonversi Suhu Celcius ke Kelvin, Reamur, dan Fahrenheit
print('Konversi Suhu dari Celcius ke Kelvin, Reamur dan Fahrenheit')
C = int(input('Masukkan Suhu dalam Celcius : '))

K = int(C + 273)            # Konversi ke Suhu Kelvin
R = int(4/5 * C)            # Konversi ke Suhu Reamur
F = int((C * 9/5) + 32)     # Konversi ke Suhu Fahrenheit

print (f'Hasil konversi dari suhu {C} derajat Celcius ke Kelvin adalah : {K}K')
print (f'Hasil konversi dari suhu {C} derajat Celcius ke Reamur adalah : {R}R')
print (f'Hasil konversi dari suhu {C} derajat Celcius ke Fahrenheit adalah {F}F')