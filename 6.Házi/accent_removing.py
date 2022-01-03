

def accent_removal(text):
    accent_dictionary = {"á":"a","é":"e","í":"i","ó":"o","ö":"o","ő":"o","ú":"u","ü":"u","ű":"u","Á":"A","É":"E","Í":"I","Ó":"O","Ö":"O","Ő":"O","Ú":"U","Ü":"U","Ű":"U"}
    result_text = ""
    for character in text:
        if character in accent_dictionary:
            result_text += accent_dictionary[character]
        else:
            result_text += character
    return result_text

def main():
    TEXT = """
A katalán zászló, a Senyera színeit fogja viselni a következő idény során a spanyol élvonalban szereplő FC Barcelona labdarúgócsapata.

A Marca című sportnapilap hétfői internetes kiadása szerint az együttes játékosai az idegenbeli mérkőzéseken húzzák majd magukra a sárga-piros csíkozású mezt - első ízben a klub történelme során.

A döntés várhatóan nem marad politikai visszhang nélkül Spanyolországban, tekintettel a katalán önállósodási törekvésekre.
"""
    print(accent_removal(TEXT))


####################################################################################################


if __name__=="__main__":
    main()
       