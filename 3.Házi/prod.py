def product(numbers):
    tmp = 1
    for number in numbers:
        tmp *=number
    return tmp


def main():
    numbers = [1 , 2 , 3 , 4 , 5]
    print(f"Product:{product(numbers)}")


if __name__=="__main__":
    main()