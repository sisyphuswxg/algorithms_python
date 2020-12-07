# -*- coding: utf-8 -*-
#
# Author: sisyphuswxg
# Date: 2020-12-8
# Desc: Selection Sort


class SelectionSort:

    def find_smallest(self, arr):
        smallest = arr[0]
        smallest_index = 0
        for i in range(1, len(arr)):
            if arr[i] < smallest:
                smallest_index = i
        return smallest_index

    def selection_sort(self, arr):
        new_arr = []
        for i in range(len(arr)):
            smallest_index = self.find_smallest(arr)
            new_arr.append(arr.pop(smallest_index))
        return new_arr


if __name__ == "__main__":
    my_list = [5, 3, 6, 3, 3, 38, 99, 2, 10, 7, 53, 532]

    ss = SelectionSort()
    print(ss.selection_sort(my_list))
