

def main():
    #1
    words = ['auto', 'villamos', 'metro']
    words_upper = [s.upper() for s in words]
    print(words_upper)

    #2
    names = ['aladar', 'bela', 'cecil']
    names_capital=[s.capitalize() for s in names]
    print(names_capital)

    #3
    zeroes = [0 for i in range(10)]
    print(zeroes)

    #4
    multiplication_with_2 = [n*2 for n in range(1,11)]
    print(multiplication_with_2)

    #5
    strings = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    numbers = [int(n) for n in strings]
    print(numbers)

    #6
    string = "1234567"
    number_list = [int(item) for item in list(string)]
    print(number_list)

    #7
    sentence='The quick brown fox jumps over the lazy dog'
    words_len = [len(s) for s in sentence.split()]
    print(words_len)

    #8
    sentence = "python is an awesome language"
    first_letters = [word[0] for word in sentence.split()]
    print(first_letters)

    #9
    sentence = "The quick brown fox jumps over the lazy dog"
    words_and_length = [(word,len(word)) for word in sentence.split()]
    print(words_and_length)

    #10
    pairs = [number for number in range(0,11,2)]
    print(pairs)

    #11
    pairs_square = [number*number for number in range(0,21,2)]
    print(pairs_square)

    #12
    end_four = [number*number for number in range(20) if int(str(number*number)[-1])==4]
    print(end_four)

    #13
    english_alphabet = "".join([chr(letter) for letter in range(65,91)])
    print(english_alphabet)

    #14
    words_with_whitespace = [' apple ', ' banana ', ' kiwi']
    words_without_whitespace = [word.strip() for word in words_with_whitespace]
    print(words_without_whitespace)

    #15
    binary_list = [1, 0, 1, 1, 0, 1, 0, 0]
    binary_string = "".join([str(n) for n in binary_list])
    print(binary_string)

if __name__=="__main__":
    main()