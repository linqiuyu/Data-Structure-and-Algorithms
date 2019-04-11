class Stack(object):
    def __init__(self):
        self.__list = []

    def destroy(self):
        self.__list = None

    def clear(self):
        self.__list = []

    def is_empty(self):
        return not self.__list

    def get_top(self):
        return self.__list[-1]

    def push(self, value):
        self.__list.append(value)

    def pop(self):
        return self.__list.pop()


if __name__ == '__main__':
    s = Stack()
    for i in range(10):
        s.push(i)

    while not s.is_empty():
        print(s.pop())
