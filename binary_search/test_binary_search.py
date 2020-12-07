# -*- coding: utf-8 -*-
#
# Author: sisyphuswxg
# Date: 2020-12-7
# Desc: Test Binary Search


from .binary_search import BinarySearch
import json
import pytest


# read data
with open("test_data.json", "r") as file:
    test_data = json.load(file)


class TestBinarySearch:

    def setup_class(self):
        # initial
        self.bs = BinarySearch()

    @pytest.mark.parametrize("search_list, item, expected_index",
                             [(test_data["list_with_10_items"], 9, 1),
                              (test_data["list_with_10_items"], 100, None),
                              (test_data["list_with_100_items"], 193, 2),
                              (test_data["list_with_100_items"], 155, None),
                              (test_data["list_with_1000_items"], 15, 1),
                              (test_data["list_with_1000_items"], 5, None),
                              ])
    def test_iterative_binary_search(self, search_list, item, expected_index):
        index = self.bs.binary_search_iterative(search_list, item)
        assert expected_index == index, "case failed"

    @pytest.mark.parametrize("search_list, item, expected_index",
                             [(test_data["list_with_10_items"], 9, 1),
                              (test_data["list_with_10_items"], 100, None),
                              (test_data["list_with_100_items"], 193, 2),
                              (test_data["list_with_100_items"], 155, None),
                              (test_data["list_with_1000_items"], 15, 1),
                              (test_data["list_with_1000_items"], 5, None),
                              ])
    def test_recursive_binary_search(self, search_list, item, expected_index):
        low, high = 0, len(search_list)-1
        index = self.bs.binary_search_recursive(search_list, low, high, item)
        assert expected_index == index, "case failed"
