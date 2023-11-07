import os

def clear_terminal():
    os.system('cls')

clear_terminal()

# Study Case 1:
print('Study Case 1:\n')
class Departemen:
    def __init__(self, nama):
        self.nama = nama
        self.total_dosen = 25
        self.__fakultas = "MIPA"

    def get_nama(self):
        return self.nama
    def set_nama(self, nama):
        self.nama = nama

    def get_total_dosen(self):
        return self.total_dosen
    def set_total_dosen(self, total_dosen):
        self.total_dosen = total_dosen

    def get_fakultas(self):
        return self.__fakultas
    def set_fakultas(self, fakultas):
        self.__fakultas = fakultas

# objek
departemen = Departemen('Matematika')
print(departemen.get_nama())
print(departemen.get_total_dosen())
print(departemen.get_fakultas())

print()
departemen.set_total_dosen(100)
print(departemen.get_total_dosen())

# print(departemen.__fakultas)
print(f'''
Prodi {departemen.get_nama()} | Total Dosen: {departemen.get_total_dosen()} | Fakultas: {departemen.get_fakultas()}
''')


# Study Case 2:
print('Study Case 2:\n')
# class parent
class Enemy:
    def __init__(self, nama, darah, attack):
        self.Name = nama
        self.hp = int(darah)
        self.attackpoint = int(attack)
    
    def attack(self):
        print(f'{self.Name} menyerang dengan kekuatan {self.attackpoint}')

# class child
class Zombie(Enemy):    # child 1
    def __init__(self, nama, darah, attack):
        super().__init__(nama, darah, attack)

    def Walk(self):
        print(f'{self.Name} berjalan dengan lamban')

class Pocong(Enemy):    # child 2
    def __init__(self, nama, darah, attack):
        super().__init__(nama, darah, attack)

    def Jump(self):
        print(f'{self.Name} Lompat tinggi ke udara')

class Drakula(Enemy):   # child 3
    def __init__(self, nama, darah, attack):
        super().__init__(nama, darah, attack)
    
    def Fly(self):
        print(f'{self.Name} Terbang dengan wujud kelelawar')

# objek
zombi = Zombie('Zombie', 20000, 10000)
pocong = Pocong('Pocong', 10000, 5000)
drakula = Drakula('Drakula', 50000, 50000)

# memanggil metode
zombi.attack()
zombi.Walk()

pocong.attack()
pocong.Jump()

drakula.attack()
drakula.Fly()
