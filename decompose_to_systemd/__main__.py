# SPDX-FileCopyrightText: © 2023 Nikita Karamov <me@kytta.dev>
#
# SPDX-License-Identifier: BSD-2-Clause

from collections.abc import Sequence

from decompose_to_systemd.cli import _get_parser
from decompose_to_systemd.convert import convert


def _main(argv: Sequence[str] | None = None) -> None:
    parser = _get_parser()
    args = parser.parse_args(argv)

    for file in args.files:
        convert(file, args.frontend)


if __name__ == "__main__":
    _main()
