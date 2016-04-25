# coding=utf-8
import random
import timeit


def sort_insertion(origin_list):
    """Implement insertion sort."""
    if len(origin_list) == 0:
        return origin_list
    else:
        sorted_list = [origin_list.pop(0)]
        while len(origin_list) > 0:
            item = origin_list.pop(0)
            for index, v in enumerate(sorted_list):
                if v >= item:
                    sorted_list.insert(index, item)
                    break
                elif sorted_list[-1] < item:
                    sorted_list.append(item)
                    break
        return sorted_list


def main():
    # Test Random List
    random_list = [random.randint(1, 10000) for i in range(10000)]
    print("\nRandom Set:\n", random_list)

    result = sort_insertion(random_list)
    print("Random Set Result:\n", result)
    print('\nSort time: {}\n'.format(
        timeit.timeit("sort_insertion", setup="from __main__ import sort_insertion",
                      number=500)))

    # Test Ordered List
    ordered_list = [i + 1 for i in range(random.randint(1, 10000))]
    print("\nOrdered Set:\n", ordered_list)

    result = sort_insertion(ordered_list)
    print("Ordered Set Result:\n", result)
    print('\nSort time: {}\n'.format(
        timeit.timeit("sort_insertion", setup="from __main__ import sort_insertion",
                      number=500)))

    # Test Reversed List
    reversed_list = [i for i in range(random.randint(1, 10000))][::-1]
    print("\nReversed Set:\n", reversed_list)

    result = sort_insertion(reversed_list)
    print("Reversed Set Result:\n", result)
    print('\nSort time: {}\n'.format(
        timeit.timeit("sort_insertion", setup="from __main__ import sort_insertion",
                      number=500)))


if __name__ == '__main__':
    main()
