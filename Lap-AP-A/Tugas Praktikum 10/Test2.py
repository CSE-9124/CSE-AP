from abc import ABC, abstractmethod

class MinumanHangatDingin(ABC):
    @abstractmethod
    def suara(self):
        pass

class KopiHangat(MinumanHangatDingin):
    def __init__(self, nama, temperatur):
        self._nama = nama
        self._temperatur = temperatur

    def suara(self):
        return f"Siap minum kopi hangat yang ditawarkan {self.get_nama()} dengan temperatur {self.get_temperatur()} derajat Celsius"


    def get_nama(self):
        return self._nama
    def get_temperatur(self):
        return self._temperatur
    
    def set_nama(self, new_nama):
        self._nama = new_nama
    def set_temperatur(self, new_temperatur):
        self._temperatur = new_temperatur


class KopiDingin(MinumanHangatDingin):
    def _init_(self, nama, temperatur):
        super().__init__(nama, temperatur)

    def suara(self):
        return f"Siap minum kopi dingin yang ditawarkan {self.get_nama()} dengan temperatur {self.get_temperatur()} derajat Celsius"


def mengeluarkan_suara(kopi):
    return kopi.suara()


kopi_hangat = KopiHangat("Kopi Mocha", 80)
kopi_dingin = KopiDingin("Kopi Espresso", 30)

print(mengeluarkan_suara(kopi_hangat))
print(mengeluarkan_suara(kopi_dingin))