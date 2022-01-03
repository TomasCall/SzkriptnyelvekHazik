
def digit_sum(number):
    tmp_number = number
    result = 0
    while tmp_number:
        tmp = tmp_number % 10
        result += tmp
        tmp_number = tmp_number // 10
    return result


def main():
    print(digit_sum(2**1000))

if __name__=="__main__":
    main()
       