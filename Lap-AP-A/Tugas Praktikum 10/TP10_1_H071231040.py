import os
import re


''' Function '''
def clear():
    os.system('cls')
def Garis(n):
    return f'{"=" * n}'
def Judul_Tabel(kata):
    return f"|{kata.center(60)}|"
def Isi_Tabel(kata):
    return f"|{kata.ljust(60)}|"


''' Class '''
class Data_User:
    def __init__ (self, nama, email, password):
        self.Nama = nama
        self.Email = email
        self.__Password = password

    def get_Password(self):
        return self.__Password
    def set_Password(self, Pass_Baru):
        self.__Password = Pass_Baru


''' Terminal '''
clear()
while True:
    print(f'''+{Garis(60):^60}+
{Judul_Tabel("Selamat Datang Silahkan Pilih Opsi Menu Anda")}
|{("-" * 60):^60}|
{Isi_Tabel("1. Detail Anda")}
{Isi_Tabel("2. Ubah Nama")}
{Isi_Tabel("3. Jumlah Data Pada Files")}
{Isi_Tabel("4. Save Data Pada Files")}
{Isi_Tabel("5. Buat Data Baru")}
{Isi_Tabel("6. keluar")}
+{Garis(60):^60}+''')

    Opsi = int(input(' Masukan Opsi: '))
    print(f'+{Garis(60):^60}+')

    match Opsi:

        # Detail Anda
        case 1:
            try:
                if User.Nama:
                    pass
                elif User.Nama == None:
                    raise NameError
                clear()

                print(f'+{Garis(60):^60}+\n{Judul_Tabel("Detail Anda")}\n+{Garis(60):^60}+')
                print(f'{Isi_Tabel(f"Nama     : {User.Nama}")}')
                print(f'{Isi_Tabel(f"Email    : {User.Email}")}')
                print(f'{Isi_Tabel(f"Password : {User.get_Password()}")}')

            except:
                print(f'{"-" * 62}\n{"Data Saat Ini Kosong":^62}\n{"-" * 62}')


        # Ubah Nama
        case 2:
            try:
                if User.Nama:
                    pass
                elif User.Nama == None:
                    raise NameError
                clear()

                print(f'+{Garis(60):^60}+\n{Judul_Tabel("Ubah Nama")}\n+{Garis(60):^60}+')

                while True:
                    Nama_Baru = input(' Silahkan Input Nama Baru : ')

                    if Nama.replace(' ', '').replace('.','').isalpha() and len(Nama.replace(' ', '').replace('.', '')) > 0:
                        break
                    else: print(f'{"-" * 62}\n{"Nama Invalid. Coba lagi!!":^62}\n{"-" * 62}')
                
                User.Nama = Nama_Baru

                print(f'+{Garis(60):^60}+\n|{f"Berhasil":^60}|\n|{f"Nama Sudah Diubah":^60}|\n+{Garis(60):^60}+')

            except:
                print(f'{"-" * 62}\n{"Data Saat Ini Kosong":^62}\n{"-" * 62}')


        # Jumlah Data Pada Files
        case 3:
            clear() 
            print(f'+{Garis(60):^60}+\n{Judul_Tabel("Jumlah Data Pada File")}\n+{Garis(60):^60}+')
            
            path = 'C:/Users/USER/OneDrive/Dokumen/Kuliah/CSE-AP/Lap-AP-A/Tugas Praktikum 10'
            os.chdir(path)

            Files = input(' Silahkan Masukkan Nama File : ') + '.txt'

            if not os.path.exists(Files):
                print(f'{"-" * 62}\n{f"Tidak Terdapat File dengan Nama {Files}":^62}\n{"Jumlah Data Pada File : 0 Data":^62}\n{"-" * 62}')

            else:
                with open(Files, 'r') as R:
                    baris = len(R.readlines())
                    Banyak_Data = (baris - 3) // 4
                    
                    print(f'+{Garis(60):^60}+\n|{f"Berhasil":^60}|\n|{f"Jumlah Data Pada File : {Banyak_Data} Data":^60}|\n+{Garis(60):^60}+')


        # Save Data Pada Files
        case 4:
            path = 'C:/Users/USER/OneDrive/Dokumen/Kuliah/CSE-AP/Lap-AP-A/Tugas Praktikum 10'
            os.chdir(path)
            try:
                if User.Nama:
                    pass
                clear()

                print(f'+{Garis(60):^60}+\n{Judul_Tabel("Save Data Pada File")}\n+{Garis(60):^60}+')

                Files = input(' Silahkan Masukkan Nama File : ') + '.txt'

                if not os.path.exists(Files):
                    with open(Files, 'w') as F:
                        F.write(f'+{Garis(60):^60}+\n')
                        F.write(f'{Judul_Tabel("DATA YANG TERSIMPAN")}\n')
                        F.write(f'+{Garis(60):^60}+\n')
                        F.write(f'{Isi_Tabel(f"Nama         : {User.Nama}")}\n')
                        F.write(f'{Isi_Tabel(f"Email        : {User.Email}")}\n')
                        F.write(f'{Isi_Tabel(f"Password     : {User.get_Password()}")}\n')
                        F.write(f'+{Garis(60):^60}+')

                        User = Data_User(nama=None, email=None, password=None)
                else:
                    with open(Files, 'a') as F:
                        F.write(f'\n{Isi_Tabel(f"Nama         : {User.Nama}")}\n')
                        F.write(f'{Isi_Tabel(f"Email        : {User.Email}")}\n')
                        F.write(f'{Isi_Tabel(f"Password     : {User.get_Password()}")}\n')
                        F.write(f'+{Garis(60):^60}+')

                        User = Data_User(nama=None, email=None, password=None)
                
                print(f'+{Garis(60):^60}+\n{Judul_Tabel("Berhasil")}\n+{Garis(60):^60}+')
                
            except:
                print(f'{"-" * 62}\n{"Data Saat Ini Kosong":^62}\n{"-" * 62}')


        # Buat Data Baru
        case 5:
            clear()
            print(f'+{Garis(60):^60}+\n{Judul_Tabel("Buat Data Baru")}\n+{Garis(60):^60}+')

            while True: # Error Handling utk Nama
                Nama = str(input(' Silahkan Masukkan Nama Anda \t : '))

                if Nama.replace(' ', '').replace('.','').isalpha() and len(Nama.replace(' ', '').replace('.', '')) > 0:
                    break
                else: print(f'{"-" * 62}\n{"Nama Invalid. Coba lagi!!":^62}\n{"-" * 62}')
            
            while True: # Error Handling utk Email
                Email = str(input(' Silahkan Masukkan Email Anda \t : '))
                Validasi_Email = re.match(r'^[a-z0-9]{2,}@student\.unhas\.ac\.id$', Email)

                if Validasi_Email:
                    break
                else: print(f'{"-" * 62}\n{"Email Yang Anda Masukkan Salah. Coba lagi!!":^62}\n{"-" * 62}')

            while True: # Error Handling utk Password
                Password = str(input(' Silahkan Masukkan Password Anda : '))
                Panjang_Password = re.match(r'.{8,20}', Password)
                Validasi_Password = re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])[a-zA-Z0-9]+$', Password)

                if Panjang_Password:
                    if Validasi_Password:
                        break
                    else: print(f'{"-" * 62}\n{"Password Yang Anda Masukkan Terlalu Lemah":^62}\n{" Gunakan Minimal 1 Huruf Kapital, Huruf Kecil, dan Angka":^62}\n{"-" * 62}')
                else: print(f'{"-" * 62}\n{"Password Harus Memiliki Panjang 8-20":^62}\n{"-" * 62}')

            User = Data_User(Nama, Email, Password)
            print(f'+{Garis(60):^60}+\n{Judul_Tabel("Data Sudah Dibuat, Tinggal Di Save")}\n+{Garis(60):^60}+')


        # Keluar
        case 6:
            clear()
            print(f'+{Garis(60):^60}+\n{Judul_Tabel("Sampai Jumpa Lagi")}\n+{Garis(60):^60}+')
            break


        case _:
            print(f'{"-" * 62}\n{"Opsi Invalid. Coba Lagi!!":^62}\n{"-" * 62}')