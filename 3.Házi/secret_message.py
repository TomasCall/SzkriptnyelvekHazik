

MESSAGE = """
Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb
"""


def main():
    makrs = ";:.!\n "
    decoded=""""""
    for character in MESSAGE:
        if character not in makrs:
            if ord(character)+2 > 122:
                decoded += chr(97+121-ord(character))
            elif ord(character)+2 <= 122 and ord(character)+2>=97:
                decoded += chr(ord(character)+2)
            elif ord(character)+2 > 90:
                decoded += chr(65+89-ord(character))
            else:
                decoded += chr(ord(character)+2)
        else:
            decoded += character
    print(decoded.strip())

    

if __name__=="__main__":
    main()