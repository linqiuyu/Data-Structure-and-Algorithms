class Stack(object):
    """
    栈
    """
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


def number_to_list(number):
    """
    将数字转化为列表
    :param number:
    :return:list
    """
    result = []
    i = 10
    while number != 0:
        n = number % i
        result.append(int(n / (i / 10)))
        i = i * 10
        number = number - n
    result.reverse()
    return result


def conversion(num, x):
    """
    将10进制数转化为8进制
    :param num:
    :param x:
    """
    s = Stack()
    while num:
        s.push(num % x)
        num = num // x

    while not s.is_empty():
        print(s.pop())


if __name__ == '__main__':
    num = number_to_list(123456)
    print(num)
