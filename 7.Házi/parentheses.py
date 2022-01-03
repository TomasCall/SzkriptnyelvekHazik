open_parentheses  = ("[","{","(")
close_parentheses  = ("]","}",")")


def is_balanced(expression):
    expression_parentheses = []
    for i in expression:
        if i in open_parentheses:
            expression_parentheses.append(i)
        elif i in close_parentheses:
            close_parentheses_index = close_parentheses.index(i)
            if len(expression_parentheses) > 0 and open_parentheses[close_parentheses_index] == expression_parentheses[len(expression_parentheses)-1]:
                expression_parentheses.pop()
            else:
                return False
    return len(expression_parentheses) == 0

  
def main():
    user_input = input("Adj meg egy kifejezést! ")
    if is_balanced(user_input):
        print("A kifejezés a zárójelek szempontjából helyes!")
    else:
        print("A kifejezés a zárójelek szempontjából helytelen!")


if __name__=="__main__":
    main()