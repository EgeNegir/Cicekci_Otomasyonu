class EgzotikBitki:
    def __init__(self, bolge, bakim_zorlugu):
        self.bolge = bolge
        self.bakim_zorlugu = bakim_zorlugu

    def egzotik_bilgi_ver(self):
        print(f"Bölge: {self.bolge}, Bakım Zorluğu: {self.bakim_zorlugu}")