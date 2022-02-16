from http import HTTPStatus
from unittest.mock import patch

import pytest
import requests
from fastapi.testclient import TestClient

from src.services import QuickSort


class TestEnd2End:
    def test_quick_sort(self, test_client: TestClient):
        n = 100
        unsorted_array = list(range(n - 1, -1, -1))
        expected_sorted_array = list(range(n))
        input = {"numbers": unsorted_array}
        response: requests.Response = test_client.post("/api/v1/sort/quick", json=input)
        assert response.status_code == HTTPStatus.OK
        assert response.json()["result"] == expected_sorted_array
        assert response.json()["sortingSteps"] == 73

    def test_quick_sort_invalid_ints(self, test_client: TestClient):
        input = {"numbers": ["A"]}
        response: requests.Response = test_client.post("/api/v1/sort/quick", json=input)
        assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
        assert response.json() == {
            "detail": [
                {
                    "loc": ["body", "numbers", 0],
                    "msg": "value is not a valid integer",
                    "type": "type_error.integer",
                }
            ]
        }

    def test_quick_sort_exception(self, test_client: TestClient):
        n = 100
        unsorted_array = list(range(n - 1, -1, -1))
        input = {"numbers": unsorted_array}
        with patch.object(QuickSort, "sort", side_effect=IndexError()):
            with pytest.raises(IndexError):
                response: requests.Response = test_client.post(
                    "/api/v1/sort/quick", json=input
                )

    def test_invalid_call(self, test_client: TestClient):
        input = {"numbers": [1, 2, 3, 5]}
        response = test_client.post("/api/v1/wrong/", json=input)
        assert response.status_code == HTTPStatus.NOT_FOUND
        assert response.json() == {"detail": "Not Found"}

    def test_root(self, test_client: TestClient):
        response = test_client.get("/")
        assert response.status_code == HTTPStatus.OK
        assert response.json() == {"Hello": "World"}
