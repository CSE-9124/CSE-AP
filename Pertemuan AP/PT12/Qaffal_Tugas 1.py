class Mahasiswa:
    def __init__(self):
       self.dataMahasiswa = {}
    
    def add(self, nama, nim, jurusan, angkatan):
        self.dataMahasiswa[nim] = {'Nama': nama, 'NIM': nim, 'Jurusan': jurusan, 'Angkatan': angkatan}
        print('Data mahasiswa berhasil ditambahkan.\n')
        
    def edit(self, nim):
        if nim in self.dataMahasiswa:
            while True:
                x = input('Ingin mengubah apa?\n1. Nama\n2. NIM\n3. Jurusan\n4. Angkatan\n')
                if x == '1':
                    while True:
                        newName = input('Masukkan nama mahasiswa: ').title()
                        if newName.replace(' ', '').replace('.', '').isalpha() and len(newName.replace(' ', '').replace('.', '')) > 0:
                            self.dataMahasiswa[nim]['Nama'] = newName; print('Data nama mahasiswa berhasil diubah.\n'); break
                        else: print('Nama invalid. Coba lagi!')
                    break
                elif x == '2':
                    while True:
                        newNim = input('\nMasukkan NIM mahasiswa: ').upper()
                        if len(newNim) > 0:
                            self.dataMahasiswa[nim]['NIM'] = newNim; print('Data NIM mahasiswa berhasil diubah.\n'); break
                        else: print('NIM invalid. Coba lagi!')
                    break
                elif x == '3':
                    while True:
                        newJurusan = input('Masukkan jurusan mahasiswa: ').title()
                        if newJurusan.replace(' ', '').replace('.', '').isalpha() and len(newJurusan.replace(' ', '').replace('.', '')) > 0:
                            self.dataMahasiswa[nim]['Jurusan'] = newJurusan; print('Data jurusan mahasiswa berhasil diubah.\n'); break
                        else: print('Jurusan invalid. Coba lagi!')
                    break
                elif x == '4':
                    while True:
                        newAngkatan = input('Masukkan angkatan mahasiswa: ')
                        if newAngkatan.isdigit() and len(newAngkatan) == 4:
                            self.dataMahasiswa[nim]['Angkatan'] = newAngkatan; print('Data angkatan mahasiswa berhasil diubah.\n'); break
                        else: print('Angkatan invalid. Coba lagi!')
                    break
                else:
                    print('Opsi invalid. Coba lagi!')
        else:
            print(f'Data mahasiswa dengan NIM {nim} tidak ditemukan.\n')
    
    def delete(self, nim):
        if nim in self.dataMahasiswa:
            del self.dataMahasiswa[nim]
            print(f'Data mahasiswa dengan NIM {nim} berhasil dihapus.\n')
        else:
            print(f'Data mahasiswa dengan NIM {nim} tidak ditemukan.\n')
    
    def tampilkanData(self):
        if len(self.dataMahasiswa) == 0:
            print('Daftar data mahasiswa kosong.')
        else:
            print('\nBerikut daftar data mahasiswa:\n'); j = 1
            while j <= len(self.dataMahasiswa):
                for _, val in self.dataMahasiswa.items():
                    print(f"{j}. Nama    : {val['Nama']}\n   NIM     : {val['NIM']}\n   Jurusan : {val['Jurusan']}\n   Angkatan: {val['Angkatan']}\n")
                    j += 1

mahasessa = Mahasiswa()
while True:
    print(f"{'=' * 50}\n" + "SELAMAT DATANG".center(50) + f"\n{'=' * 50}")
    opsi = input('Pilih opsi:\n1. Tambah data mahasiswa\n2. Ubah data mahasiswa\n3. Hapus data mahasiswa\n4. Tampilkan daftar data mahasiswa\n5. Keluar\nOpsi : ')
    if opsi == '1':
        print()
        while True:
            nama = input('Masukkan nama mahasiswa: ').title()
            if nama.replace(' ', '').replace('.', '').isalpha() and len(nama.replace(' ', '').replace('.', '')) > 0: break
            else: print('Nama invalid. Coba lagi!')
        while True:
            nim = input('Masukkan NIM mahasiswa: ').upper()
            if len(nim) > 0: break
            else: print('NIM invalid. Coba lagi!')
        while True:
            jurusan = input('Masukkan jurusan mahasiswa: ').title()
            if jurusan.replace(' ', '').replace('.', '').isalpha() and len(jurusan.replace(' ', '').replace('.', '')) > 0: break
            else: print('Jurusan invalid. Coba lagi!')
        while True:
            angkatan = input('Masukkan angkatan mahasiswa: ')
            if angkatan.isdigit() and len(angkatan) == 4: break
            else: print('Angkatan invalid. Coba lagi!')
        mahasessa.add(nama, nim, jurusan, angkatan)
    elif opsi == '2':
        mahasessa.edit(input('\nMasukkan NIM mahasiswa: ').upper())
    elif opsi == '3':
        mahasessa.delete(input('\nMasukkan NIM mahasiswa: ').upper())
    elif opsi == '4':
        mahasessa.tampilkanData()
    elif opsi == '5':
        print(f"{'=' * 50}\n" + "TERIMA KASIH".center(50) + f"\n{'=' * 50}"); break
    else:
        print('\nOpsi invalid. Coba lagi!\n')