# -*- coding: utf-8 -*-
#
# Author: sisyphuswxg
# Date: 2020-12-7
# Desc: Binary Search


class BinarySearch:

    def binary_search_iterative(self, list, item):
        low = 0
        high = len(list) - 1

        while low <= high:
            mid = (low + high) // 2
            mid_value = list[mid]
            if item == mid_value:
                return mid
            elif item > mid_value:
                low = mid + 1
            else:
                high = mid - 1
        return None

    def binary_search_recursive(self, list, low, high, item):

        if low <= high:
            mid = (low + high) // 2
            mid_value = list[mid]
            if item == mid_value:
                return mid
            elif item > mid_value:
                return self.binary_search_recursive(list, mid+1, high, item)
            else:
                return self.binary_search_recursive(list, low, mid-1, item)
        return None


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    bs = BinarySearch()
    # test iterative
    print(bs.binary_search_iterative(my_list, 10))
    print(bs.binary_search_iterative(my_list, 3))
    print(bs.binary_search_iterative(my_list, -1))

    # test recurtive
    low, high = 0, len(my_list)-1
    print(bs.binary_search_recursive(my_list, low, high, 10))
    print(bs.binary_search_recursive(my_list, low, high, 3))
    print(bs.binary_search_recursive(my_list, low, high, -1))



