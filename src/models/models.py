from enum import Enum

from pydantic import BaseModel


class SortAlgorythm(Enum):
    QUICKSORT = "quicksort"


class Input(BaseModel):  # pytype: disable=base-class-error
    numbers: list[int]


class InputAndAlgorythm(Input):
    algorythm: SortAlgorythm
