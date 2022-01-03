
def get_word():
    words = []
    f = open("DT2.txt")
    lines = f.read().splitlines()
    for line in lines:
        if len(line)>4:
            if "j" in line and "s" in line and "u" in line and "n" in line:
                if line.index("j") < line.index("s") and line.index("s") < line.index("u") and line.index("u") < line.index("n"):
                    words.append(line.split(",")[0])
    f.close()
    return words

def main():
    print("A keresett szavak amelyek segítenek a bolygók sorrendjének megjegyzésében:")
    for word in get_word():
        print(word)

if __name__ == "__main__":
    main()