from typing import Any

import PySimpleGUI as sg
from loguru import logger

from pysimplegui_boilerplate.configuration.event_bus_configuration import event_bus
from pysimplegui_boilerplate.layout.hello_pysimplegui.view import create_window
from pysimplegui_boilerplate.layout.view_video_game.controller import (
    main as view_video_game_main,
)

current_window: sg.Window


def main() -> None:
    # Inject the layout to the window
    global current_window
    current_window = create_window()
    # Display and interact with the Window using an Event Loop
    while True:
        event, values = current_window.read()
        # See if the user wants to quit or window was closed
        if event == sg.WINDOW_CLOSED or event == "Exit":
            logger.info("Window closed")
            break
        logger.debug(
            f"Emitting event: {event}, values: {values}, window: {current_window}"
        )
        event_bus.emit(event, values, current_window)
    # Finish up by removing from the screen
    current_window.close()


@event_bus.on("Submit")
def on_submit_event(values: dict[str, Any], window: sg.Window) -> None:
    logger.info(f"On Submit event, got values: {values}, window: {window}")
    # Output a message to the window
    window["-OUTPUT-TEXT-"].update(
        f"Hello {values['-INPUT-']}! Thanks for trying PySimpleGUI"
    )
    sg.popup_notify(f"On Submit event, got values: {values}", title="Hello PySimpleGUI")


@event_bus.on("View Video Games")
def on_view_video_games(_: dict[str, Any], __: sg.Window) -> None:
    view_video_game_main()


@event_bus.on("-VIDEO-GAME-TABLE-")
def on_view_video_table(values: dict[str, Any], __: sg.Window) -> None:
    global current_window
    current_window["-INPUT-"].update(f"Got values from Video Game Table: {values}")
