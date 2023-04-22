"""Create systemd service definitions from Compose files.

This script converts ``compose.yaml`` (or any other Compose files)
to systemd ``.service`` files. The parameters from the Compose file
define the arguments to ``podman run`` (or ``docker run``)
for the ``ExecStart`` option. It also populates the ``After`` option
according to the dependencies (``needs``).

You can run this as script::

    python3 -m decompose_to_systemd compose.yaml

or via the Python API.

SPDX-FileCopyrightText: © 2023 Nikita Karamov <me@kytta.dev>
SPDX-License-Identifier: BSD-2-Clause
"""
