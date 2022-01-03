import random


def shuffled(input_list):
    tmp_list = input_list[::1]
    random.shuffle(tmp_list)
    return tmp_list


def main():
    user_list = [1,2,3,4,5]
    print(f"Shuffeled lista: {shuffled(user_list)}")
    print(f"Eredeti lista: {user_list}")
    print(f"Shuffeled lista utolsó eleme: {shuffled(user_list)[-1]}")


if __name__ == "__main__":
    main()