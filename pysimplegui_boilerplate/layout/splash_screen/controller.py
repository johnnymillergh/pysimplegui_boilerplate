from pysimplegui_boilerplate.configuration.event_bus_configuration import event_bus
from pysimplegui_boilerplate.layout.hello_pysimplegui.controller import (
    main as hello_pysimplegui_main,
)
from pysimplegui_boilerplate.layout.splash_screen.view import create_window

DISPLAY_TIME_MILLISECONDS = 5000


def main() -> None:
    create_window().read(timeout=DISPLAY_TIME_MILLISECONDS, close=True)
    event_bus.emit("splash_screen_dismissed")


@event_bus.on("splash_screen_dismissed")
def on_splash_screen_dismissed() -> None:
    hello_pysimplegui_main()
