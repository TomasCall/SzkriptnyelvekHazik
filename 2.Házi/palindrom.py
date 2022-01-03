def is_palindrom(text):
    if text==text[::-1]:
        return True
    else:
        return False


def main():
    user_input = input("Adj meg egy sztringet! ")
    if is_palindrom(user_input):
        print("A szting palindróm!")
    else:
        print("A sztring nem palindróm!")
        

if __name__=="__main__":
    main()
