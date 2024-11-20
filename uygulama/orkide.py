from uygulama.cicek import Cicek
from uygulama.egzotik_bitki import EgzotikBitki

class Orkide(Cicek, EgzotikBitki):
    def __init__(self, renk, stok, bolge, bakim_zorlugu):
        Cicek.__init__(self, "Orkide", renk, stok)
        EgzotikBitki.__init__(self, bolge, bakim_zorlugu)

    def bilgi_ver(self):
        super().bilgi_ver()
        print(f"Bölge: {self.bolge}, Bakım Zorluğu: {self.bakim_zorlugu}")