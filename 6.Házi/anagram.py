
def normalize(word):
    result_word=""
    for character in word:
        if character != " ":
            result_word += character
    return result_word.lower()


def is_anagram1(word1,word2):
    return sorted(normalize(word1)) == sorted(normalize(word2))

def is_anagram2(word1,word2):
    return set(normalize(word1)) == set(normalize(word2))


def main():
    user_input1 = input("Adj meg egy szót! ")
    user_input2 = input("Adj meg egy szót! ")
    if is_anagram1(user_input1,user_input2):
        print("A két szó anagramma!")
    else:
        print("A két szó nem anagramma! ")

if __name__=="__main__":
    main()
       