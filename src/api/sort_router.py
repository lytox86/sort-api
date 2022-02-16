from typing import Any

from fastapi import APIRouter, status

from src.models import Input
from src.services import QuickSort

sort_router = APIRouter(prefix="/sort")


@sort_router.post("/quick", status_code=status.HTTP_200_OK)
def quick_sort(input: Input) -> dict[str, Any]:
    sorted_array, steps = QuickSort().sort(input.numbers)
    return {"result": sorted_array, "sortingSteps": steps}
