
def get_last_item(items):
    return items[-1]

def get_id(data):
    return int(data.split(":")[0])


def get_second_column(matrix):
    return matrix[1]


def main():
    #1.,
    data = [ (1, 'Albany', 'NY', 162692), (3, 'Allegany', 'NY', 11986), (121, 'Wyoming', 'NY', 8722), (123, 'Yates', 'NY', 5094)]
    print(f"A data lista rendezve a tuple-ök utolsó értéke szerint:")
    for item in sorted(data,key=get_last_item):
        print(item)
    #2.,
    lst = ['10:User1', '80:User2', '100:User3', '00:User4', '75:User4', '45:User5']
    print(f"A lista rendezve id szerint csökkenő sorrendben:")
    for item in sorted(lst,key=get_id)[::-1]:
        print(item)
    #3.,
    li=[ [2,6],[1,3],[5,4] ]
    print(f"A második oszlop szerint rendezett mátrix:")
    for item in sorted(li,key=get_second_column):
        print(item)


if __name__ == "__main__":
    main()