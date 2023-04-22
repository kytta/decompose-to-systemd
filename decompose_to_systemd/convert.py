import argparse
import shutil
from pathlib import Path

import podman_compose
from jinja2 import Environment
from jinja2 import PackageLoader
from jinja2 import select_autoescape
from podman_compose import Podman
from podman_compose import PodmanCompose
from podman_compose import container_to_args

jinja_env = Environment(
    loader=PackageLoader("decompose_to_systemd"),
    autoescape=select_autoescape(),
)


def convert(file: Path, frontend: str) -> None:
    frontend_path = shutil.which(frontend)

    cwd = Path.cwd()

    podman_compose.assert_cnt_nets = lambda _a, _b: None

    compose = PodmanCompose()
    compose.podman = Podman(compose, dry_run=True)

    global_args = argparse.Namespace()
    global_args.podman_args = []
    global_args.project_name = cwd.name
    global_args.file = [str(file)]
    global_args.dirname = str(cwd)
    global_args.env_file = ".env"
    global_args.in_pod = False
    compose.global_args = global_args

    compose._parse_compose_file()  # noqa: SLF001
    containers = compose.containers

    template = jinja_env.get_template("template.service.jinja")
    for container in containers:
        Path(container["name"]).with_suffix(".service").write_text(
            template.render(
                project_name=cwd.name,
                service_name=container["service_name"],
                container_name=container["name"],
                image=container["image"] if "build" not in container else None,
                frontend_path=frontend_path,
                args=container_to_args(compose, container, detached=False),
            ),
        )
