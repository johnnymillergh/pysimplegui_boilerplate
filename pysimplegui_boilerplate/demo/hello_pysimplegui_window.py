from datetime import datetime
from typing import Any

import PySimpleGUI as sg
from loguru import logger
from plyer import notification
from PySimpleGUI import Element, Window

from pysimplegui_boilerplate.__main__ import startup
from pysimplegui_boilerplate.configuration.event_bus_configuration import event_bus

# https://www.pysimplegui.org/en/latest/


def main() -> None:
    sg.theme("PythonPlus")
    # Inject the layout to the window
    window = sg.Window("Window Title", layout(datetime.now()))
    # Display and interact with the Window using an Event Loop
    while True:
        event, values = window.read()
        # See if the user wants to quit or window was closed
        if event == sg.WINDOW_CLOSED or event == "Exit":
            logger.info("Window closed")
            break
        logger.debug(f"Emitting event: {event}, values: {values}, window: {window}")
        event_bus.emit(event, values, window)
    # Finish up by removing from the screen
    window.close()


def layout(date: datetime) -> list[list[Element]]:
    return [
        [sg.Text(f"What's your name? {date}")],
        [sg.Input(key="-INPUT-")],
        [sg.Text(size=(40, 1), key="-OUTPUT-TEXT-")],
        [sg.Submit(), sg.Exit()],
    ]


@event_bus.on("Submit")
def on_submit_event(values: dict[str, Any], window: Window) -> None:
    logger.info(f"On Submit event, got values: {values}, window: {window}")
    # Output a message to the window
    window["-OUTPUT-TEXT-"].update(
        f"Hello {values['-INPUT-']}! Thanks for trying PySimpleGUI"
    )
    notification.notify(
        title="Hello PySimpleGUI",
        message=f"On Submit event: {values['-INPUT-']}! Thanks for trying PySimpleGUI",
    )


if __name__ == "__main__":
    startup()
    main()
    # PySimpleGUI.main()
