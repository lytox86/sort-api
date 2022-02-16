from unittest.mock import patch

import pytest
from pydantic.error_wrappers import ValidationError

from src.models.models import Input
from src.services import QuickSort
from src.api.sort_router import quick_sort


class TestSortRouter:
    def test_quick_sort(self):
        mocked_sort_result = [1], 1
        expected_result = {"result": [1], "sortingSteps": 1}
        with patch.object(QuickSort, "sort", return_value=mocked_sort_result) as mock:
            json_response = quick_sort(Input(numbers=[1]))
        assert json_response == expected_result
        mock.assert_called_once_with([1])
