class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def __str__(self):
        return f"Nama: {self.nama}, NIM: {self.nim}"

class DaftarMahasiswa:
    def __init__(self):
        self.mahasiswa_list = []

    def tambah_mahasiswa(self, nama, nim):
        mahasiswa = Mahasiswa(nama, nim)
        self.mahasiswa_list.append(mahasiswa)
        print(f"Mahasiswa {nama} dengan NIM {nim} berhasil ditambahkan.")

    def edit_mahasiswa(self, nama_baru, nim):
        mahasiswa = self._cari_mahasiswa(nim)
        if mahasiswa:
            mahasiswa.nama = nama_baru
            print(f"Data mahasiswa dengan NIM {nim} berhasil diubah menjadi {nama_baru}.")
        else:
            print(f"Mahasiswa dengan NIM {nim} tidak ditemukan.")

    def hapus_mahasiswa(self, nim):
        mahasiswa = self._cari_mahasiswa(nim)
        if mahasiswa:
            self.mahasiswa_list.remove(mahasiswa)
            print(f"Data mahasiswa dengan NIM {nim} berhasil dihapus.")
        else:
            print(f"Mahasiswa dengan NIM {nim} tidak ditemukan.")

    def tampilkan_daftar_mahasiswa(self):
        print("\nDaftar Mahasiswa:")
        for mahasiswa in self.mahasiswa_list:
            print(mahasiswa)

    def _cari_mahasiswa(self, nim):
        for mahasiswa in self.mahasiswa_list:
            if mahasiswa.nim == nim:
                return mahasiswa
        return None

# penggunaan program
daftar_mahasiswa = DaftarMahasiswa()

# tambah mahasiswa
daftar_mahasiswa.tambah_mahasiswa("Salsabila Dwi Putri", "H071231011")
daftar_mahasiswa.tambah_mahasiswa("Muh. Akbar Dhani", "D131231067")

# tampilkan daftar mahasiswa
daftar_mahasiswa.tampilkan_daftar_mahasiswa()

print('-' * 50)

# edit mahasiswa
daftar_mahasiswa.edit_mahasiswa("An Naura", "H071231047")
daftar_mahasiswa.tampilkan_daftar_mahasiswa()

print('-' * 50)

# hapus mahasiswa
daftar_mahasiswa.hapus_mahasiswa("H071231011")
daftar_mahasiswa.tampilkan_daftar_mahasiswa()
