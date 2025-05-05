
#ősosztály: minden közös tulajdonság és metódus itt szerepel
class Forroital:
    def __init__(self,nev, ar,cukor):

        self.nev = nev
        self.ar = ar
        self.cukor = cukor

    def aremeles(self):
        self.ar+=50
    
    def __str__(self):
        return f"{self.nev};{self.ar};{self.cukor}"

#leszármaztatott osztéály, gyermek osztály
#minden tulajdonsága megvan , ami az ősosztálynak megvan, és minden metódus is.    
class Kave(Forroital):
    def __init__(self, nev, ar, cukor, tej):
        super().__init__(nev, ar, cukor) #super kulcsszó: az ősosztályra mutat rá, itt a Forróital osztály init metódusát hivja.
        self.tej = tej
    def aremeles(self):
        self.ar+=20
    def __str__(self):
        return f"{super().__str__()} {self.tej}"

class Tea(Forroital):
    def __init__(self, nev, ar, cukor, citrom):
        super().__init__(nev,ar,cukor)
        self.citrom = citrom
    def arameles(self):
        self.ar+=10
    def __str__(self):
        citrom = "citrom nélkül"
        if self.citrom:
            citrom = "citrommal"
        return f"{super().__str__()} {citrom}"

class Capucsino(Kave):
    def __init__(self, nev, ar, cukor, tej, tejszin):
        super().__init__(nev,ar,cukor,tej)
    
        self.tejszin = tejszin
    def aremeles(self):
        self.ar+=100
    def __str__(self):
        tejszin = "tejszin nelkul"
        if self.tejszin:
            tejszin = "tejszinnel"
        return f"{super().__str__()} {tejszin}"



def main():

    f = Forroital("Forrocsoki",200,2)
    print(f)
    f.aremeles()
    print(f)
    k = Kave("Expresso",230,5,"tej nélkül")
    print(k)
    k.aremeles()
    print(k)
    r = Tea("PirosBogyos",260,4,True)
    print(r)
    e = Capucsino("Pistacias",320,3,"tej nélkül",True)
    e.aremeles()
    print(e)
    print("-------------")
    lista = [f,k,r,e]
    for item in lista:
        if isinstance(item,Kave):
            print(item.nev,item.tej)
main()