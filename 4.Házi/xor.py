

def main():
    str1 = "python"
    str2 = None
    if (bool(str1) and not bool(str2)) or (bool(str2) and not bool(str1)):
        print("Teljesül a XOR művelet! ")
    else:
        print("Nem teljesül a XOR művelet! ")

if __name__=="__main__":
    main()