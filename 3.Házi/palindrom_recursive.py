def is_palindrom(text,left_index,right_index):
    if len(text) == 1 or left_index == int(len(text)+0.5):
        return True
    else:
        if text[left_index] == text[right_index]:
            return is_palindrom(text,right_index+1,left_index-1)
        else:
            return False


def main():
    user_input = input("Adj megy egy sztringet! ")
    if is_palindrom(user_input,0,len(user_input)-1):
        print("A szting palindróm!")
    else:
        print("A sztring nem palindróm!")


if __name__=="__main__":
    main()