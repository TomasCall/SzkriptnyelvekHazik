def type_of_sound_order(user_input):
    deep = ["a", "á", "o", "ó", "u", "ú"]
    high = ["e", "é", "i", "í", "ö", "ő", "ü", "ű"]
    deep_high=[False,False]
    for letter in user_input:
        if letter in deep:
            deep_high[0] = True
            break
    for letter in user_input:
        if letter in high:
            deep_high[1] = True
            break
    if deep_high[0] and deep_high[1]:
        return "m"
    elif deep_high[0]:
        return "d"
    elif deep_high[1]:
        return "h"
    else:
        return "n"


def main():
    user_input = input("Adj megy egy szót: ")
    type_of_user_input = type_of_sound_order(user_input)
    if type_of_user_input == "m":
        print("A szó típusa vegyes!")
    elif type_of_user_input == "d":
        print("A szó típusa mély!")
    elif type_of_user_input == "h":
        print("A szó típusa magas!")
    else:
        print("A szó típusa semmilyen!")

if __name__=="__main__":
    main()