# O(logN) time | O(logN) space
def recursivebinarysearch(array, target):
    return recursivebinarysearch(array, target, 0, len(array)-1)


def binarysearchhelper(array, target, left, right):
    if left > right:
        return -1
    middle = (left + right) // 2
    potentialMatch = array[middle]
    if target == potentialMatch:
        return middle
    elif target < potentialMatch:
        return binarysearchhelper(array, target, left, middle - 1)
    else:
        return binarysearchhelper(array, target, middle + 1, right)


# BEST OPTION
# Time O(logN) | Space O(1)
def iteractivebinarysearch(array, target):
    left = 0
    right = len(array)-1
    while left <= right:
        middle = (left + right) // 2
        potentialMatch = array[middle]
        if target == potentialMatch:
            return middle
        elif target < potentialMatch:
            right = middle - 1
        else:
            left = middle + 1
    return -1