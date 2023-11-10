from typing import Any

import PySimpleGUI as sg


def create_window(values: list[list[Any]]) -> sg.Window:
    layout = [
        [
            sg.Table(
                values=values,
                headings=[
                    "Title",
                    "Features.Handheld?",
                    "Features.Max Players",
                    "Features.Multiplatform?",
                    "Features.Online?",
                    "Metadata.Genres",
                    "Metadata.Licensed?",
                    "Metadata.Publishers",
                    "Metadata.Sequel?",
                    "Metrics.Review Score",
                    "Metrics.Sales",
                    "Metrics.Used Price",
                    "Release.Console",
                    "Release.Rating",
                    "Release.Re-release?",
                    "Release.Year",
                ],
                max_col_width=25,
                auto_size_columns=False,
                display_row_numbers=True,
                justification="center",
                num_rows=20,
                alternating_row_color="lightblue",
                key="-VIDEO-GAME-TABLE-",
                selected_row_colors="red on yellow",
                enable_events=True,
                expand_x=False,
                expand_y=True,
                vertical_scroll_only=False,
                # enable_click_events = True to enable header and other clicks
                enable_click_events=False,
                tooltip="This is a table",
            )
        ],
        [sg.Button("Read"), sg.Button("Double"), sg.Button("Change Colors")],
        [sg.Text("Read = read which rows are selected")],
        [sg.Text("Double = double the amount of data in the table")],
        [sg.Text("Change Colors = Changes the colors of rows 8 and 9"), sg.Sizegrip()],
    ]
    return sg.Window("The Table Element", layout, resizable=True)
