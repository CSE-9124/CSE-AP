# Soal Nomor 1 : Menghitung Luas dan Keliling Segitiga Siku-Siku
print ('Menghitung luas permukaan dan keliling segitiga')
X = float(input('Panjang sisi X : '))
Y = float(input('Panjang sisi Y : '))
Z = (X**2 + Y**2)**0.5

L = X * Y / 2
K = X + Y + Z
print(f'Luas Permukaan : {L:.2f}')
print(f'Keliling : {K:.2f}')