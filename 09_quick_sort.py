def quick_sort(a, first=0, last=0):
    """
    快速排序
    :param a:
    :param first:
    :param last:
    :return:
    """
    length = len(a)
    mid_value = a[first]
    low = first
    if last == 0:
        last = length - 1
    high = last
    while low < high:
        while low < high and a[high] > mid_value:
            high -= 1
        a[low] = a[high]
        while low < high and a[low] <= mid_value:
            low += 1
        a[high] = a[low]
    a[low] = mid_value

    if first < low-1:
        quick_sort(a, first, low-1)
    if last > low+1:
        quick_sort(a, low+1, last)


if __name__ == '__main__':
    a = [2, 4, 5, 7, 89, 0]
    quick_sort(a)
    print(a)
