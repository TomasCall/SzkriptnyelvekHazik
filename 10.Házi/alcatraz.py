

def main():

    doors = []
    for i in range(600):
        doors.append(False)
    i = 1
    while i <= 600:
        j=i-1
        while j < 600:
            if doors[j]:
                doors[j] = False
            else:
                doors[j] = True
            j += i
        i += 1
    print(f"A szabaduló foglyok cellaszámai: ",end="")
    for d in range(0,600):
        if doors[d]:
            print(d+1,end=" ")



if __name__ == "__main__":
    main()