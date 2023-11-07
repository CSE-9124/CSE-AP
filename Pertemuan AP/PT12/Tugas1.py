class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def delete(self, file):
        if file == self.nama or self.nim:
            print("Ter-Delete")  
        elif file != self.nama or self.nim :
            print("Tidak ada file")

mhs = Mahasiswa("Faizz", "H071231066")
mhs.delete("H071231266")