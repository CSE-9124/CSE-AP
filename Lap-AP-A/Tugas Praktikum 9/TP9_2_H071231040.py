# Soal 2 : Membuat sebuah Class Mahasiswa
import os
os.system('cls')

class Mahasiswa:
    def __init__(self, nama, NIM, Jurusan, IPK):
        self.Nama = nama
        self.NIM = NIM
        self.Jurusan = Jurusan
        self.IPK = float(IPK)

    def Tampilkan_info(self):
        print(f'Nama \t : {self.Nama}')
        print(f'NIM \t : {self.NIM}')
        print(f'Jurusan  : {self.Jurusan}')
        print(f'IPK \t : {self.IPK}')

    def Hitung_predikat(self):
        if self.IPK >= 3.5:
            return 'Cumlaude'
        elif self.IPK >= 3.0:
            return 'Sangat Memuaskan'
        elif self.IPK >= 2.5:
            return 'Memuaskan'
        elif self.IPK >= 2.0:
            return 'Cukup'
        else:
            return 'Kurang'
        
# Objek
Mahasiswa_1 = Mahasiswa('William', 'C011231239', 'Kedokteran Umum', 3.3)
Mahasiswa_2 = Mahasiswa('Valeri', 'C031231006', 'Kedokteran Hewan', 3.8)

# Memanggil Method
Mahasiswa_1.Tampilkan_info()
print(f'Predikat : {Mahasiswa_1.Hitung_predikat()}')
print('-' * 50)
Mahasiswa_2.Tampilkan_info()
print(f'Predikat : {Mahasiswa_2.Hitung_predikat()}')