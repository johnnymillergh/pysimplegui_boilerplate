from datetime import datetime

import PySimpleGUI as sg
from loguru import logger
from requests import request

from pysimplegui_boilerplate.__main__ import startup
from pysimplegui_boilerplate.configuration.apscheduler_configuration import scheduler


def led_indicator(key: str | None = None, radius: int = 30) -> sg.Graph:
    return sg.Graph(
        canvas_size=(radius, radius),
        graph_bottom_left=(-radius, -radius),
        graph_top_right=(radius, radius),
        pad=(0, 0),
        key=key,
    )


def set_led(window: sg.Window, key: str, color: str) -> None:
    graph: sg.Graph = window[key]
    graph.erase()
    graph.draw_circle((0, 0), 12, fill_color=color, line_color=color)


layout = [
    [sg.Text("Network Status Indicator", size=(20, 1))],
    [sg.Text("www.google.com"), led_indicator("_google_")],
    [sg.Text("www.bing2.com"), led_indicator("_bing2_")],
    [sg.Text("www.bing.com"), led_indicator("_bing_")],
    [sg.Exit()],
]

window = sg.Window(
    "Network Status Indicator",
    layout,
    default_element_size=(24, 1),
    auto_size_text=False,
    finalize=True,
)


def check_network_status(url: str, window: sg.Window, ui_key: str) -> None:
    try:
        response = request(method="GET", url=url, timeout=5)
    except Exception as e:
        logger.warning(f"{url} failed, {e}")
        set_led(window, ui_key, "red")
        return
    logger.info(f"{url}: {response.status_code}")
    if response.status_code in (range(200, 299)):
        set_led(window, ui_key, "green")
    if response.status_code in (range(300, 399)):
        set_led(window, ui_key, "yellow")
    if response.status_code in (range(400, 599)):
        set_led(window, ui_key, "red")


if __name__ == "__main__":
    startup()
    i = 0
    while True:  # Event Loop
        event, value = window.read(timeout=400)
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if value is None:
            break
        if i == 0:
            now = datetime.now()
            scheduler.add_job(
                func=check_network_status,
                trigger="interval",
                args=("https://www.google.com", window, "_google_"),
                seconds=15,
                next_run_time=now,
            )
            scheduler.add_job(
                func=check_network_status,
                trigger="interval",
                args=("https://www.bing2.com", window, "_bing2_"),
                seconds=15,
                next_run_time=now,
            )
            scheduler.add_job(
                func=check_network_status,
                trigger="interval",
                args=("https://www.bing.com", window, "_bing_"),
                seconds=15,
                next_run_time=now,
            )
            i += 1
    window.close()
