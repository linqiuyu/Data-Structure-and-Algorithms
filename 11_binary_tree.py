class Node(object):
    """
    节点
    """
    def __init__(self, item):
        self.elem = item
        self.left_child = None
        self.right_child = None


class Tree(object):
    """
    二叉树
    """
    def __init__(self):
        self.root = None

    def add(self, item):
        """
        添加节点
        :param item:
        :return:
        """
        node = Node(item)
        if self.root is None:
            self.root = Node(item)
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.left_child is None:
                cur_node.left_child = node
                return
            else:
                queue.append(cur_node.left_child)
            if cur_node.right_child is Node:
                cur_node.right_child = node
                return
            else:
                queue.append(cur_node.right_child)
