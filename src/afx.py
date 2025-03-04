import textwrap
from dataclasses import dataclass
from pathlib import Path
from typing import override

import numpy as np


@dataclass
class FrameData:
    frame: int
    x: float
    y: float
    z: float


class AfterEffectsData:
    def __init__(self, txt: Path):
        self.txt: Path = txt

    def get_framerate(self) -> int:
        """Reads the input .txt file and returns the framerate."""
        with open(self.txt, "r") as f:
            line = f.readlines()[2].strip().split()
            try:
                framerate: int = int(line[3])
            # TODO: What errors would this potentially raise?
            except Exception as error:
                raise error
            return framerate

    def get_frames(self) -> tuple[FrameData, ...]:
        """For each frame, returns a FrameData object."""
        data: list[FrameData] = []

        with open(self.txt, "r") as f:
            for line in f.readlines():
                if line.strip() == "":
                    continue
                if not line.strip()[0].isdigit():
                    continue

                # FIXME: This is failing silently. Fine for now but needs improvement.
                parts: list[str] = line.split()
                if len(parts) != 4:
                    continue

                try:
                    d = FrameData(
                        frame=int(parts[0].strip()),
                        x=float(parts[1].strip()),
                        y=float(parts[2].strip()),
                        z=float(parts[3].strip()),
                    )
                # FIXME: More specific Exceptions.
                except Exception as error:
                    raise error
                else:
                    data.append(d)

        return tuple(data)

    def get_degrees(self):
        frames = self.get_frames()
        x = np.degrees(np.unwrap(np.radians([frame.x for frame in frames])))
        y = np.degrees(np.unwrap(np.radians([frame.y for frame in frames])))
        z = np.degrees(np.unwrap(np.radians([frame.z for frame in frames])))
        return x, y, z

    @override
    def __repr__(self) -> str:
        return f"AfterEffectsData(txt={self.txt})"

    @override
    def __str__(self) -> str:
        output: str = ""
        for frame in self.get_frames():
            frame = f"""
                Frame #{frame.frame}:
                    X: {frame.x}
                    Y: {frame.y}
                    Z: {frame.z}
            """
            output += frame
        return textwrap.dedent(output)
