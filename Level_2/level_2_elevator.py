# The code implements a modified quick sort algorithm
# The only modification is a properly defined comparison between two version.


def fill_zeros(lis):  # replace empty minors or revisions with zeros
    if len(lis) < 3:
        lis.extend([0] * (3- len(lis)))


def less_or_equal(v1, v2):
    '''Compares two versions and returns true if v1 <= v2'''
    l1, l2 = [int(s) for s in v1.split('.')], [int(s) for s in v2.split('.')]
    len1, len2 = len(l1), len(l2)  # save the original lengths of l1 and l2
    fill_zeros(l1)
    fill_zeros(l2)
    for n1, n2 in zip(l1, l2):
        if n1 < n2:
            return True
        if n1 > n2:
            return False
    # if all three numbers are equal
    if len1 <= len2:
        return True
    return False


def partition(lst, start, end):
    j = start
    for i in range(start + 1, end + 1):
        if less_or_equal(lst[i], lst[start]):
            j += 1
            lst[i], lst[j] = lst[j], lst[i]

    lst[start], lst[j] = lst[j], lst[start]
    return j


def quick_sort(lst, start, end):
    if start >= end:
        return
    j = partition(lst, start, end)
    quick_sort(lst, start, j - 1)
    quick_sort(lst, j + 1, end)


def solution(l):
    quick_sort(l, 0, len(l) - 1)
    return l


# print(solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]))

