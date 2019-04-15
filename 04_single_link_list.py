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
        self.__foot = None

    def is_empty(self):
        return not self.__head

    def length(self):
        count = 0
        cur = self.__head
        while cur:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self.__head
        while cur:
            print(cur.data)
            cur = cur.next

    def add(self, item):
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
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

    def insert(self, node):
        pass

    def remove(self, item):
        pass

    def search(self, item):
        pass


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
