<!--
SPDX-FileCopyrightText: © 2023 Nikita Karamov <me@kytta.dev>

SPDX-License-Identifier: BSD-2-Clause
-->

# decompose-to-systemd

> Create [systemd service] definitions from [Compose] files

This script reads a `compose.yaml` (or any other Compose file) and outputs
a directory with systemd `.service` files. It uses the parameters from
the Compose file to set the arguments to `podman run` (or `docker run`) for
the `ExecStart` option. It also populates the `After` option for the dependents.
You can create your own service templates with Jinja.

This script allows you to supervise Docker containers with systemd, possibly in
environments without support for Compose (take older Docker versions or Podman).
It is specifically designed for [CoreOS].

## Install

_TBA_

## Usage

_TBA_

## Credits

I got the idea for this project when I was digging around
[Andrey Sitnik's home server config][ai/susedko]. He uses `.service.yml` files
to build systemd service files. I have decided to build a tool that works with
existing Compose files to ease migration from existing configs.

## Licence

© 2023 [Nikita Karamov]\
Licensed under the [BSD 2-Clause "Simplified" License][BSD-2-Clause].

---

This project is hosted on GitHub:
<https://github.com/kytta/figue.git>

[ai/susedko]: https://github.com/ai/susedko
[BSD-2-Clause]: https://spdx.org/licenses/BSD-2-Clause.html
[Compose]: https://compose-spec.io/
[CoreOS]: https://fedoraproject.org/coreos/
[nikita karamov]: https://www.kytta.dev/
[systemd service]: https://www.freedesktop.org/software/systemd/man/systemd.service.html
