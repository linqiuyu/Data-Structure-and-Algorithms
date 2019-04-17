class Node(object):
    """
    节点
    """
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLink(object):
    """
    单链表
    """
    def __init__(self):
        self.__head = None

    def is_empty(self):
        """
        判断链表是否为空
        :return:
        """
        return not self.__head

    def length(self):
        """
        获取链表的长度
        :return:
        """
        count = 0
        cur = self.__head
        while cur:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """
        遍历链表
        :return:
        """
        cur = self.__head
        while cur:
            print(cur.data, end=' ')
            cur = cur.next
        print('')

    def add(self, item):
        """
        在头部添加元素
        :param item:
        :return:
        """
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        """
        在尾部添加元素
        :param item:
        :return:
        """
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur:
                if cur.next is None:
                    cur.next = node
                    break
                cur = cur.next

    def insert(self, pos, item):
        """
        在指定位置添加元素
        :param pos:
        :param item:
        :return:
        """
        if pos <= 0:
            self.add(item)
        elif pos > self.length():
            self.append(item)
        i = 0
        node = Node(item)
        cur = self.__head
        while i < (pos - 1):
            cur = cur.next
            i += 1
        node.next = cur.next
        cur.next = node

    def remove(self, item):
        """
        移除指定元素
        :param item:
        :return:
        """
        if self.__head is None:
            return
        cur = self.__head
        if cur.data == item:
            self.__head = cur.next
        while cur.next is not None:
            if cur.next.data == item:
                cur.next = cur.next.next
                break
            cur = cur.next

    def search(self, item):
        """
        查找元素
        :param item:
        :return:
        """
        cur = self.__head
        while cur is not None:
            if cur.data == item:
                return True
            cur = cur.next
        return False


if __name__ == '__main__':
    link_list = SingleLink()
    print(link_list.is_empty())
    print(link_list.length())

    link_list.append(1)
    print(link_list.is_empty())
    print(link_list.length())
    link_list.append(2)
    link_list.append(3)
    link_list.append(4)
    print(link_list.length())
    link_list.travel()

    link_list.add(5)
    print(link_list.length())
    link_list.travel()

    link_list.insert(2, 7)
    link_list.travel()

    link_list.remove(5)
    link_list.travel()
