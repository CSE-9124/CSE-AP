# Soal Nomor 1 : Menghitung Luas dan Keliling Segitiga Siku-Siku
print ('Menghitung luas permukaan dan keliling segitiga')
X = float(input('Panjang sisi X : '))
Y = float(input('Panjang sisi Y : '))
Z = (X**2 + Y**2)**0.5

L = X * Y / 2
K = X + Y + Z
print(f'Luas Permukaan : {L:.2f}')
print(f'Keliling : {K:.2f}')

# Soal Nomor 2 : Mengkonversi Suhu Celcius ke Kelvin, Reamur, dan Fahrenheit
print('Konversi Suhu dari Celcius ke Kelvin, Reamur dan Fahrenheit')
C = int(input('Masukkan Suhu dalam Celcius : '))

K = int(C + 273)
R = int(4/5 * C)
F = int((C * 9/5) + 32)

print (f'Hasil konversi dari suhu {C} derajat Celcius ke Kelvin adalah : {K}K')
print (f'Hasil konversi dari suhu {C} derajat Celcius ke Reamur adalah : {R}R')
print (f'Hasil konversi dari suhu {C} derajat Celcius ke Fahrenheit adalah {F}F')

# Soal Nomor 3 : Menghitung Solusi Persamaan Kuadrat
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

# Soal Nomor 4 : Menentukan Karakter Huruf Kapital, Huruf Kecil, dan Angka
print('Pengujian jenis karakter')
print('------------------------')
Karakter = (input('Karakter = '))

uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'F', 'W', 'X', 'Y', 'Z']
lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'f', 'w', 'x', 'y', 'z']
digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',]

kapital = Karakter in uppercase
kecil = Karakter in lowercase
angka = Karakter in digit

print('Huruf kapital?', kapital)
print('Huruf kecil?', kecil)
print('Angka?', angka)

# Soal Nomor 5 : Merubah detik ke dalam format jam:menit:detik
print('konversi detik ke jam')
Detik = int(input('Masukkan jumlah detik: '))

jam = Detik // 3600
menit = Detik % 3600 // 60
detik = Detik % 60

print(f"{jam:02}:{menit:02}:{detik:02}")