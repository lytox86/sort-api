from unittest.mock import patch

import pytest

from src.models.models import SortAlgorythm
from src.services.algorithms.quick_sort import QuickSort
from src.services.sort_service import SortService


class TestSearchService:
    def test_known_algorithm(self):
        expected_value = [1], 1
        with patch.object(QuickSort, "sort", return_value=expected_value) as mock:
            response = SortService.sort([1], SortAlgorythm.QUICKSORT)
        assert response == expected_value
        mock.assert_called_once_with([1])

    def test_unknown_algorythm(self):
        with patch.object(QuickSort, "sort", return_value=([1], 1)) as mock:
            with pytest.raises(NotImplementedError):
                _ = SortService.sort([1], "insertion_sort")  # type: ignore
        mock.assert_not_called()
