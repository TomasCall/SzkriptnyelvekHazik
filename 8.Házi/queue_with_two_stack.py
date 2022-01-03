class Queue:
    def __init__(self):
        self.stack_one = []
        self.stack_two = []
 
    
    def append(self, new_item):
        while len(self.stack_one) != 0:
            self.stack_two.append(self.stack_one[-1])
            self.stack_one.pop()
        self.stack_one.append(new_item)
        while len(self.stack_two) != 0:
            self.stack_one.append(self.stack_two[-1])
            self.stack_two.pop()


    def is_empty(self):
        return len(self.stack_one)==0

    
    def size(self):
        return len(self.stack_one)

    
    def popleft(self):
        if self.is_empty():
            print("A sor üres!")
        item = self.stack_one[-1]
        self.stack_one.pop()
        return item
 

if __name__ == '__main__':
    q = Queue()
    print(f"is_empty() értéke: {q.is_empty()}")
    q.append(4)
    q.append(3)
    print(f"Sor hossza: {q.size()}")
    q.append(7)
 
    print(f"pop: {q.popleft()}")
    print(f"pop: {q.popleft()}")
    print(f"pop: {q.popleft()}")