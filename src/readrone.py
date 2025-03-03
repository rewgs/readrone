# 1. CLI args:
# - orientation input txt file
# - position input txt file
# - framerate


import argparse
from pathlib import Path

from aftereffects import AfterEffectsData

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

    o = Path(args.orientation).resolve(strict=True)
    p = Path(args.position).resolve(strict=True)

    if o.suffix != ".txt":
        raise Exception(f"{o.as_posix()} is not a .txt file!")

    if p.suffix != ".txt":
        raise Exception(f"{o.as_posix()} is not a .txt file!")

    orientation = AfterEffectsData(o)
    position = AfterEffectsData(p)

    print(orientation)
    print(position)


if __name__ == "__main__":
    main()
