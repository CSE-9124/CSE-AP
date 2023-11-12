import os
os.system('cls')

class Mahasiswa:
    def __init__(self):
        self.daftar_mahasiswa = {}

    def Tambah(self, nama, nim):
        if nim not in self.daftar_mahasiswa:
            self.daftar_mahasiswa[nim] = {'Nama': nama, 'NIM': nim}
        else:
            print(f'Mahasiswa dengan NIM {nim} sudah ada dalam daftar.')
        
    def Edit(self, nim, nama_baru, nim_baru):
        if nim in self.daftar_mahasiswa:
            self.daftar_mahasiswa[nim] = {'Nama': nama_baru, 'NIM': nim_baru}
        else:
            print(f"Mahasiswa dengan NIM {nim} tidak ditemukan.")

    def Delete(self, nim):
        if nim in self.daftar_mahasiswa:
            del self.daftar_mahasiswa[nim]
            print(f'Mahasiswa dengan NIM {nim} berhasil dihapus.')
        else:
            print(f"Mahasiswa dengan NIM {nim} tidak ditemukan.")

    def Tampilkan_daftar(self):
        print("Daftar Mahasiswa :")
        i = 1
        while i <= len(self.daftar_mahasiswa):
            for _, nim in self.daftar_mahasiswa.items():
                print(f'{i}. {nim["Nama"]} ({nim["NIM"]})\n')
                i += 1


daftar_mahasiswa = Mahasiswa()

print(f'{"=" * 50}\n' + f'{"MEMBUAT DAFTAR NAMA dan NIM MAHASISWA":^50}\n' + f'{"=" * 50}')
while True:
    Nama = input('Masukkan Nama Mahasiswa : ').title()
    if len(Nama) > 0: 
        break
    else:
        print('Invalid Nama, Try Again!!')
while True:
    NIM = input('Masukkan NIM Mahasiswa  : ').upper()
    if len(NIM) > 0:
        break
    else:
        print('Invalid NIM, Try Again!!')
daftar_mahasiswa.Tambah(Nama, NIM)

while True:
    print(f'{"=" * 50}\nPilih Opsi :\n1. Tambah data Mahasiswa\n2. Edit data Mahasiswa\n3. Delete data Mahasiswa\n4. Tampilkan daftar data Mahasiswa\n5. Keluar\n{"=" * 50}' )
    opsi = int(input('Opsi : '))
    match opsi:
        case 1:
            os.system('cls')
            print(f'{"=" * 50}\n' + f'{"Tambah Data Mahasiswa":^50}\n' + f'{"=" * 50}')
            while True:
                Nama = input('Masukkan Nama Mahasiswa : ')
                if len(Nama) > 0: 
                    break
                else:
                    print('Invalid Nama, Try Again!!')
            while True:
                NIM = input('Masukkan NIM Mahasiswa  : ').upper()
                if len(NIM) > 0:
                    break
                else:
                    print('Invalid NIM, Try Again!!')
            daftar_mahasiswa.Tambah(Nama, NIM)
            print('Data Mahasiswa berhasil ditambahkan.')

        case 2:
            os.system('cls')
            print(f'{"=" * 50}\n' + f'{"Delete Data Mahasiswa":^50}\n' + f'{"=" * 50}')
            NIM = input('Masukkan NIM Mahasiswa : ').upper()
            while True:
                Nama_Baru = input('Masukkan Nama Baru Mahasiswa : ')
                if len(Nama_Baru) > 0: 
                    break
                else:
                    print('Invalid Nama, Try Again!!')
            while True:
                NIM_Baru = input('Masukkan NIM Baru Mahasiswa  : ').upper()
                if len(NIM_Baru) > 0:
                    break
                else:
                    print('Invalid NIM, Try Again!!')
            daftar_mahasiswa.Edit(NIM, Nama_Baru, NIM_Baru)
            print('Data Mahasiswa berhasil diubah.')
        
        case 3:
            os.system('cls')
            print(f'{"=" * 50}\n' + f'{"Delete Data Mahasiswa":^50}\n' + f'{"=" * 50}')
            NIM = input('Masukkan NIM Mahasiswa : ').upper()
            daftar_mahasiswa.Delete(NIM)

        case 4:
            os.system('cls')
            print(f'{"=" * 50}\n' + f'{"DAFTAR":^50}\n' + f'{"=" * 50}')
            daftar_mahasiswa.Tampilkan_daftar()

        case 5:
            os.system('cls')
            print(f'{"=" * 50}\n' + f'{"SELAMAT TINGGAL":^50}\n' + f'{"=" * 50}')
            break
        
        case _:
            print('Invalid Opsi, Try Again!!')