'''String Manipulation dalam python adalah sebuah cara yang digunakan untuk
memodifikasi sebuah string atau membuat string baru dengan membuat perubahan pada string
yang telah dibuat. '''

# Mengakses Karakter dalam String
'''kelas = 'IPA'
huruf = kelas[1]
print('Hurufnya adalah', huruf)
'''

# Menentukan Panjang String "len()"
'''kelas = 'IPS'
panjang = len(kelas)
print('Panjang huruf adlah', panjang)
'''

# Menemukan Karakter pada String "Method.find()"
'''kelas = 'Keep Safe'
character = 'S'
position = kelas.find(character)
print('Posisi karakter ada pada indeks ke', position)
'''

# Menemukan Frekuensi/Banyak Karakter pada String "Method.count()" 
'''kelas = 'Keep Safe'
character = 'e'
position = kelas.count(character)
print('Posisi karakter ada pada indeks ke', position)
'''

# Menghitung Jumlah Spasi pada String "Method.count()"
'''kelas = 'Keep Safe and be Smart'
character = ' '
position = kelas.count(character)
print('Posisi karakter ada pada indeks ke', position)
'''

# String Slicing
'''word = 'Hello World'

print(word[0]) #Mendapatkan Karakter Pertama
print(word[0:1]) #Mendapatkan Karakter Pertama
print(word[0:3]) #Mendapatkan Tiga Karakter Pertama
print(word[:3]) #Mendapatkan Tiga Karakter Pertama
print(word[-3:]) #Mendapatkan Tiga Karakter Pertama
print(word[3:]) #Mendapatkan Kseseluruhan Karakter kecuali Tiga Karakter Pertama
print(word[:-3]) #Mendapatkan Kseseluruhan Karakter kecuali Tiga Karakter Terakhir
'''

# Memeriksa apakah String DIMULAI dengan / DIAKHIRI dengan Karakter
'''# 1. Metode ".stratwith()"
word = 'Hello World'

awal = word.startswith('H')
print(awal) # Output True
awal = word.startswith('l')
print(awal) # Output False '''

'''# 2. Metode ".endswith()"
word = 'Hello World'

akhir = word.endswith('d')
print(akhir) # Output True
akhir = word.endswith('l')
print(akhir) # Output False '''

# Membuat String Berulang
'''word = 'Hello World'
berulang = word * 4
print(berulang)
'''

# Mengganti Substring "Method.replace()"
'''word = 'Hello World'
baru = word.replace('World', 'Dunia')
print(baru) # Output Hello Dunia
'''

# Mengubah String Huruf Besar dan Kecil
'''# 1. Metode ".upper()"
kecil = 'Hello World'
baru = kecil.upper()
print(baru) '''

'''# 2. Metode ".lower()"
baru = kecil.lower()
print(baru) '''

'''# 3. Metode ".title()"
baru = kecil.title()
print(baru) '''

'''# 4. Metode ".capitalize()"
baru = kecil.capitalize()
print(baru) '''

'''# 5. Metode ".swapcase()"
baru = kecil.swapcase()
print(baru) '''