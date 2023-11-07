import os
import datetime
import random

def GGG():
    print('='*70)

def createHistory():
    """fungsi untuk membuat file history dan juga tabelnya"""
    with open('history', 'w') as file:
        file.write(f"{'='*70}\n")
        file.write(f"|{'RIWAYAT TRANSAKSI':^68}|\n")
        file.write(f"{'='*70}\n")
        file.write(f"|{'Waktu':^18}|{'ID Transaksi':^24}|{'Nominal Transaksi':^24}|\n")
        file.write(f"{'='*70}\n")
        file.close()

def addHistory(waktu, id, nominal):
    """fungsi untuk menambah isi dari history transaksi"""
    with open('history','a') as file:
        file.write(f"|{waktu:^18}|{id:^24}|{'Rp' + nominal:^24}|\n")
        file.write(f"{'-'*70}\n")

def atasanStruk(nama, waktu):
    """fungsi untuk membuat bagian atas dari format transaksi termasuk tabel"""
    data.write(f"{'TOKO CHINA':^70}\n\n")
    data.write(f"{'='*70}\n")
    data.write(f"Nama kasir \t\t: {nama}\n")
    data.write(f"Waktu transaksi \t: {waktu}\n")
    data.write(f"{'='*70}\n\n")
    data.write(f"{'Daftar Produk':^70}\n\n")
    data.write(f"{60*'=':^70}\n")
    data.write(f"{5*' '}|{'Nama':^20}|{'Harga':^12}|{'Jumlah':^8}|{'Total':^15}|\n")
    data.write(f"{60*'=':^70}\n")

def addStruk(nama, harga, jumlah, total):
    """fungsi untuk menambah isi dari transaksi"""
    if len(nama) > 20:
        nama = nama[:17] + "..."
    data.write(f"{5*' '}|{nama:<20}|{'Rp' + str(harga):^12}|{jumlah:^8}|{'Rp' + str(total):>15}|\n")

def bawahanStruk(total_belanja):
    """fungsi untuk membuat bagian bawah dari format transaksi termasuk total transaksi"""
    data.write(f"{60*'=':^70}\n")
    data.write(f"{' '*5}|{'TOTAL':^42}|{'Rp' + str(total_belanja):>15}|\n")
    data.write(f"{60*'=':^70}\n\n")
    data.write(f"{'='*70}\n")
    data.write(f"{'TERIMA KASIH TELAH BERBELANJA':^70}\n")
    data.write(f"{'='*70}\n")

def id(kasir):
    """fungsi untuk membuat id file berdasarkan format yang telah ditentukan"""
    nama = kasir.upper().replace(" ","")
    nama =  nama[0] + nama[len(nama)//2] + nama[-1]
    waktu = datetime.datetime.now()
    tahun = str(waktu.year)
    bulan = str(waktu.month)
    hari = str(waktu.day)
    jam = str(waktu.hour)
    menit = str(waktu.minute)
    kode = str(random.randint(100,999))
    while len(kode) < 3:
        kode = str(random.randint(100,999))

    file_name = nama + tahun[-2:] + bulan + hari + jam + menit + kode 
    return file_name

def waktu():
    """fungsi untuk mengambil data berupa waktu tahun bulan hari jam dan menit"""
    waktu = str(datetime.datetime.now())
    waktu = waktu[2:16].replace("-","/")
    return waktu

folder_path = "Invoices"

GGG()
print('SELAMAT DATANG'.center(70))
GGG()
kasir = input("Masukkan nama Kasir\t: ")

#jika folder history belum ada maka buat dulu
if not os.path.exists("history"):
    createHistory()

while True:
    GGG()
    print('Pilih opsi:\n1. Transaksi baru\n2. Cari transaksi\n3. Keluar')
    GGG()
    opsi = int(input("Masukkkan opsi pilihan\t: "))
    GGG()
    match opsi:
        case 1:
            ID = id(kasir)
            file_name = ID + ".txt"
            file_path = os.path.join(folder_path, file_name)

            # jika folder tidak ada maka di buat dulu
            if not os.path.exists(folder_path):
                os.mkdir(folder_path)
            
            data = open(file_path, "a")
            WAKTU = waktu() #diubah menjadi variabel agar bisa masuk kedalam fungsi
            atasanStruk(kasir, WAKTU)

            total_belanja = 0
            
            while True:
                nama = input("Masukkan nama produk\t: ")
                harga = int(input("Masukkan harga produk\t: "))
                jumlah = int(input("Masukkan jumlah produk\t: "))
                GGG()
                total_barang = harga * jumlah
                total_belanja += total_barang

                # invoices
                addStruk(nama, harga, jumlah, total_barang)

                #tambah jumlah belanja
                isTambah = input("Tambah produk? (y/t)\t: ")
                if isTambah == 't':
                    bawahanStruk(total_belanja)
                    data.close()
                    GGG()
                    print(f"{'TRANSAKSI BERHASIL':^70}")
                    break
                GGG()

            # riwayat transaksi
            NOMINAL = str(total_belanja)
            addHistory(WAKTU, ID, NOMINAL)

        case 2:
            cari = input("Masukkan ID file transaksi : ")
            cari_path = folder_path + "/" + cari + ".txt"
            if os.path.exists(cari_path):
                with open(cari_path, "r") as file:
                    GGG()
                    print(f"\n\n{file.read()}")
            else:
                print(f"File dengan ID {cari} tidak ditemukan")

        case 3:
            print(f"SEE YOU {kasir.upper()}".center(70))
            GGG()
            break
    
        case _:
            print("INPUT TIDAK VALID".center(70))