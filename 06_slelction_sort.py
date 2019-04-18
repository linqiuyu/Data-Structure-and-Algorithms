def selection_sort(li):
    """
    选择排序
    :param li:list
    :return: list
    """
    count = len(li)
    for j in range(count-1):
        min_index = j
        for i in range(j + 1, count):
            if li[min_index] > li[i]:
                min_index = i
        li[j], li[min_index] = li[min_index], li[j]
    return li


if __name__ == '__main__':
    li = [2, 54, 65, 21, 33, 11, 78]
    li = selection_sort(li)
    print(li)
