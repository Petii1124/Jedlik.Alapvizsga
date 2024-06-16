from datetime import datetime

class tanulo:
    def __init__(self, veteteknev:str,keresztnev:str,szuletes:datetime, jegyek:list[int]) -> None:
        self.vezeteknev=veteteknev
        self.keresztnev=keresztnev
        self.szuletes=szuletes
        self.jegyek=jegyek

    def atlag(self)->float:
        if len(self.jegyek)==0: #ha nicsen jegye el kell kerulni a 0 osztot
            return 0
        osszeg=0
        for j in self.jegyek:
            osszeg+=j
        return osszeg/len(self.jegyek)