class Verem:
    def __init__(self):
        self.verem=[]


    def ures(self):
        return len(self.verem)==0


    def meret(self):
        return len(self.verem)

    def betesz(self,elem):
        self.verem.append(elem)

    
    def kivesz(self):
        if self.ures():
            return "Üres veremből akartál kivenni"
        else:
            return self.verem.pop()


    def __str__(self):
        return f"{self.verem}"


def main():
    v = Verem()      # üres verem létrehozása
    print(v)         # [
    print(v.ures())  # True
    v.betesz(1)
    v.betesz(4)
    v.betesz(5)
    print(v)         # [1 4 5
    print(v.meret()) # 3
    print(v.ures())  # False
    x = v.kivesz()
    print(x)         # 5
    print(v)         # [1 4
    v.kivesz()
    v.kivesz()       # most már üres
    x = v.kivesz()
    print(x)         # None (jelezzük pl. így, hogy egy üres veremből akarunk kivenni)

if __name__=="__main__":
    main()