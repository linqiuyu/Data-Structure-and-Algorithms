def binary_search(a, item):
    """
    二分查找, 递归
    :param a:
    :param item:
    :return:bool
    """
    length = len(a)

    if length > 1:
        mid_index = length // 2
        if a[mid_index] == item:
            return True
        elif a[mid_index] > item:
            return binary_search(a[:mid_index], item)
        else:
            return binary_search(a[mid_index:], item)
    if a[0] == item:
        return True
    return False


def binary_search2(a, item):
    """
    二分查找, 非递归
    :param a:
    :param item:
    :return:
    """
    length = len(a)
    first = 0
    last = length - 1
    while first <= last:
        mid_index = (first + last) // 2
        if a[mid_index] == item:
            return True
        elif a[mid_index] > item:
            last = mid_index - 1
        else:
            first = mid_index + 1
    return False


if __name__ == '__main__':
    a = [2, 3, 6, 8, 12, 34, 54]
    print(binary_search(a, 4))
    print(binary_search(a, 12))
    print(binary_search2(a, 4))
    print(binary_search2(a, 12))
