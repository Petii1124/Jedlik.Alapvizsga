idok=['01:17:565', '01:16:258', '01:15:711', '01:16:437', '01:16:764', '01:16:964', '01:15:185', '01:15:573', '01:15:078', '01:15:723', '01:17:284', '01:15:929', '01:15:382', '01:17:378', '01:17:961', '01:15:348', '01:17:303', '01:16:233', '01:17:665', '01:15:050' ]

def versenyzok():
    print(f'{len(idok)} versenyző indult a futamon.')

def leggyorsabb()->str:
    leggyorsabb_ember=0
    for i in idok:
        if i>leggyorsabb_ember:
            leggyorsabb_ember==i


    return i


def idoMasodpercben(ido: str) -> float:
    """
    A paraméterben stringként megadott időt átváltja másodpercre.
    """
    idok = ido.split(':')
    return int(idok[0]) * 60 + int(idok[1]) + int(idok[2]) / 1000