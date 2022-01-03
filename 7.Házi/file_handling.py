

from os import linesep


def main():
    file = open("string1.py","r")
    print("Olvasás megkezdése!")
    lines = file.readlines()
    file.close()
    print("Olvasás befejezése!")
    print("Írás megkezdése!")
    file = open("string1_clean.py","w")
    for line in lines:
        if "#" not in line:
            file.write(line)
    file.close()
    print("Írás befejezése!")


if __name__=="__main__":
    main()