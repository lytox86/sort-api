from typing import Optional

from src.models.models import SortAlgorythm
from src.services.algorithms.abstract_sort import AbstractSort
from src.services.algorithms.quick_sort import QuickSort

algorythm_map: dict[SortAlgorythm, AbstractSort] = {
    SortAlgorythm.QUICKSORT: QuickSort()
}


class SortAlgorythmFactory:
    @staticmethod
    def get_algorythm(sort_algorythm: SortAlgorythm) -> Optional[AbstractSort]:
        return algorythm_map.get(sort_algorythm)
