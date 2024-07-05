import pytest
from jedi.plugins import pytest
from demo.binary_search import binary_search

def test_list_1():
    test_list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    assert binary_search(test_list_1,7) == 6
    assert binary_search(test_list_1,1) == 0
    assert binary_search(test_list_1,10) == 9
    assert binary_search(test_list_1,11) == -1

def test_list_2():
    test_list_2 = [-8,-6,-1,3,1000]

    assert binary_search(test_list_2, -6) == 1
    assert binary_search(test_list_2, -8) == 0
    assert binary_search(test_list_2,1000) == 4
    assert binary_search(test_list_2,0) == -1

def test_list_3():
    test_list_3 = []

    assert binary_search(test_list_3,11) == -1

def test_list_4():
    test_list_4 = [i for i in range(1000)]

    assert binary_search(test_list_4,7) == 7
    assert binary_search(test_list_4,0) == 0
    assert binary_search(test_list_4,999) == 999
    assert binary_search(test_list_4,-999) == -1
import pytest
@pytest.mark.parametrize("test_list, target, expected", [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 7, 6),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1, 0),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 9),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11, -1),
    ([-8, -6, -1, 3, 1000], -6, 1),
    ([-8, -6, -1, 3, 1000], -8, 0),
    ([-8, -6, -1, 3, 1000], 1000, 4),
    ([-8, -6, -1, 3, 1000], 0, -1),
    ([], 11, -1),
    ([i for i in range(1000)], 7, 7),
    ([i for i in range(1000)], 0, 0),
    ([i for i in range(1000)], 999, 999),
    ([i for i in range(1000)], -999, -1)
])
def test_binary_search(test_list, target, expected):
    assert binary_search(test_list, target) == expected