# 1. CLI args:
# - orientation input txt file
# - position input txt file
# - framerate


import argparse
from pathlib import Path

from orientation import Orientation
from position import Position

# import numpy as np


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-o",
        "--orientation",
        help=".txt file from Adobe After Effects containing orientation data",
        type=str,
        required=True,
    )
    parser.add_argument(
        "-p",
        "--position",
        help=".txt file from Adobe After Effects containing postion data",
        type=str,
        required=True,
    )

    args = parser.parse_args()

    o_path = Path(args.orientation).resolve(strict=True)
    p_path = Path(args.position).resolve(strict=True)

    if o_path.suffix != ".txt":
        raise Exception(f"{o_path.as_posix()} is not a .txt file!")

    if p_path.suffix != ".txt":
        raise Exception(f"{o_path.as_posix()} is not a .txt file!")

    o = Orientation(o_path)
    p = Position(p_path)

    # print(o.input_txt.as_posix())
    # print(p.input_txt.as_posix())


if __name__ == "__main__":
    main()
