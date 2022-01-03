from enum import Enum

class High(Enum):
    e = "e"
    é = "é"
    i = "i"
    í = "í"
    ö = "ö"
    ő = "ő"
    ü = "ü"
    ű = "ű"

class Deep(Enum):
    a = "a"
    á = "á"
    o = "o"
    ó = "ó"
    u = "u"
    ú = "ú"

def idenefy_sound_order(word):
    deep = 0
    high = 0
    tmp_word = word.lower()
    for charcter in tmp_word:
        for data in Deep:
            if charcter == data.value:
                deep += 1
    for charcter in tmp_word:
        for data in High:
            if charcter == data.value:
                high += 1
    if deep != 0 and high == 0:
        return 1
    elif deep == 0 and high != 0:
        return 2
    elif deep != 0 and high != 0:
        return 3
    else:
        return 4



def main():
    user_input = input("Adj meg egy szót és megmondom a hangrendjét!")
    sound_order = idenefy_sound_order(user_input)
    if sound_order == 1:
        print("A megadott szó mély")
    elif sound_order == 2:
        print("A megadott szó magas")
    elif sound_order == 3:
        print("A megadott szó vegyes")
    else:
         print("A megadott szó semmilyen!")

if __name__=="__main__":
    main()