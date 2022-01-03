def int_reverse(number):
    tmp = str(number)
    return int(tmp[::-1])


def main():
    number = int(input("Adj meg egy pozitív egész számot! "))
    print("A számod megfordítva: " + str(int_reverse(number)))
    

if __name__=="__main__":
    main()