from dataclasses import dataclass
from pathlib import Path

from aftereffects import AfterEffectsFile


@dataclass
class Data:
    frame: int
    x: int
    y: int
    z: int


class Position(AfterEffectsFile):
    def __init__(self, input_txt: Path):
        super().__init__(input_txt=input_txt)

    # TODO:
    def get_data(self) -> tuple[Data, ...]:
        with open(input, "r") as f:
            ...
