# # Soal 1 : Menghasilkan Jumlah Suku Fibonacci
# Suku = int(input())
# n1 = 0
# n2 = 1
# s = 0

# if Suku > 0 :
#     while s < Suku :
#         print(n1, end=" ")
#         Un = n1 + n2
#         n1 = n2 
#         n2 = Un
#         s += 1        
# elif Suku == 1:
#     print(n1)
# else:
#     print('Input Bilangan Positif')


# Soal 2 : Menghitung Kembalian dari Suatu Transaksi
# harga = int(input('Harga Barang : '))
# bayar = int(input('Nilai Uang :  '))

# kembalian = bayar - harga

# Rp_100000 = 0
# Rp_50000 = 0
# Rp_20000 = 0
# Rp_10000 = 0
# Rp_5000 = 0
# Rp_2000 = 0
# Rp_1000 = 0

# while kembalian > 0:
#    if kembalian >= 100000:
#       Rp_100000 += 1
#       kembalian -= 100000
#    elif kembalian >= 50000:
#       Rp_50000 += 1
#       kembalian -= 50000
#    elif kembalian >= 20000:
#       Rp_20000 += 1
#       kembalian -= 20000
#    elif kembalian >= 10000:
#       Rp_10000 += 1
#       kembalian -= 10000
#    elif kembalian >= 5000:
#       Rp_5000 += 1
#       kembalian -= 5000
#    elif kembalian >= 2000:
#       Rp_2000 += 1
#       kembalian -= 2000
#    elif kembalian >= 1000:
#       Rp_1000 += 1
#       kembalian -= 1000

# print(f'{Rp_100000} uang sejumlah Rp.100000')
# print(f'{Rp_50000} uang sejumlah Rp.50000')
# print(f'{Rp_20000} uang sejumlah Rp.20000')
# print(f'{Rp_10000} uang sejumlah Rp.10000')
# print(f'{Rp_5000} uang sejumlah Rp.5000')
# print(f'{Rp_2000} uang sejumlah Rp.2000')
# print(f'{Rp_1000} uang sejumlah Rp.1000')

# CARA 2:
# Harga = int(input('Harga Barang : '))
# Bayar = int(input('Nilai Uang : '))
# Kembalian = Bayar - Harga

# Uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000]
# Banyak = [0]*7
     


# Soal 3 :
# while True:
#    M = float(input())
#    if 0 <= M < 360:
#       break
#    else:
#       print('End Of File')

# Detik = int(M * 240) # 1 derajat sama dengan 4 menit (240 detik)

# Jam = Detik // 3600 + 6
# if Jam >= 24:
#    Jam = Jam % 24
# Menit = Detik % 3600 // 60
# Detik = Detik % 60

# if 6 <= Jam < 11:
#    print('Selamat Pagi')
# elif 11 <= Jam < 15 :
#    print('Selamat Siang')
# elif 15 <= Jam < 18:
#    print('Selamat Sore')
# else:
#    print('Selamat Malam')

# print(f'{Jam:02}:{Menit:02}:{Detik:02}')