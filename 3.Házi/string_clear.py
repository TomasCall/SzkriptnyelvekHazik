def string_clearer(text):
    tmp = text.split()
    final = ""
    for character in tmp:
        final += character.strip()
    return final


def main():
    url1 = "206.130.99.82:\n8080"
    url2 = "192.20.246.138:\n 6666"
    print(f"A javított url1: {string_clearer(url1)}")
    print(f"A javított url2: {string_clearer(url2)}")
    

if __name__=="__main__":
    main()