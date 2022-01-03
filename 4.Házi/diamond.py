def diamond_drawing(height):
    if height % 2 == 0:
        print("Hiba páratlan számot kell megadnod!")
    else:
        lines = []
        for i in range(1,int(height/2+0.5)+1):
            left = "*" * i
            right = "*" * int(len(left)-1)
            a = int(height/2+0.5)-i
            space = " " * a
            lines.append(space+left+right)
        for i in range(int(height/2+0.5)-1,0,-1):
            left = "*" * i
            right = "*" * int(len(left)-1)
            a = int(height/2+0.5)-i
            space = " " * a
            lines.append(space+left+right)    
        for i in lines:
            print(i)


def main():
    user_input = int(input("Add meg milyen magas legyen a gyémánt!(Páratlan számot adj meg) "))
    diamond_drawing(user_input)


if __name__=="__main__":
    main()