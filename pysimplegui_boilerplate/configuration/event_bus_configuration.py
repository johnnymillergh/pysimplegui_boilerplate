from event_bus import EventBus
from loguru import logger

event_bus = EventBus()


def configure() -> None:
    """
    Configure event bus.
    """
    logger.warning(f"Initialized event bus: {event_bus}")
