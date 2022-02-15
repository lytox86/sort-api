from typing import Any

from fastapi import APIRouter, status, HTTPException

from src.models.models import Input, SortAlgorythm, InputAndAlgorythm
from src.services.sort_service import SortService

sort_router = APIRouter(prefix="/sort")


@sort_router.post("/quick", status_code=status.HTTP_200_OK)
def quick_sort(input: Input) -> dict[str, Any]:
    return _sort(input.numbers, SortAlgorythm.QUICKSORT)


@sort_router.post("", status_code=status.HTTP_200_OK)
def sort(inp: InputAndAlgorythm) -> dict[str, Any]:
    return _sort(inp.numbers, inp.algorythm)


def _sort(numbers: list[int], sort_algorythm: SortAlgorythm) -> dict[str, Any]:
    try:
        sorted_array, steps = SortService.sort(numbers, sort_algorythm)
    except NotImplementedError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="algorythm not implemented"
        )
    return {"result": sorted_array, "sortingSteps": steps}
