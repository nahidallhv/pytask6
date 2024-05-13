class hesab:
    def __init__(self, hesabNomresi, balans):
        self.hesabNomresi = hesabNomresi
        self.balans = balans
    def balansArtirma(self, miqdar):
        self.balans += miqdar
        print(f"{miqdar} AZN balansiniza elave olundu. Yeni balans: {self.balans} AZN")
    def pulCixar(self, miqdar):
        if self.balans >= miqdar:
            self.balans -= miqdar
            print(f"{miqdar} AZN balansinizdan cixarildi. Yeni balans: {self.balans} AZN")
        else:
            print("Balansinizda kifayet qeder vesait yoxdur.")
    def balansiGoster(self):
        print(f"hesab nomresi: {self.hesabNomresi}, Balans: {self.balans} AZN")
class kredit(hesab):
    def __init__(self, hesabNomresi, balans, kreditMiqdar):
        super().__init__(hesabNomresi, balans)
        self.kreditMiqdar = kreditMiqdar
    def kreditVer(self):
        self.balansArtirma(self.kreditMiqdar)
        print(f"{self.kreditMiqdar} AZN kreditiniz hesabiniza elave olundu.")
    def kreditOdenis(self):
        ayliqOdenis = self.kreditMiqdar / 12
        self.pulCixar(ayliqOdenis)
        print(f"kredit odenisi olan {ayliqOdenis} AZN balansinizdan cixarildi.")
        
### Test hesabB ###
hesab1 = hesab(12042005, 1000)
hesab1.balansiGoster()
hesab1.balansArtirma(400)
hesab1.pulCixar(200)
hesab1.balansiGoster()

### test kredit ###
kredit1 = kredit(12042005, 2000, 12000)
kredit1.kreditVer()
kredit1.kreditOdenis()
kredit1.balansiGoster()
