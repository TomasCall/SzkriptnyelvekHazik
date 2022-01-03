def main():
    while True:
        try:
            szam1 = float(input("1. szam: "))
            szam2 = float(input("2. szam: "))
            result = szam1 / szam2
            print('Az osztas eredmenye: {0:.2f}'.format(result))
            print('-' * 10)
        except ValueError:
            print("Kérlek számot adj meg ne szöveget. Tört szám esetén ne vesszőt, hanem pontot használj!")
        except KeyboardInterrupt:
            break
        except ZeroDivisionError:
            print("A nullával való osztás nem értelmezett.")

#####

if __name__ == "__main__":
    main()