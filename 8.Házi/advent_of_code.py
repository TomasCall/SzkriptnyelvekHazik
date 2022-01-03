

def main():
    file = open("day02.txt","r")
    lines = file.read().splitlines()
    differences = []
    for line in lines:
        tmp_numbers = []
        for number in line.split("\t"):
            tmp_numbers.append(int(number))
        differences.append(max(tmp_numbers)-min(tmp_numbers))
    print(f"Az input táblázatunk ellenörző összege:{sum(differences)}")


if __name__=="__main__":
    main()