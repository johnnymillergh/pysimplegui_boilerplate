import PySimpleGUI as sg
from loguru import logger

from pysimplegui_boilerplate.common.common_function import get_module_name


def main() -> None:
    """
    Main function.
    """
    logger.info(f"Current module: {get_module_name()}")

    sg.theme("TanBlue")
    sg.set_options(scaling=2.0)
    layout = [
        [sg.Text("What's your name?")],
        [sg.Input(key="-INPUT-")],
        [sg.Text(size=(40, 1), key="-OUTPUT-TEXT-")],
        [sg.Button("OK"), sg.Button("Quit")],
    ]
    # Create the window
    window = sg.Window("Window Title", layout)

    # Display and interact with the Window using an Event Loop
    while True:
        event, values = window.read()
        # See if the user wants to quit or window was closed
        if event == sg.WINDOW_CLOSED or event == "Quit":
            logger.info("Window closed")
            break
        # Output a message to the window
        window["-OUTPUT-TEXT-"].update(
            f"Hello {values['-INPUT-']}! Thanks for trying PySimpleGUI"
        )

    # Finish up by removing from the screen
    window.close()


if __name__ == "__main__":
    main()
