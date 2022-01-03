
def converter(binary_string):
    binary_bytes = []
    for i in range(0, len(binary_string), 7):
        binary_bytes.append(str(int(binary_string[i:i + 7])))
    decimals = []
    for item in binary_bytes:
        tmp_item = item[::-1]
        tmp = 0
        for j in range(len(tmp_item)):
            tmp += int(tmp_item[j])*pows_of_two[j]
        decimals.append(tmp)
    output = ""
    for item in decimals:
        output += chr(item)
    return(output)


pows_of_two = (1,2,4,8,16,32,64,128)
#0111100101101111011101010111010001110101001011100110001001100101001011110110010001010001011101110011010001110111001110010101011101100111010110000110001101010001

def main():
    user_input = input("Add meg a dekódolandó szöveget! ")
    print(f"A dekódolt szöveg: {converter(user_input)}")


if __name__ == '__main__':
    main()