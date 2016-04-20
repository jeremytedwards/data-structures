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
            for i in range(len(sorted_list)):
                if sorted_list[i] >= item:
                    sorted_list.insert(i, item)
                    break
                elif sorted_list[-1] < item:
                    sorted_list.append(item)
                    break
        return sorted_list


def main():
    random_list = [random.randint(25, 100) for i in range(10)]
    result_1 = sort_insertion(random_list)
    time = timeit.timeit('random_list', sort_insertion(random_list), 1000000)
    print("Insertion sort on random list:", result_1, time)
    # ordered_list = [for i in rang(10)]
    # result_2 = sort_insertion(ordered_list)
    # print("Insertion sort on ordered list:", result_2)
    # reversed_list = [for i in range(10)]
    # result_3 = sort_insertion(reversed_list)
    # print("Insertion sort on reversed list:", result_3)


if __name__ == '__main__':
    main()
