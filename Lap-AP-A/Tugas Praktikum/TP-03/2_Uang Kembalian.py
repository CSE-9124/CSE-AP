# Soal 2 : Menghitung Kembalian dari Suatu Transaksi
# CARA 1:
harga = int(input('Harga Barang : '))
bayar = int(input('Nilai Uang :  '))
if bayar < harga:
   print('Nilai Uang Kurang!!!')
   exit()

kembalian = bayar - harga

Rp_100000 = 0
Rp_50000 = 0
Rp_20000 = 0
Rp_10000 = 0
Rp_5000 = 0
Rp_2000 = 0
Rp_1000 = 0

while kembalian > 0:
   if kembalian >= 100000:
      Rp_100000 += 1
      kembalian -= 100000
   elif kembalian >= 50000:
      Rp_50000 += 1
      kembalian -= 50000
   elif kembalian >= 20000:
      Rp_20000 += 1
      kembalian -= 20000
   elif kembalian >= 10000:
      Rp_10000 += 1
      kembalian -= 10000
   elif kembalian >= 5000:
      Rp_5000 += 1
      kembalian -= 5000
   elif kembalian >= 2000:
      Rp_2000 += 1
      kembalian -= 2000
   elif kembalian >= 1000:
      Rp_1000 += 1
      kembalian -= 1000

print(f'{Rp_100000} uang sejumlah Rp.100000')
print(f'{Rp_50000} uang sejumlah Rp.50000')
print(f'{Rp_20000} uang sejumlah Rp.20000')
print(f'{Rp_10000} uang sejumlah Rp.10000')
print(f'{Rp_5000} uang sejumlah Rp.5000')
print(f'{Rp_2000} uang sejumlah Rp.2000')
print(f'{Rp_1000} uang sejumlah Rp.1000')

# CARA 2:
Harga = int(input('Harga Barang : '))
Bayar = int(input('Nilai Uang : '))
Kembalian = Bayar - Harga

Uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000]

for Banyak in Uang:
   Jumlah = Kembalian // Banyak 
   Kembalian = Kembalian % Banyak
   print(f'{Jumlah} uang sejumlah Rp.{Banyak}')