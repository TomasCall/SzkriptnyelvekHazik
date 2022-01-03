

def main():
    digits = []
    for number in range(1,101):
        digits += list(str(number))
    int_digits = [int(number) for number in digits]
    print("1-től 100-ig a számjegyek összege: " +str(sum(int_digits)))


if __name__=="__main__":
    main()