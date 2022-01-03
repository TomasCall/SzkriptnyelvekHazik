

def is_palindrom(text):
    i = 0
    j = len(text)-1
    while i < int(len(text)+0.5):
        if text[i] != text[j]:
            return False
        i += 1
        j -=1
    return True
      


def main():
    user_input = input("Adj megy egy sztringet! ")
    if is_palindrom(user_input):
        print("A szting palindróm!")
    else:
        print("A sztring nem palindróm!")


if __name__=="__main__":
    main()