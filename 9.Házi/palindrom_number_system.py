from palindrom_prime import is_palindrom


def decimal_to_binary(num: int) -> str:
    return "{0:b}".format(int(num))


def main():
    sum = 0
    for i in range(1000001):
        if is_palindrom(str(i)):
            if is_palindrom(decimal_to_binary(i)):
                sum += i
    print(f"Azoknak a számoknak az összege amelyek mind a binárias, és a deciámlis számrendszerben palindromok: {sum}")


if __name__ == "__main__":
    main()