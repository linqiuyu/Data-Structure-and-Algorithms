class Queue(object):
    """
    队列
    """
    def __init__(self):
        self.__list = []

    def enqueue(self, item):
        """
        添加一个元素到队列
        :param item:
        :return:
        """
        self.__list.append(item)

    def dequeue(self):
        """
        从头部删除一个元素
        :return:
        """
        self.__list.pop(0)

    def is_empty(self):
        """
        判断队列是否为空
        :return:
        """
        return not self.__list

    def size(self):
        """
        队列的大小
        :return:
        """
        return len(self.__list)


if __name__ == '__main__':
    pass
