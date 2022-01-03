import math

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]


def get_lottery_numbers(numbers):
    for i in numbers:
        for j in range(i):
            for k in range(j):
                for l in range(k):
                    for m in range(l):
                        for n in range(m):
                            tmp = [numbers[i],numbers[j],numbers[k],numbers[l],numbers[m],numbers[n]]
                            if sum(tmp) == 90:
                                if numbers[i]*numbers[j]*numbers[k]*numbers[l]*numbers[m]*numbers[n] == 996300:
                                    return tmp




def main():
    print(f"A keresett lottószámok: {get_lottery_numbers(nums)}")
    print()


if __name__ == "__main__":
    main()