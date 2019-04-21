def insert_sort(a):
    for i in range(1, len(a)):
        while i > 0:
            if a[i] < a[i-1]:
                a[i], a[i-1] = a[i-1], a[i]
                i -= 1
            else:
                break
    return a


if __name__ == '__main__':
    a = [2, 5, 7, 23, 1, 22, 34, 67, 12]
    insert_sort(a)
    print(a)
