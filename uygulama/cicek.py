class Cicek:
    def __init__(self,isim,renk,stok):
        self.isim=isim   
        self._renk=renk   
        self.__stok=stok   
    
    def stok_ekle(self, miktar):
        if miktar > 0:
            self.__stok += miktar
            print(f"{miktar} adet stok eklendi. Güncel stok: {self.__stok}")
        else:
            print("Geçersiz miktar!")

    def stok_azalt(self, miktar):
        if 0 < miktar <= self.__stok:
            self.__stok -= miktar
            print(f"{miktar} adet stok çikarildi. Güncel stok: {self.__stok}")
        else:
            print("Yetersiz stok veya geçersiz miktar!")
    def bilgi_ver(self):
        print(f"Çiçek Adı: {self.isim}, Renk: {self._renk}, Stok: {self.__stok}")
    
    
    def get_stock(self):
        return self.__stok

    def set_stock(self, yeni_stok):
        if yeni_stok >= 0:
            self.__stok = yeni_stok
        else:
            print("Stok miktarı negatif olamaz!")