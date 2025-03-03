from abc import ABC, abstractmethod
from pathlib import Path


class AfterEffectsFile(ABC):
    def __init__(self, input_txt: Path):
        self.input_txt: Path = input_txt

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

    # TODO:
    # def output_midi(self) -> Path:
    #     """Exports a MIDI file of the data."""

    @abstractmethod
    def get_data(self) -> tuple[object, ...]:
        """Returns a tuple of orientation.Data or position.Data objects."""
