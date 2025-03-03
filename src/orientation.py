from dataclasses import dataclass
from pathlib import Path

from aftereffects import AfterEffectsFile


@dataclass
class Data:
    frame: int
    x: int


class Orientation(AfterEffectsFile):
    def __init__(self, input_txt: Path):
        super().__init__(input_txt=input_txt)

    # TODO:
    def get_data(self) -> tuple[Data, ...]:
        ...
        # with open(self.input_txt, "r") as f:
        #     lines: list[str] = [line.strip().split() for line in f.readlines()]


# with open(input_file, "r") as file:
#     lines = file.readlines()
#
# # Parse the lines, skipping headers
# for line in lines:
#     parts = line.strip().split()
#     if len(parts) == 4 and parts[0].isdigit():
#         frame = int(parts[0])
#         x, y, z = map(float, parts[1:])
#         frames.append(frame)
#         x_degrees.append(x)
#         y_degrees.append(y)
#         z_degrees.append(z)
