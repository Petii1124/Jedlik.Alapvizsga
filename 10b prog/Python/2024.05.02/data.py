class versenyzo:
    def __init__(self,sor:str) -> None:
        adatok=sor.split(';')
        self.nev=adatok[0]
        self.szul_ev=int(adatok[1])
        self.rajtszam=int(adatok[2])
        self.neme=adatok[3]
        self.kategoria=adatok[4]
        self.ido_uszas=adatok[5]
        self.ido_elsod=adatok[6]
        self.ido_kerekp=adatok[7]
        self.ido_masodikd=adatok[8]
        self.ido_futas=adatok[9]

        self.osszido=""