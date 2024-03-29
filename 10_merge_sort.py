def merge_sort(a):
    """
    归并排序
    :param a:
    :return:
    """
    length = len(a)
    if length <= 1:
        return a
    mid = length//2

    left_li = merge_sort(a[:mid])
    right_li = merge_sort(a[mid:])
    left_pointer, right_pointer = 0, 0
    result = []

    while left_pointer < len(left_li) and right_pointer < len(right_li):
        if left_li[left_pointer] < right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer += 1
        else:
            result.append(right_li[right_pointer])
            right_pointer += 1

    result += left_li[left_pointer:]
    result += right_li[right_pointer:]
    return result


if __name__ == '__main__':
    a = [3, 8, 1, 98, 1, 2]
    a = merge_sort(a)
    print(a)
