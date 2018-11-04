import random


def insertion_sort(array):
    pass


def merge_sort(array):
    def merge(arr1, arr2):
        lidx = 0
        ridx = 0
        res = []
        while lidx != len(arr1) and ridx != len(arr2):
            if arr1[lidx] < arr2[ridx]:
                res.append(arr1[lidx])
                lidx += 1
            else:
                res.append(arr2[ridx])
                ridx += 1
        if lidx != len(arr1):
            res += arr1[lidx:]
        elif ridx != len(arr2):
            res += arr2[ridx:]
        return res

    if len(array) <= 1:
        return array
    pivot = int(len(array) / 2)
    left = merge_sort(array[:pivot])
    right = merge_sort(array[pivot:])
    result = merge(left, right)
    return result


def quick_sort(array):
    # pick righmost element as pivot always
    if len(array) <= 1:
        return array
    pivot = array[-1]
    left = []
    right = []
    for i in array[:-1]:
        if i < pivot:
            left.append(i)
        else:
            right.append(i)
    return quick_sort(left) + [pivot] + quick_sort(right)


def bucket_sort(array, bucket_size):
    pass


min_int = 0  # min value of integer
max_int = 9999  # max value of integer
array_size = 100  # length of array to sort
test_arr = []
# not using numpy
for i in range(array_size):
    test_arr.append(random.randint(min_int, max_int))
# start sort
qs = quick_sort(test_arr)
for j in range(array_size - 1):
    if qs[j] > qs[j + 1]:
        print("QUICKSORT ERROR")
        exit(1)
ms = merge_sort(test_arr)
for j in range(array_size - 1):
    if ms[j] > ms[j + 1]:
        print("MERGESORT ERROR")
        exit(1)
