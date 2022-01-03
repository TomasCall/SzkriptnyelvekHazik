import sys


def main():
    characters = "abcdefghijklmnopqrstuvwxyz"
    if "a-z.py" in sys.argv[0]:
        print(characters)
    elif "z-a.py" in sys.argv[0]:
        print(characters[::-1])



if __name__ == "__main__":
    main()