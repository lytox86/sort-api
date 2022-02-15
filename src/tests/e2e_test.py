from http import HTTPStatus

import requests
from fastapi.testclient import TestClient


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

    def test_sort(self, test_client: TestClient):
        n = 100
        unsorted_array = list(range(n - 1, -1, -1))
        expected_sorted_array = list(range(n))
        input = {"numbers": unsorted_array, "algorythm": "quicksort"}
        response = test_client.post("/api/v1/sort", json=input)
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

    def test_sort_wrong_algorythm(self, test_client: TestClient):
        input = {"numbers": [1, 2, 3, 5], "algorythm": "mergesort"}
        response = test_client.post("/api/v1/sort", json=input)
        assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
        assert response.json() == {
            "detail": [
                {
                    "ctx": {"enum_values": ["quicksort"]},
                    "loc": ["body", "algorythm"],
                    "msg": "value is not a valid enumeration member; permitted: 'quicksort'",
                    "type": "type_error.enum",
                }
            ]
        }

    def test_invalid_call(self, test_client: TestClient):
        input = {"numbers": [1, 2, 3, 5]}
        response = test_client.post("/api/v1/wrong/", json=input)
        assert response.status_code == HTTPStatus.NOT_FOUND
        assert response.json() == {"detail": "Not Found"}

    def test_root(self, test_client: TestClient):
        response = test_client.get("/")
        assert response.status_code == HTTPStatus.OK
        assert response.json() == {"Hello": "World"}
