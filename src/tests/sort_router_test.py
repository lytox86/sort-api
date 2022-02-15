from unittest.mock import patch

import pytest
from pydantic.error_wrappers import ValidationError

from src.models.models import SortAlgorythm, InputAndAlgorythm, Input
from src.services.sort_service import SortService
from src.api.sort_router import quick_sort, sort


class TestSortRouter:
    def test_quick_sort_algorithm(self):
        mocked_sort_result = [1], 1
        expected_result = {"result": [1], "sortingSteps": 1}
        with patch.object(SortService, "sort", return_value=mocked_sort_result) as mock:
            json_response = quick_sort(Input(numbers=[1]))
        assert json_response == expected_result
        mock.assert_called_once_with([1], SortAlgorythm.QUICKSORT)

    def test_sort_known_algorithm(self):
        mocked_sort_result = [1], 1
        expected_result = {"result": [1], "sortingSteps": 1}
        with patch.object(SortService, "sort", return_value=mocked_sort_result) as mock:
            json_response = sort(
                InputAndAlgorythm(numbers=[1], algorythm=SortAlgorythm.QUICKSORT)
            )
        assert json_response == expected_result
        mock.assert_called_once_with([1], SortAlgorythm.QUICKSORT)

    def test_sort_unknown_algorythm(self):
        mocked_sort_result = [1], 1
        with patch.object(SortService, "sort", return_value=mocked_sort_result) as mock:
            with pytest.raises(ValidationError):
                _ = sort(InputAndAlgorythm(numbers=[1], algorythm="bubblesort"))
        mock.assert_not_called()
