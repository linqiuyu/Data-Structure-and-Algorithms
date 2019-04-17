class Node(object):
    """
    节点
    """
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLink(object):
    """
    循环链表
    """
    def __init__(self):
        self.__head = None

    def is_empty(self):
        """
        判断链表是否为空
        :return:
        """
        return not self.__head

