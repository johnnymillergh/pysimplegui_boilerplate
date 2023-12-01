from importlib import metadata as importlib_metadata
from pathlib import Path

from loguru import logger


def calc_container(path: Path) -> int:
    total_size = 0
    for item in Path(path).rglob("*"):
        if item.is_file():
            total_size += item.stat().st_size
    return total_size


def list_python_dependencies() -> None:
    distributions = list(importlib_metadata.distributions())
    logger.info(f"Size of dists: {len(distributions)}")
    for dist in distributions:
        try:
            # noinspection PyUnresolvedReferences,PyProtectedMember
            path = Path(dist._path.parent, dist.metadata["name"])  # type: ignore
            size = calc_container(path)
            if size / 1000 > 1.0:
                logger.info(f"{dist.metadata['name']}: {size / 1000} KB")
                logger.info("-" * 40)
        except OSError as e:
            logger.error(f"{dist.metadata['name']} no longer exists", e)


if __name__ == "__main__":
    list_python_dependencies()
