# coding=utf-8
import random
import timeit


def split_merge(origin_list):
    if len(origin_list) > 1:
        index = len(origin_list) // 2
        left = origin_list[:index]

        # print("left:", left)
        split_merge(left)
        right = origin_list[index:]

        # print("right:", right)
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


def sort_merge(origin_list):
    """
    Takes a list and recursively sorts the left and right, merging on the way
    back up the recursion.
    :param origin_list:
    :return: result of ordered_lists(left, right)
    """
    # if: size is one or less return the list
    if len(origin_list) <=1:
        return origin_list

    # else: recursively find the left and right of list to sort from
    midpoint = len(origin_list) // 2
    left = sort_merge(origin_list[:midpoint])
    right = sort_merge(origin_list[midpoint:])

    return order_lists(left, right)


def order_lists(left, right):
    """
    Takes two lists and returns the merged set
    :param left:
    :param right:
    :return: merged set of left and right list
    """
    if not left:
        return right
    if not right:
        return left

    if left[0] < right[0]:
        return [left[0]] + order_lists(left[1:], right)

    return [right[0]] + order_lists(left, right[1:])


def main():
    test_list = [random.randint(1, 100) for i in range(11)]
    print(test_list)
    result = split_merge(test_list)
    print(result, timeit.timeit('split_merge', setup='from __main__ import split_merge', number=10000))

    # Test Random List
    random_list = [random.randint(1, 10000) for i in range(10000)]
    print("\nRandom Set:\n", random_list)

    result = split_merge(random_list)
    print("Random Set Result:\n", result)
    print('\nSplit_merge: Sort time: {}'.format(
        timeit.timeit("split_merge", setup="from __main__ import split_merge",
                      number=500)))
    print('Sort_merge: Sort time: {}\n'.format(
        timeit.timeit("sort_merge", setup="from __main__ import sort_merge",
                      number=500)))

    # Test Ordered List
    ordered_list = [i + 1 for i in range(random.randint(1, 10000))]
    print("\nOrdered Set:\n", ordered_list)

    result = split_merge(ordered_list)
    print("Ordered Set Result:\n", result)
    print('\nSplit_merge: Sort time: {}'.format(
        timeit.timeit("split_merge", setup="from __main__ import split_merge",
                      number=500)))
    print('Sort_merge: Sort time: {}\n'.format(
        timeit.timeit("sort_merge", setup="from __main__ import sort_merge",
                      number=500)))

    # Test Reversed List
    reversed_list = [i for i in range(random.randint(1, 10000))][::-1]
    print("\nReversed Set:\n", reversed_list)

    result = split_merge(reversed_list)
    print("Reversed Set Result:\n", result)
    print('\nSplit_merge: Sort time: {}'.format(
        timeit.timeit("split_merge", setup="from __main__ import split_merge",
                      number=500)))
    print('Sort_merge: Sort time: {}\n'.format(
        timeit.timeit("sort_merge", setup="from __main__ import sort_merge",
                      number=500)))

if __name__ == '__main__':
    main()
