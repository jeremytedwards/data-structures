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
            print(item)
            # import pdb;pdb.set_trace()
            for index, v in enumerate(sorted_list):
                if v >= item:
                    sorted_list.insert(index, item)
                    break
                else:
                    sorted_list.append(item)
                    break
        return sorted_list


def main():
    random_list = [random.randint(25, 100) for i in range(15)]
    print(random_list)
    result = sort_insertion(random_list)
    print("Insertion sort on random list:\n", result)
    # ordered_list = []
    # sort_insertion(ordered_list)
    # print
    # reversed_list = []
    # sort_insertion(reversed_list)
    # print


if __name__ == '__main__':
    main()
