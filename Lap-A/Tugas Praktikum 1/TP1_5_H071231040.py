# Soal Nomor 5 : Merubah detik ke dalam format jam:menit:detik
print('konversi detik ke jam')
Detik = int(input('Masukkan jumlah detik: '))

jam = Detik // 3600
menit = Detik % 3600 // 60
detik = Detik % 60

print(f"{jam:02}:{menit:02}:{detik:02}")