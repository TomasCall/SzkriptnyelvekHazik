import math


def is_prime_number(number: int) -> bool:
    sqrt_of_number = int(math.sqrt(number))+1
    for i in range(2,sqrt_of_number+1):
        if number % i == 0:
            return False
    return True


def is_palindrom(text: str) -> bool:
    if int(text)==int(text[::-1]):
        return True
    else:
        return False


def palinrom_prime(number: int) -> int:
    i = number
    while True:
        if is_palindrom(str(i)):
            if is_prime_number(i):
                return i
        i += 1


def main():
    user_input = int(input("Adj meg egy számot és megmondom az utána kövekező első palindróm prím számot! "))
    print(palinrom_prime(user_input))


if __name__ == "__main__":
    main()