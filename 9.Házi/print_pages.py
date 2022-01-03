

def pages(pages: str) -> list[int]:
    tmp = pages.split(",")
    result = []
    for element in tmp:
        if "-" in element:
            tmp_element_list = element.split("-")
            result+=range(int(tmp_element_list[0]), int(tmp_element_list[1])+1)
        else:
            result.append(int(element))
    return result


def main():
    user_input = input("Add meg mely oldalakat szeretnéd kinyomtatni!(Használható formátumok: 1-2 vagy 1,2 vagy 12-15,18-20) ")
    pages_list = pages(user_input)
    pages_string = ""
    for i in range(len(pages_list)):
        if i == len(pages_list) - 1:
            pages_string += str(pages_list[i])
        else:
            pages_string += str(pages_list[i]) + ", "
    print(f"Nyomtatandó oldalak: {pages_string}")


if __name__ == "__main__":
    main()