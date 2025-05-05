from enum import Enum
#felsorálás tipus: csak ilyen tipusu attributumok léteznek, amiket meghatároztunk
class Attribute(Enum):
    READ_ONLY = 10
    HIDDEN = 2
    SYSTEM = 3
    ARCHIVE = 4
    DEVICE = 5
    TEMPORARY = 6
    COMPRESSED = 7
    OFFLINE = 8
    NON_CONTEXT_INDEXED = 9
    ENCRYPTED = 10


class Fajl:
    def __init__(self, nev: str, kiterjesztes: str, tartalom: str, attribute: Attribute):
        self.nev = nev
        self.kiterjesztes = kiterjesztes
        self.tartalom = tartalom
        self.attribute = attribute
        self.meret = len(tartalom)

    def __str__(self):
        return f"{self.nev}.{self.kiterjesztes}: {self.tartalom} {self.attribute}"


class Hattertarolo:
    def __init__(self, meret):
        self.files = []
        self.meret = meret

    def hozzaad(self, file: Fajl):
        for item in self.files:
            if item.nev == file.nev:
                print("A fájl már létezik a háttértárolón.")
                return
        if self.FoglaltKapacitás() + file.meret > self.meret:
            print("A fájl nem fér el a háttértárolón.")
        else:
            self.files.append(file)

    def Torles(self, nev: str): 
        for item in self.files:
            if item.nev == nev:
                self.files.remove(item)
                print(f"{nev} fájl törölve.")
                return
        print("A fájl nem található.")

    def MaximálisKapacitás(self):
        return self.meret

    def FoglaltKapacitás(self):
        ossz = 0
        for item in self.files:
            ossz += item.meret
        return ossz

    def SzabadKapacitás(self):
        maxim = self.MaximálisKapacitás()
        foglalt = self.FoglaltKapacitás()
        return maxim - foglalt

    def Keres(self, nev):
        for item in self.files:
            if item.nev == nev:
                print("Fájl megtalálva.")
                return item
        print("A fájl nem található.")
        return None

    def Listáz(self):
        for item in self.files:
            if item.attribute not in {Attribute.HIDDEN, Attribute.SYSTEM, Attribute.ARCHIVE, Attribute.TEMPORARY}:
                print(item)

    def Listáz_logikai(self, csak_nepszeru: bool):
        if csak_nepszeru:
            for item in self.files:
                if item.attribute == Attribute.READ_ONLY:
                    print(item)
        else:
            self.Listáz()

    def __str__(self):
        s = ""
        for item in self.files:
            s += item.__str__() + "\n"
        return s


# Tesztelés
def main():
    t1 = "a tiramisu receptje: babapiskóta, kave, mascarpone, tejszin, cukor, kakaopor"
    t2 = "Toltottkáposzta: káposzta, hus, rizs, meg egy csomo szeretet"
    
    f1 = Fajl("sütik", "txt", t1, Attribute.READ_ONLY)
    f2 = Fajl("Nagyi_recept", "docx", t2, Attribute.HIDDEN)
    
    pen = Hattertarolo(200000000)#hivódik az init, létrejon a files lista
    pen.hozzaad(f1)
    pen.hozzaad(f2)
    print(pen)
    
    pen.Torles("sütik")
    pen.Listáz()
    pen.Listáz_logikai(False)
    pen.Listáz_logikai(True)

main()
