from dataclasses import dataclass
from pathlib import Path

from .aftereffects import AfterEffectsFile


@dataclass
class Data:
    frame: int
    x: int


@dataclass
class Orientation(AfterEffectsFile):
    input: Path  # .txt file
    output: Path  # .midi file

    def get_data(self) -> tuple[Data, ...]:
        with open(input, "r") as f:
            ...
