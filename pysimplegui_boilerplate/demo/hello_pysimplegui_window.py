from datetime import datetime

import PySimpleGUI as sg
from loguru import logger
from PySimpleGUI import Window

from pysimplegui_boilerplate.configuration.event_bus_configuration import event_bus


def show():
    sg.theme("PythonPlus")
    # Inject the layout to the window
    window = sg.Window("Window Title", layout(datetime.now()))
    # Display and interact with the Window using an Event Loop
    while True:
        event, values = window.read()
        # See if the user wants to quit or window was closed
        if event == sg.WINDOW_CLOSED or event == "Quit":
            logger.info("Window closed")
            break
        event_bus.emit(event, values, window)
    # Finish up by removing from the screen
    window.close()


def layout(date: datetime):
    return [
        [sg.Text(f"What's your name? {date}")],
        [sg.Input(key="-INPUT-")],
        [sg.Text(size=(40, 1), key="-OUTPUT-TEXT-")],
        [sg.Button("OK"), sg.Button("Quit")],
    ]


@event_bus.on("OK")
def on_ok_event(values: dict, window: Window):
    logger.info(f"On OK event: {values}")
    # Output a message to the window
    window["-OUTPUT-TEXT-"].update(
        f"Hello {values['-INPUT-']}! Thanks for trying PySimpleGUI"
    )
