import textwrap
from dataclasses import dataclass
from pathlib import Path
from typing import override


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
            try:
                line: list[str] = f.readline(2).strip().split()
            # TODO: What errors would this potentially raise?
            except Exception as error:
                raise error

            try:
                framerate: int = int(line[3])
            # TODO: What errors would this potentially raise?
            except Exception as error:
                raise error
            return framerate

    def get_frames(self) -> tuple[FrameData, ...]:
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
