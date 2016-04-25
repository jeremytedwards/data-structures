from __future__ import division
import random
import timeit


def sort_redix(origin_list):
    if origin_list is None:
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
    result = sort_redix(test_list_1)
    print(result, timeit.timeit('sort_redix', setup='from __main__ import sort_redix', number=1000))


if __name__ == '__main__':
    main()