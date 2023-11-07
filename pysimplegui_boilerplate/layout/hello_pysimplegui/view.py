from datetime import datetime

import PySimpleGUI as sg


def create_window() -> sg.Window:
    return sg.Window(
        "Hello PySimpleGUI",
        [
            [
                sg.Menu(
                    [
                        ["File", ["View Video Games", "Exit"]],
                        ["Edit", ["Edit Me"]],
                        ["Help", ["About"]],
                    ],
                    k="-MENUBAR-",
                    p=0,
                )
            ],
            [sg.Text(f"What's your name? {datetime.now()}")],
            [sg.Input(key="-INPUT-")],
            [sg.Text(size=(40, 1), key="-OUTPUT-TEXT-")],
            [sg.Submit(), sg.Exit()],
        ],
    )
