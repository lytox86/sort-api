from .algorithms.factory import SortAlgorythmFactory
from ..models import SortAlgorythm


class SortService:
    @staticmethod
    def sort(
        numbers: list[int], sort_algorythm: SortAlgorythm
    ) -> tuple[list[int], int]:
        if algorythm := SortAlgorythmFactory.get_algorythm(sort_algorythm):
            return algorythm.sort(numbers)
        raise NotImplementedError()
