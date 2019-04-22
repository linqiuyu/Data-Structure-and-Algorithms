def shell_sort(a):
    """
    希尔排序
    :param a:
    :return:
    """
    length = len(a)
    gap = length // 2
    while gap:
        for i in range(gap, length):
            while i > 0:
                if a[i] < a[i-gap]:
                    a[i], a[i-gap] = a[i-gap], a[i]
                    i -= gap
                else:
                    break
        gap //= 2


if __name__ == '__main__':
    li = [54, 65, 21, 33, 2, 11, 78]
    shell_sort(li)
    print(li)
