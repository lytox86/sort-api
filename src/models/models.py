from pydantic import BaseModel


class Input(BaseModel):  # pytype: disable=base-class-error
    numbers: list[int]
