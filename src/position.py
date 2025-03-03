from dataclasses import dataclass
from pathlib import Path


@dataclass
class Data:
    frame: int
    x: int
    y: int
    z: int


@dataclass
class Position:
    input: Path  # .txt file
    output: Path  # .midi file

    def get_data(self) -> tuple[Data, ...]:
        with open(input, "r") as f:
            ...
