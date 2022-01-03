def main():
    chars = "abcdefghijklmnopqrstuvwxyz"
    codes = list(range(ord("a"), ord("z")+1))
    for t in range(26):
        print(f"('{chars[t]}' , {codes[t]})")


if __name__ == '__main__':
    main()