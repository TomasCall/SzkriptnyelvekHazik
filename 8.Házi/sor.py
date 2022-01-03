class Sor:
    def __init__(self):
        self.sor=[]


    def ures(self):
        return len(self.sor)==0


    def meret(self):
        return len(self.sor)

    def betesz(self,elem):
        self.sor.append(elem)

    
    def kivesz(self):
        if self.ures():
            return "Üres sorból akartál kivenni"
        else:
            return self.sor.pop(0)


    def __str__(self):
        return f"{self.sor}"


def main():
    s = Sor()
    print(s)
    print(s.ures())
    s.betesz(1)
    s.betesz(4)
    s.betesz(5)
    print(s)
    print(s.meret()) 
    print(s.ures())
    x = s.kivesz()
    print(x)
    print(s)
    s.kivesz()
    s.kivesz()
    x = s.kivesz()
    print(x)

if __name__=="__main__":
    main()