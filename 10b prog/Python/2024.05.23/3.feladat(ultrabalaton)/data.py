class Versenyzo:
    def __init__(self,sor:str) -> None:
        adatok=sor.split(';')
        self.neve=adatok[0]
        self.rajtszam=str(adatok[1])
        self.kategoria=adatok[2]
        self.ido=adatok[3]
        self.teljesitett_tav=int(adatok[4])