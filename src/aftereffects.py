from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path


@dataclass
class AfterEffectsFile(ABC):
    input_txt: Path
    output_midi: Path

    def get_framerate(self) -> int:
        """Reads the input .txt file and returns the framerate."""
        with open(self.input_txt, "r") as f:
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

    @abstractmethod
    def get_data(self) -> tuple[object, ...]: ...
