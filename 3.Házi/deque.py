import collections


def main():
    deque_list = collections.deque(range(8))
    print("Deque: ",deque_list)
    print("Length: ",len(deque_list))


    deque_list.append(100)
    deque_list.appendleft(999)
    print("Deque: ",deque_list)


    deque_list.rotate(2)
    print('Right rotation:', deque_list)


    deque_list.rotate(-2)
    print('Left rotation :', deque_list)


if __name__=="__main__":
    main()