import PySimpleGUI as sg

from pysimplegui_boilerplate.common.common_function import get_resources_dir


def create_window() -> sg.Window:
    return sg.Window(
        "Window Title",
        [
            [
                sg.Image(
                    filename=str(
                        get_resources_dir() / "picture/PySimpleGUI Boilerplate.png"
                    )
                )
            ]
        ],
        transparent_color=sg.theme_background_color(),
        no_titlebar=True,
        keep_on_top=True,
    )
