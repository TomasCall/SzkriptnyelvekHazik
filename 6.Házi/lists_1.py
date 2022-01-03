# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# A magyar változatot készítette:
# Szathmáry László (jabba.laci@gmail.com)
# frissítés Python 3-ra: 2016.09.09.


# A. match_ends
# Bemenet: sztringek listája. Számoljuk meg, hogy a bemenetben
# hány olyan sztring van, melynek a hossza legalább 2 s az
# első karaktere egyezik az utolsó karakterével. A visszatérési
# érték ezen feltételeket kielégítő sztringek száma legyen.
# Megjegyzés: Pythonban inkrementálásra a ++ helyett a += operátort használjuk.
def match_ends(words):
    count = 0
    for word in words:
        if  len(word)>=2 and word[0] == word[-1]:
            count += 1
    return count


# B. front_x
# Bemenet: sztringek listája. Egy olyan listával térjünk vissza,
# melyben a szavak rendezve vannak, viszont az 'x'-szel kezdődő szavak
# kerüljenek előre.
# Példa: ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] bemenet esetén
# az eredmény: ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'].
# Tipp: használhatunk 2 listát is, melyeket külön-külön rendezünk, majd
#       egyesítjük őket.
def front_x(words):
    tmp = []
    for word in sorted(words):
        if word[0] == "x":
            tmp.append(word)
    tmp.sort()
    i = 0
    while(sorted(words)[i][0] != "x"):
        tmp.append(sorted(words)[i])
        i += 1
    return tmp


# Egy egyszerű teszt fv. Kiírja az egyes fv.-ek visszaadott értékét, ill.
# azt is, hogy mit kellett volna visszaadniuk.


# Ezt ne módosítsuk.
# A main() fv. meghívja a fenti fv.-eket különféle paraméterekkel,
# s a test() fv. segítségével megnézi, hogy az eredmények helyesek-e.
def main():
    pass

#############################################################################

if __name__ == '__main__':
    main()