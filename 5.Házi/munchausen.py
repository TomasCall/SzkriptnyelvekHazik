


pows = (0, 1, 4, 27, 256, 3125, 46656, 823543, 16777216, 387420489)


def is_munchausen1(number):
    """
    A függvény a paraméterkén kapott számról eldönti hogy Münchausen szám-e
    Ha a szám Münchausen-szám akkor True-val ha pedig nem akkor False értékkel tér vissza
    Optimalizációként a függvény megvizsgálja először ahogy a legnagyobb számjegy nagyobb-e a számnál, ha igen akkor False-ként vissza tér
    A szám maradékos osztásával nézzük meg az utolsó számjegyet majd a hatványozás elvégzése után hozzáadjuk a sum_of_digit változóhoz amiben az eddigi hatványozott számösszegek vannak.
    Hibakeresés gyanánt itt is vizsgálom hogy átlépte-e már a sum_of_digit az eredeti szám értékét.
    """

    tmp_max_digit = int(max((str(number))))
    if pows[tmp_max_digit]>number:
        return False
    sum_of_digit=0
    tmp=number
    while tmp:
        tmp_digit = tmp % 10
        sum_of_digit += pows[tmp_digit]
        if sum_of_digit > number:
            return False
        tmp=tmp//10
    return sum_of_digit == number



def main():
    
    for i in range(440000000):
        if is_munchausen1(i):
            print(i)


if __name__=="__main__":
    main()