from __future__ import division
import random
import timeit


def sort_radix(origin_list):
    """
    Takes a list and returns a sorted list using radix method
    :param origin_list:
    :return: origin_list sorted
    """
    if len(origin_list) == 0:
        return origin_list
    radix = 10
    for i in range(len(str(max(origin_list)))):
        sub_list = [[] for x in range(10)]
        for num in origin_list:
            sub_list[(num % radix) // (radix // 10)].append(num)
        radix *= 10
        origin_list = [num for bucket in sub_list for num in bucket]
    return origin_list


def main():
    test_list_1 = [random.randint(999, 100000) for i in range(20)]
    print(test_list_1)
    result = sort_radix(test_list_1)
    print(result, timeit.timeit('sort_radix', setup='from __main__ import sort_radix',
                                number=1000))

    # Test Random List
    random_list = [random.randint(1, 10000) for i in range(10000)]
    print("\nRandom Set:\n", random_list)

    result = sort_radix(random_list)
    print("Random Set Result:\n", result)
    print('\nRadix Sort: Sort time: {}'.format(
        timeit.timeit("sort_radix", setup="from __main__ import sort_radix",
                      number=500)))

    # Test Ordered List
    ordered_list = [i + 1 for i in range(random.randint(1, 10000))]
    print("\nOrdered Set:\n", ordered_list)

    result = sort_radix(ordered_list)
    print("Ordered Set Result:\n", result)
    print('\nRadix Sort: Sort time: {}'.format(
        timeit.timeit("sort_radix", setup="from __main__ import sort_radix",
                      number=500)))

    # Test Reversed List
    reversed_list = [i for i in range(random.randint(1, 10000))][::-1]
    print("\nReversed Set:\n", reversed_list)

    result = sort_radix(reversed_list)
    print("Reversed Set Result:\n", result)
    print('\nRadix Sort: Sort time: {}'.format(
        timeit.timeit("sort_radix", setup="from __main__ import sort_radix",
                      number=500)))


if __name__ == '__main__':
    main()