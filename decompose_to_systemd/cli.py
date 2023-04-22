# SPDX-FileCopyrightText: © 2023 Nikita Karamov <me@kytta.dev>
#
# SPDX-License-Identifier: BSD-2-Clause

import argparse
from pathlib import Path


def _get_parser() -> argparse.ArgumentParser:
    """Return an argument parser to set the script's parameters.

    :return: a populated parser
    """
    from importlib.metadata import version

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--version",
        "-V",
        action="version",
        version=version("decompose_to_systemd"),
    )

    parser.add_argument(
        "--frontend",
        "-f",
        default="podman",
        type=str,
        choices=["docker", "podman"],
        help="frontend which will be used to run the containers",
    )

    parser.add_argument(
        "files",
        nargs="+",
        type=Path,
        help="files to convert. Must adhere to the Compose spec.",
        metavar="FILE",
    )

    return parser
