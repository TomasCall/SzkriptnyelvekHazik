
def median_value(data):
    tmp = sorted(data)
    if len(tmp) % 2 == 0:
        return (tmp[int(len(tmp)/2)-1] + tmp[int(len(tmp)/2)])/2
    else:
        return tmp[int(len(tmp)/2)]


def main():
    user_input = input("Adj meg számokat szóközzel elválasztva, és megmondom a mediánjukat! ")
    numbers = []
    for number in user_input.split():
        numbers.append(int(number))
    print(f"A mediánja a megadott számaidnak: {median_value(numbers)}")


if __name__=="__main__":
    main()
       