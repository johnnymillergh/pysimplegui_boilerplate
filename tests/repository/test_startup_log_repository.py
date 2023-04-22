import sys

from loguru import logger

from pysimplegui_boilerplate.repository.model.startup_log import StartupLog
from pysimplegui_boilerplate.repository.startup_log_repository import (
    retain_startup_log,
    save,
    update_latest,
)


def test_save() -> None:
    try:
        saved_startup_log = save(StartupLog(command_line=" ".join(sys.argv)))
    except Exception as ex:
        assert False, f"{save} raised an exception {ex}"
    assert saved_startup_log is not None
    assert saved_startup_log.get_id() > 0
    logger.info(f"Saved startup log, id: {saved_startup_log.get_id()}")


def test_update_latest() -> None:
    try:
        update_latest()
    except Exception as ex:
        logger.warning(f"Failed to update latest startup log. {ex}")


def test_retain_startup_log():
    try:
        retain_startup_log()
    except Exception as ex:
        assert False, f"{retain_startup_log} raised an exception {ex}"
