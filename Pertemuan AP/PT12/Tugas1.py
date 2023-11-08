class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
        self.daftar_mahasiswa = {}

    def Tambah(self, nama, nim):
        if nim not in self.daftar_mahasiswa:
            self.daftar_mahasiswa[nim] = nama
        else:
            print(f'Mahasiswa dengan NIM {nim} sudah ada dalam daftar')
        
    def Edit(self, nama_baru, nim):
        if nim in self.daftar_mahasiswa:
            self.daftar_mahasiswa[nim] = nama_baru
        else:
            print(f"Mahasiswa dengan NIM {nim} tidak ditemukan.")

    def Delete(self, nim):
        if nim in self.daftar_mahasiswa:
            del self.daftar_mahasiswa[nim]
        else:
            print(f"Mahasiswa dengan NIM {nim} tidak ditemukan.")

    def Tampilkan_daftar(self):
        print("Daftar Mahasiswa:")
        for nim, mahasiswa in self.daftar_mahasiswa.items():
            print(f"NIM: {nim}, Nama: {mahasiswa.nama}")


daftar_mahasiswa = Mahasiswa()

daftar_mahasiswa.Tambah('Cholyn Sharon Enos', 'H071231040')
daftar_mahasiswa.Tambah('Andi Riswanda', "H071231008")
daftar_mahasiswa.Tambah('Ivan Betrandi', "H071231038")
daftar_mahasiswa.Tampilkan_daftar()

daftar_mahasiswa.Edit("Cholyn Sharon", 'H071231040')
daftar_mahasiswa.Delete("H081231098")
daftar_mahasiswa.Tampilkan_daftar()