# 1. CLI args:
# - framerate


import argparse
from pathlib import Path

from aftereffects import AfterEffectsData

# import numpy as np


def __check_path(p: str) -> Path:
    path = Path(p)
    if path.suffix != ".txt":
        raise Exception(f"{p} is not a .txt file!")
    try:
        resolved = path.resolve(strict=True)
    except FileNotFoundError as error:
        raise error
    else:
        return resolved


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-o",
        "--orientation-file",
        help=".txt file from Adobe After Effects containing orientation data",
        type=str,
        required=True,
        dest="orientation",
    )
    parser.add_argument(
        "-p",
        "--position-file",
        help=".txt file from Adobe After Effects containing postion data",
        type=str,
        required=True,
        dest="position",
    )

    args = parser.parse_args()

    o = AfterEffectsData(__check_path(args.orientation))
    p = AfterEffectsData(__check_path(args.position))

    # print(o)
    # print(p)
    print(o.get_framerate())
    print(p.get_framerate())


if __name__ == "__main__":
    main()
