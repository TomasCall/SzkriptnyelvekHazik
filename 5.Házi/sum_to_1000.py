

def main():
    multiple_sum = sum([i for i in range(3,1001,3)]) + sum([i for i in range(5,1001,5)])
    print(f"Az 1000-nél kisebb számok összege, melyek 3-nak vagy 5-nek a többszörösei: {multiple_sum}")


if __name__=="__main__":
    main()