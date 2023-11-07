import os
import datetime
import random

def Garis(n):
    print('=' * n)

# Membuat ID Transaksi
def Inisial_Nama(Nama):
    Huruf = Nama.title()
    Inisial = ''
    for i in Huruf:
        if i.isupper():
            Inisial += i
    return Inisial
def ID_Transaksi(Nama):
    Waktu = datetime.datetime.now()

    ID = f"{Inisial_Nama(Nama)}{Waktu.strftime('%y%m%d')}{Waktu.strftime('%H%M')}{random.randrange(100, 1000)}"
    return ID

# Tabel yang akan muncul di dalam File Transaksi
def waktu():
    waktu = datetime.datetime.now()
    Waktu = f'{waktu.strftime("%x %H:%M")}'
    return Waktu

def Tabel_Atas(Nama, Waktu):
    f.write(f"\n{f'TOKO {Nama.upper()}':^70}\n\n")

    f.write(f"{'=' * 70}\n")
    f.write(f"{'Nama kasir':<20}: {Nama}\n")
    f.write(f"{'Waktu transaksi':<20}: {Waktu}\n")
    f.write(f"{'=' * 70}\n\n")

    f.write(f"{'Daftar Produk':^70}\n\n")
    
    f.write(f"{60*'=':^70}\n")
    f.write(f"{5*' '}|{'Nama':^20}|{'Harga':^12}|{'Jumlah':^8}|{'Total':^15}|\n")
    f.write(f"{60*'=':^70}\n")
def Tabel_Transaksi(Nama, Harga, Jumlah, Total):
    for i in Produk:
        Nama, Harga, Jumlah, Total = i
        if len(Nama) >= 20:
            Nama = Nama[:15] + "..."

        f.write(f"{' ' * 5}| {Nama:<18} | {'Rp' + str(Harga):>10} |{Jumlah:^8}| {'Rp' + str(Total):>13} |\n")
def Tabel_Bawah(Total_Produk):
    f.write(f"{60 * '=':^70}\n")
    f.write(f"{' ' * 5}|{' ' * 7}{'TOTAL':<35}| {'Rp' + str(Total_Produk):>13} |\n") # 7+35+13+2+3 = 60
    f.write(f"{60 * '=':^70}\n\n")

    f.write(f"{'=' * 70}\n")
    f.write(f"{'TERIMA KASIH TELAH BERBELANJA':^70}\n")
    f.write(f"{'=' * 70}\n")

# Tabel yang akan muncul di dalam File Riwayat
def Riwayat_Transaksi():
    with open('trx_history.txt', 'w') as R:
        R.write(f"{'=' * 70}\n")
        R.write(f"|{'RIWAYAT TRANSAKSI':^68}|\n")
        R.write(f"{'=' * 70}\n")
        R.write(f"|{'Waktu':^18}|{'ID Transaksi':^24}|{'Nominal Transaksi':^24}|\n")
        R.write(f"{'=' * 70}\n")
def Tabel_Riwayat_Transaksi(Waktu, ID, Nominal):
    with open('trx_history.txt', 'a') as R:
        R.write(f"|{Waktu:^18}|{ID:^24}| {'Rp' + Nominal:>22} |\n")
        R.write(f"{'=' * 70}\n")


# BERIKUT YG AKAN MUNCUL DI TERMINAL
Garis(60)
print('SELAMAT DATANG'.center(60))
Garis(60)
Nama = input('Masukkan nama kasir \t: ')
Garis(60)

while True:
    print('''Pilih opsi:
1. Transaksi baru
2. Cari transaksi
3. Keluar ''')
    Garis(60)
    opsi = int(input('Masukkan opsi pilihan \t: '))
    Garis(60)

    match opsi:
        case 1:
            Produk = []
            Total_Produk = 0
            while True:
                Nama_Produk = str(input('Masukkan nama produk \t: '))
                Harga = int(input("Masukkan harga produk \t: "))            
                Jumlah = int(input("Masukkan jumlah produk \t: "))
                Total = Harga * Jumlah
                Garis(60)

                Total_Produk += Total
                Produk.append((Nama_Produk, Harga, Jumlah, Total))

                Tambah = input('Tambah Produk? (y/t) \t: ').lower()
                if Tambah == 'y':
                    Garis(60)
                    continue
                elif Tambah == 't':
                    Garis(60)
                    print('TRANSAKSI BERHASIL'.center(60))
                    Garis(60)

                    # Membuat File Transaksi
                    ID = ID_Transaksi(Nama)
                    Nama_File = f'{ID}.txt'
                    Nama_Folder = 'invoices'
                    File_Path = os.path.join(Nama_Folder, Nama_File)

                    Waktu = waktu()
                    
                    # Membuat Folder jika Foldernya belum ada
                    if not os.path.exists(Nama_Folder):
                        os.mkdir(Nama_Folder)
                    
                    f = open(File_Path, 'w')
                    
                    Tabel_Atas(Nama, Waktu)
                    Tabel_Transaksi(Nama_Produk, Harga, Jumlah, Total)
                    Tabel_Bawah(Total_Produk)
                    
                    f.close()

                    # Membuat File Riwayat jika File belum ada
                    if not os.path.exists('trx_history.txt'):
                        Riwayat_Transaksi()
                    
                    Nominal = str(Total_Produk)
                    Tabel_Riwayat_Transaksi(Waktu, ID, Nominal)

                    break
                else:
                    Garis(60)
                    print('Invalid pilihan')
                    break

        case 2:
            Cari = input('Masukkan ID transaksi \t: ')
            Nama_Folder = 'invoices'
            Cari_Path = os.path.join(Nama_Folder, f'{Cari}.txt')

            if os.path.exists(Cari_Path):
                with open(Cari_Path, "r") as file:
                    print('_' * 70)
                    print(f"\n{file.read()}")
                    print('_' * 70)   
            else:
                print(f"File dengan ID {Cari} tidak ditemukan")
        
        case 3:
            print('SAMPAI JUMPA'.center(60))
            Garis(60)
            break

        case _:
            print('Invalid Opsi'.center(60))
            Garis(60)
            break