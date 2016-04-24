import random


def pivot(the_list):
    """Choose pivot of a list, sort and reset pivot."""
    if len(the_list) > 1:
        pivot = 0
        pivot_val = the_list[0]
        left_cursor = pivot + 1
        right_cursor = len(the_list) - 1

        to_shift = True
        while to_shift:
            while left_cursor <= right_cursor and the_list[left_cursor] <= pivot_val:
                left_cursor = left_cursor + 1
            while right_cursor >= left_cursor and the_list[right_cursor] >= pivot_val:
                right_cursor = right_cursor - 1
            if right_cursor < left_cursor:
                to_shift = False
            else:
                temp = the_list[left_cursor]
                the_list[left_cursor] = the_list[right_cursor]
                the_list[right_cursor] = temp

        temp = the_list[0]
        the_list[0] = the_list[right_cursor]
        the_list[right_cursor] = temp

        return right_cursor


def split(the_list):
    """Split a list on pivot."""
    if len(the_list) > 1:
        slipt_point = pivot(the_list)
        left_list = the_list[:slipt_point]
        print("left", left_list)
        right_list = the_list[slipt_point + 1:]
        print("right", right_list)
        the_list = split(left_list) + [the_list[slipt_point]] + split(right_list)
        print("the_list", the_list)
    return the_list


def quicksort(the_list):
    """Split a list and sort."""
    result = split(the_list)
    return result


test_list = [random.randint(1, 100) for i in range(15)]
print(test_list)
result = quicksort(test_list)
print(result)