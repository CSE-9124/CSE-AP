import re
import os

class Data:
    def __init__(self, nama, email, password):
        self.nama = nama
        self.email = email
        self.password = password


def menu():
    print("=" * 60)
    print("Selamat Datang Silahkan Pilih Opsi Menu Anda")
    print("1. Detail Anda")
    print("2. Ubah Nama")
    print("3. Jumlah Data Pada File")
    print("4. Save Data Pada File")
    print("5. Buat Data Baru")
    print("6. Keluar")


# Opsi 1
def detail_anda(data_list):
    if len(data_list) == 0:
        print("Data saat ini kosong")
    else:
        print(f"Nama:", data_list[0].nama)
        print(f"Email:", data_list[0].email)
        print(f"Password:", data_list[0].password)

# Opsi 2
def ubah_nama(data_list):
    if len(data_list) == 0:
        print("Data saat ini kosong")
    else:
        new_name = input("Masukkan nama baru (jika ada): ")
        if new_name:
            data_list[0].nama = new_name
            print("Nama berhasil diubah")

# Opsi 3
def jumlah_data_pada_file(filename):
    try:
        with open(f"{filename}.txt", "r") as file:
            lines = len(file.readlines())
            Banyak_Data = (lines - 3) // 4
            print("Berhasil")
            print(f"Jumlah data pada file : {Banyak_Data} data")
    except FileNotFoundError:
        print(f"Tidak Terdapat File dengan Nama {filename}.txt")
        print("Jumlah data pada file : 0 data")

# Opsi 4
def save_data(data_list):
    if len(data_list) == 0:
        print("Data Saat Ini Kosong")
    else:
        Files = input(' Silahkan Masukkan Nama File : ') + '.txt'

        if not os.path.exists(Files):
            with open(Files, 'w') as F:
                for data in data_list:
                    F.write(f'{"=" * 60}\n')
                    F.write(f'{"DATA YANG TERSIMPAN"}\n')
                    F.write(f'{"=" * 60}\n')
                    F.write(f'{f"Nama         : {data.nama}"}\n')
                    F.write(f'{f"Email        : {data.email}"}\n')
                    F.write(f'{f"Password     : {data.password}"}\n')
                    F.write(f'{"=" * 60}')
        
        else:
            with open(Files, 'a') as F:
                for data in data_list:
                    F.write(f'{f"Nama         : {data.nama}"}\n')
                    F.write(f'{f"Email        : {data.email}"}\n')
                    F.write(f'{f"Password     : {data.password}"}\n')
                    F.write(f'{"=" * 60}')
        data_list = []
        return 

# Opsi 5
def buat_data_baru():
    nama = input("Silahkan Masukkan Nama : ")
    email = input("Silahkan Masukkan Email : ")
    if not re.match(r"^[a-z0-9]+@student\.unhas\.ac\.id$", email):
        print("Email yang Anda Masukkan Salah")
        return None
    
    password = input("Silahkan Masukkan Password : ")
    if not (8 <= len(password) <= 20):
        print("Password harus memiliki Panjang 8 - 20 karakter")
        return None
    if not re.search(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])[a-zA-Z0-9]+$", password):
        print("Password yang anda masukkan terlalu lemah, gunakan minimal 1 huruf kapital, huruf kecil, dan angka")
        return None
    
    return Data(nama, email, password)


def main():
    data_list = []
    while True:
        menu()
        pilihan = input("Silahkan Pilih Opsi Anda : ")

        if pilihan == "1":
            detail_anda(data_list)

        elif pilihan == "2":
            ubah_nama(data_list)

        elif pilihan == "3":
            filename = input()
            jumlah_data_pada_file(filename)

        elif pilihan == "4":
            data_list = save_data(data_list)
            print("Berhasil")

        elif pilihan == "5":
            new_data = buat_data_baru()
            if new_data:
                data_list.append(new_data)
                print("Berhasil Membuat Data Baru")

        elif pilihan == "6":
            print("Sampai Jumpa Lagi")
            break

        else:
            print("Pilihan tidak valid")


main()