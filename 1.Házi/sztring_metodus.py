# A program bekér egy szót a felhasználótól és kiírja annak a nagybetűs változatát. 


def main():
    user_input = input("Adj meg egy szót légyszives: ")
    print(user_input.upper())


if __name__=="__main__":
    main()