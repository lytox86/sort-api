from abc import ABC, abstractmethod


class AbstractSort(ABC):
    @abstractmethod
    def sort(self, array: list[int]) -> tuple[list[int], int]:
        """
        :return: tuple of new sorted array and numbers of steps
        """
        pass
