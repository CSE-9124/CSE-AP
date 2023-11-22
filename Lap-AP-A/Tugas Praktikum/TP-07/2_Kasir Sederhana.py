import os
from datetime import datetime
import random

def Garis(s, n):
    return f'{str(s) * int(n)}'

def transaksiBaru(n, x, t): # 'n' untuk parameter ID; 'x' untuk parameter list data produk; dan 't' untuk parameter total harga produk
    if len(x) == 0: # Jika 'x' kosong alias user tidak tambah produk, maka list data produk dikosongkan
        dataProduk = []
    else: # Jika user tambah produk, maka list produk sama dengan list data produk sebelumnya (rekursi)
        dataProduk = x
    dataTr = [] # List data transaksi akan selalu dikosongkan

    print(f"{Garis('=', 50)}")
    namaProduk = input('Masukkan nama produk        : ').capitalize()
    while True:
        try:
            hargaProduk = input('Masukkan harga produk       : ')
            if len(str(hargaProduk)) < 3 or hargaProduk[0] == '0': # Memastikan harga minimal ratusan, berupa integer, dan tidak dimulai dari nol
                raise Exception('\nHarga produk invalid!\n')
            hargaProduk = int(hargaProduk)
            break

        except ValueError:
            print('\nHarga produk invalid!\n')

        except Exception as ex:
            print(ex)

    while True:
        try:
            jumlahProduk = input('Masukkan jumlah produk      : ')
            if jumlahProduk[0] == '0':
                raise ValueError
            jumlahProduk = int(jumlahProduk)
            print(f"{Garis('=', 50)}")
            break

        except ValueError:
            print('\nJumlah produk invalid!\n')

    totalHarga = int(hargaProduk * jumlahProduk) # Total harga setiap produk
    TOTAL = t; TOTAL += totalHarga ; RpTOTAL = f'Rp{TOTAL}'# Total harga semua produk

    namaTanpaSpasi = namaKasir.replace(' ','') # Nama untuk ID
    tglDanWaktuIndo = datetime.now().strftime("%d/%m/%y %H:%M") # Tanggal dan waktu untuk tabel
    if len(namaTanpaSpasi) <= 3: # ID dari nama jika panjang nama kasir kurang atau sama dengan tiga karakter.
        IDnama = namaTanpaSpasi.upper()
    else:
        IDnama = (namaTanpaSpasi[0] + namaTanpaSpasi[len(namaTanpaSpasi) // 2] + namaTanpaSpasi[-1]).upper() # ID dari nama kasir jika panjang nama kasir lebih dari tiga karakter
    IDtglwaktu = datetime.now().strftime("%y%m%d%H%M") # ID dari tanggal dan waktu
    IDangka = str(random.randint(100, 999)) # ID dari tiga angka acak
    if len(n) == 1:
        ID = IDnama + IDtglwaktu + IDangka # ID jika user telah melakukan transaksi
    else:
        ID = n # ID jika user ingin tambah produk

    dataProduk.append([namaProduk, f'Rp{hargaProduk}', jumlahProduk, f'Rp{totalHarga}']) # Menampung data produk dari user
    dataTr.append([tglDanWaktuIndo, ID, f'Rp{TOTAL}']) # Menampung data riwayat transaksi user
    
    while True:
        try:
            tp = input('Tambah produk? (y / t)      : ').lower() # Menentukan apakah user ingin tambah produk
            if tp == 't':
                print(f"{Garis('=', 50) }\n" + 'TRANSAKSI BERHASIL'.center(50) + f"\n{Garis('=', 50) }")
                
                path = 'C:/Users/USER/OneDrive/Dokumen/Kuliah/CSE-AP/Lap-AP-A/Tugas Praktikum/TP-07'
                os.chdir(path)
                
                namaFolder = 'Invoices' # Membuat nama dir / folder
                filePath = f'{namaFolder}/{ID}.txt' # Membuat file path (tempat beserta nama file)
                
                if not os.path.exists(namaFolder): # Cek apakah dir / folder sudah ada
                    os.mkdir(namaFolder) # Membuat folder baru

                with open(filePath, 'a') as fh: # Open file
                    # Membuat tabel untuk invoices
                    fh.write('\n' + f"TOKO {namaKasir.upper()}".center(66) + '\n') 
                    fh.write(f"\n{Garis('=', 66)}\nNama kasir         : {namaKasir}\nWaktu transaksi    : {tglDanWaktuIndo}\n{Garis('=', 66)}")
                    fh.write('\n\n' + 'Daftar Produk'.center(66) + '\n\n')
                    fh.write(f"\t{Garis('=', 58)}\n")
                    fh.write(f"\t|        Nama        |    Harga   | Jumlah |    Total    |\n")
                    fh.write(f"\t{Garis('=', 58)}") # Format head table Daftar Produk
                    for i in range(len(dataProduk)):
                        nama = dataProduk[i][0][:15] + '...' if len(dataProduk[i][0]) > 15 else dataProduk[i][0][:15]
                        fh.write(f"\n\t| {nama:<18} |" + f" {dataProduk[i][1]:>10} |" + f" {dataProduk[i][2]:^6} " + f"| {dataProduk[i][3]:>11} |")
                    fh.write('\n' + f"{Garis('=', 58)}".center(66))
                    fh.write('\n' + f'    |       TOTAL                              | {RpTOTAL:>11} |' + '\n')
                    fh.write(f"{Garis('=', 58)}".center(66) + f"\n\n{Garis('=', 66)}\n" + 'TERIMA KASIH TELAH BERBELANJA'.center(66) + f"\n{Garis('=', 66)}")

                trxFile = 'trx_history2.txt' # Membuat file untuk riwayat transaksi
                if os.path.exists(trxFile) == False: # Cek apakah file sudah ada
                    # Membuat tabel riwayat transaksi jika file belum ada
                    with open(trxFile, 'a') as tr:
                        tr.write(f"{Garis('=', 80)}")
                        tr.write(f"\n|                              RIWAYAT TRANSAKSI                               |")
                        tr.write(f"\n{Garis('=', 80)}")
                        tr.write(f"\n| {'Waktu':^20} | {'ID':^20} | {'Nominal':^30} |")
                        tr.write(f"\n{Garis('=', 80)}\n") # Format tabel riwayat transaksi jika filenya belum ada
                        for i in range(len(dataTr)):
                            tr.write(f"| {dataTr[i][0]:^20} | {dataTr[i][1]:^20} | {dataTr[i][2]:>30} |")
                            tr.write(f"\n{Garis('=', 80)}")
                    break

                else: # Membuat tabel riwayat transaksi jika file belum ada
                    with open(trxFile, 'a') as tr:
                        for i in range(len(dataTr)):
                            tr.write(f"| {dataTr[i][0]:^20} | {dataTr[i][1]:^20} | {dataTr[i][2]:>30} |")
                            tr.write(f"\n{Garis('=', 80)}") # Format tabel riwayat transaksi jika file sudah ada
                    break
            elif tp == 'y':
                transaksiBaru(ID, dataProduk, TOTAL) # Jika user ingin menambahkan produk, maka terjadi rekursi dengan menggunakan ID dan list data produk sebelumnya
                break
            else: # Memastikan user hanya menginput opsi 'y' atau 't'
                raise Exception(f"{Garis('=', 50)}\nHanya ada opsi 'y' dan 't'!\n")
            
        except Exception as ex:
            print(ex)

def cekTrx():
    while True:
        try:
            path = 'C:/Users/USER/OneDrive/Dokumen/Kuliah/CSE-AP/Lap-AP-A/Tugas Praktikum/TP-07'
            os.chdir(path)
            
            id = input(f"{Garis('=', 50)}\nMasukkan ID transaksi       : ")
            filePath = f'invoices/{id}.txt'

            if os.path.exists(filePath): # Mencari file berdasarkan ID yang dimasukkan
                print(f"{'_' * 66}")
                with open(filePath, 'r') as fh:
                    print(fh.read())
                print(f"{'_' * 66}")
                break

            else: 
                raise Warning(f"{Garis('=', 50)}\nID invalid!\n")
            
        except Warning as wr:
            print(wr)


print(f"{Garis('=', 50)}\n" + "SELAMAT DATANG".center(50) + f"\n{Garis('=', 50)}")
while True:
    try:
        namaKasir = input("Masukkan nama kasir         : ").title()
        if (namaKasir.replace(' ','').replace('.','')).isalpha() == False: # Memastikan tidak ada karakter selain huruf, spasi, dan tanda titik
            raise Exception('\nNama harus huruf!\n')
        elif len(namaKasir) == 0: # Memastikan nama kasir tidak kosong
            raise Warning('\nNama tidak boleh kosong!\n')
        print(Garis('=', 50))
        break
    except Warning as war:
        print(war)
    except Exception as ex:
        print(ex)

while True:
    try:
        print('Pilih opsi:\n1. Transaksi baru\n2. Cari transaksi\n3. Keluar')
        print(Garis('=', 50))
        opsi = input('Masukkan opsi pilihan Anda  : ')
        if opsi == '1':
            transaksiBaru('1', '', 0)
        elif opsi == '2':
            cekTrx()
        elif opsi == '3':
            print(f"{Garis('=', 50)}\n" + 'SAMPAI JUMPA'.center(50) + f"\n{Garis('=', 50)}")
            break
        else:
            raise Warning(f"{'=' * 50}\nOpsi invalid!\n")
    except Warning as wr:
        print(wr)