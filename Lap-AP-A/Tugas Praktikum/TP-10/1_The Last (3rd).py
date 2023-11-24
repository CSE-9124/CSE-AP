import os
import re

class UserData:
    def __init__(self):
        self.data = {}

    # Opsi 1
    def show_detail(self):
        if not self.data:
            print("=" * 60)
            print("Data saat ini kosong")
        else:
            print("=" * 60)
            print("Data anda adalah")
            for key, value in self.data.items():
                print(f"{key}: {value}")
    
    # Opsi 2
    def change_name(self):
        if not self.data:
            print("=" * 60)
            print("Data saat ini kosong")
        else:
            new_name = input("Silahkan Masukkan nama baru: ")
            self.data['Nama'] = new_name
            print("Nama berhasil diubah.")

    # Opsi 4
    def save_to_file(self):
        if not self.data:
            print("=" * 60)
            print("Data saat ini kosong")
        else:
            print("=" * 60)
            file_name = input("Silahkan Masukkan nama file : ") + ".txt"

            if not os.path.exists(file_name):
                with open(file_name, 'w') as file:
                    file.write(f'{"=" * 60}\n')
                    file.write("DATA YANG TERSIMPAN\n")
                    file.write(f'{"=" * 60}\n')
                    for key, value in self.data.items():
                        file.write(f"{key}: {value}\n")
                    file.write(f'{"=" * 60}')
            else:
                with open(file_name, 'a') as file:
                    for key, value in self.data.items():
                        file.write(f"\n{key}: {value}")
                    file.write(f'\n{"=" * 60}')

            self.data = {}
            print("Berhasil menyimpan data.")

    # Opsi 5
    def create_new_data(self):
        print("=" * 60)
        nama = input("Silahkan Masukkan Nama: ")

        while True:
            email = input("Silahkan Masukkan Email: ")
            # Validasi Email
            if not re.match(r"^[a-z0-9]+@student\.unhas\.ac\.id$", email):
                print("=" * 60)
                print("Email yang Anda masukkan salah")
            else:
                break
            
        while True:
            password = input("Silahkan Masukkan Password: ")
            # Validasi Password
            if not 8 <= len(password) <= 20:
                print("=" * 60)
                print("Password Harus Memiliki Panjang 8-20")
                continue
            if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])[a-zA-Z0-9]+$", password):
                print("=" * 60)
                print("Password Yang Anda Masukkan Terlalu Lemah")
                print("Gunakan Minimal 1 Huruf Kapital, Huruf Kecil, dan Angka")
            else:
                break

        self.data = {'Nama': nama, 'Email': email, 'Password': password}
        print("Data baru berhasil dibuat.")


def main():
    user_data = UserData()

    while True:
        print("=" * 60)
        print("Selamat Datang Silahkan Pilih Opsi Menu Anda")
        print("1. Detail Anda")
        print("2. Ubah Nama")
        print("3. Jumlah Data pada File")
        print("4. Save Data pada File")
        print("5. Buat Data Baru")
        print("6. Keluar")

        opsi = input("Silahkan Pilih Opsi Anda : ")

        if opsi == '1':
            user_data.show_detail()

        elif opsi == '2':
            user_data.change_name()

        elif opsi == '3':
            print("=" * 60)
            file_name = input("Silahkan Masukkan nama file : ") + ".txt"
            try:
                with open(file_name, 'r') as file:
                    baris = len(file.readlines())
                    data_count = (baris - 3) // 4
                print("Berhasil")
                print(f"Jumlah data pada file : {data_count} data")
            except FileNotFoundError:
                print(f"Tidak Terdapat File dengan Nama {file_name}")
                print("Jumlah Data Pada File : 0 Data")

        elif opsi == '4':
            user_data.save_to_file()

        elif opsi == '5':
            user_data.create_new_data()

        elif opsi == '6':
            print("=" * 60)
            print("Sampai Jumpa Lagi")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih menu yang benar.")

main()