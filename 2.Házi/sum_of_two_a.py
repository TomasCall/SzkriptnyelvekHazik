import sys

def main():
    if len(sys.argv)<2:
        print("Nem adtad meg mindkét számot!")
    else:
        print(f"A két szám összege: {int(sys.argv[1])+int(sys.argv[2])}")
        

if __name__=="__main__":
    main()