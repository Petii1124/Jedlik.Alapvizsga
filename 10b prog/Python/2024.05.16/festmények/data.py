class festmeny:
    def __init__(self,sor:str) -> None:
        adatok=sor.split(';')
        self.festmeny=adatok[0]
        self.festo=adatok[1]
        self.keszites_ev=int(adatok[2])
        self.becsult_ertek=int(adatok[3])
        self.eredeti_ar=int(adatok[4])
        self.eladas_eve=int(adatok[5])