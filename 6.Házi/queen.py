

def drawing(positions):
    print("+-------------------------+")
    tmp_positions=[]
    for position in positions:
        tmp_positions.append(7-position)
    for i in range(8):
        line = "|"
        for j in range(8):
            if j == tmp_positions.index(i):
                line += " Q "
            else:
                line += " . "
        line += " |"
        print(line)
    print("+-------------------------+")

    

def main():
    user_input = input("Adj meg szóközzel elválasztva 8 különböző számot, 1-8-ig! ")
    positions = []
    for position in user_input.split():
        positions.append(int(position)-1)
    drawing(positions)

if __name__=="__main__":
    main()
       