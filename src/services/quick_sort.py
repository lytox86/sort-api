from copy import copy


class QuickSort:
    _steps: int
    _array: list[int]
    _depth: int

    def sort(self, array: list[int]) -> tuple[list[int], int]:
        """
        sorts array using quicksort
        a new array is returned, the parameter array is not modified
        :return: tuple of new sorted array and numbers of steps
        """
        self._steps = 0
        self._depth = 0
        self._array = copy(array)
        if len(self._array) <= 1:
            return self._array, self._steps
        # TODO shuffle input to reduce performance dependance on input?
        self._recursive_sort(0, len(self._array) - 1, 1)
        return self._array, self._steps

    def _recursive_sort(self, low: int, high: int, depth: int) -> None:
        """
        recursively sorts self._array in place from indices [low..hi], both inclusively
        """
        if low < high:
            self._depth = depth
            self._steps += 1

            pivot_index = self._partition(low, high)

            self._recursive_sort(low, pivot_index - 1, depth + 1)
            self._recursive_sort(pivot_index + 1, high, depth + 1)

    def _partition(self, low: int, high: int) -> int:
        """
        partitions self._array from [low..hi] and returns pivot index
        self._array[low..pivot_index-1] <= self._array[pivot_index]  <= self._array[pivot_index+1..high]
        """
        original_low = low
        pivot_index = (low + high) // 2
        pivot = self._array[pivot_index]
        self._swap(low, pivot_index)
        low += 1

        while low <= high:
            while low <= high and self._array[low] <= pivot:
                low += 1
            while low <= high and self._array[high] >= pivot:
                high -= 1
            if low < high:
                assert self._array[low] > self._array[high]
                self._swap(low, high)
                low += 1
                high -= 1

        assert low == high + 1
        pivot_index = high
        self._swap(original_low, pivot_index)

        return pivot_index

    def _swap(self, i: int, j: int) -> None:
        self._array[i], self._array[j] = self._array[j], self._array[i]


if __name__ == "__main__":
    sort = QuickSort()
    print(sort.sort([1, 2, 3, 4, 5]))
