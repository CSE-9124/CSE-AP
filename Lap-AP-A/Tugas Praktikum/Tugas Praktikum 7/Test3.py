import os
import datetime
import random

def Inisial_Nama(Nama):
    Huruf = Nama.title()
    Inisial = ''
    for i in Huruf:
        if i.isupper():
            Inisial += i
    return Inisial
    # for i in Huruf:
    #     Inisial += i[0].upper()
    # return Inisial

def ID_Transaksi(Nama):
    Tanggal = datetime.datetime.now()
    Waktu = datetime.datetime.now()

    ID = f"{Inisial_Nama(Nama)}{Tanggal.strftime('%y%m%d')}{Waktu.strftime('%H%M')}{random.randrange(100, 1000)}"
    return ID

def Garis():
    print("=" * 60)

def Buat_File(ID,Nama,Produk):
    Nama_File = f'{ID}.txt'
    Nama_Folder = 'invoices'
    File_path = os.path.join(Nama_Folder, Nama_File)
    Tanggal = datetime.datetime.now()

    if not os.path.exists(Nama_Folder):
        os.mkdir(Nama_Folder)
    
    with open(File_path, 'w') as f:
        f.write('\n')
        f.write(f'TOKO {Nama}'.center(60))
        f.write(Garis() + '\n')
        f.write(f'Nama kasir               : {Nama}')
        f.write(f'Waktu transaksi          : {Tanggal.strftime("%x")} {Tanggal.strftime("%H")}:{Tanggal.strftime("%M")}')
        f.write(Garis() + '\n\n')
        f.write('Daftar Produk'.center(60))
        f.write('\n\n' + Garis())
        

Garis()
print('SELAMAT DATANG'.center(60))
Garis()
Nama = input('Masukkan Nama Kasir      : ')
Garis()


while True:
    produk = {}

    print('''Pilih opsi:
1. Transaksi baru
2. Cari transaksi
3. Keluar ''')
    Garis()
    opsi = int(input('Masukkan opsi pilihan    : '))
    Garis()
    
    match opsi:
        case 1: # Soal 1
            while True:
                Nama_Produk = str(input('Masukkan nama produk     : '))
                if not Nama_Produk:
                    break

                Harga = int(input("Masukkan harga produk    : "))            
                Jumlah = int(input("Masukkan jumlah produk   : "))
                Total = Harga * Jumlah
                Garis()

                produk[Nama_Produk] = [Nama_Produk]

                produk[Nama_Produk].append(Harga)
                produk[Nama_Produk].append(Jumlah)
                produk[Nama_Produk].append(Total)
                
                Tambah = input('Tambah Produk? (y/t)     : ').lower()
                if Tambah == 'y':
                    Garis()
                    continue
                elif Tambah == 't':
                    Garis()
                    print('TRANSAKSI BERHASIL'.center(60))
                    Garis()
                    break



print(produk)
print(Inisial_Nama(Nama))