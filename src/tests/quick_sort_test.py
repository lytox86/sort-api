from random import randint
from unittest.mock import ANY
from src.services import QuickSort


class TestQuickSort:
    def test_sort_base_case(self):
        assert QuickSort().sort([]) == ([], 0)
        assert QuickSort().sort([1]) == ([1], 0)

    def test_sort_already_sorted(self):
        sorted_array = list(range(5))
        assert QuickSort().sort(sorted_array) == (sorted_array, 3)

    def test_sort_worst_case(self):
        n = 5
        reversed_sorted_array = list(range(n - 1, -1, -1))
        expected_sorted_array = list(range(n))
        assert QuickSort().sort(reversed_sorted_array) == (expected_sorted_array, 3)

    def test_sort_random(self):
        n = 1000
        random_array = [randint(-100, 100) for _ in range(n)]
        expected_sorted_array = sorted(random_array)
        response = QuickSort().sort(random_array)
        assert response == (expected_sorted_array, ANY)
        steps = response[1]
        # log_2_n = n.bit_length()-1
        assert 1 <= steps <= n
