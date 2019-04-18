def bubble_sort(li):
    """
    冒泡排序
    :param li:list
    :return: list
    """
    count = len(li)
    while count:
        exchange = False
        for i in range(0, count-1):
            if li[i] > li[i+1]:
                li[i], li[i+1] = li[i+1], li[i]
                exchange = True
        count -= 1
        if not exchange:
            break
    return li


if __name__ == '__main__':
    li = [1, 34, 56, 89, 12, 43, 22]
    li = bubble_sort(li)
    print(li)
