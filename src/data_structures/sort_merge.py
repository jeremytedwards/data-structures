# coding=utf-8
import random
import timeit


def split_merge(origin_list):
    if len(origin_list) > 1:
        index = len(origin_list) // 2
        left = origin_list[:index]
        print("left:", left)
        split_merge(left)
        right = origin_list[index:]
        print("right:", right)
        split_merge(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                origin_list[k] = left[i]
                i = i + 1
            else:
                origin_list[k] = right[j]
                j = j + 1
            k = k + 1

        while i < len(left):
            origin_list[k] = left[i]
            i = i + 1
            k = k + 1

        while j < len(right):
            origin_list[k] = right[j]
            j = j + 1
            k = k + 1
    return origin_list


def main():
    test_list = [random.randint(1, 100) for i in range(11)]
    print(test_list)
    result = split_merge(test_list)
    print(result, timeit.timeit('split_merge', setup='from __main__ import split_merge', number=10000))

if __name__ == '__main__':
    main()
