import PySimpleGUI as sg
from loguru import logger

from pysimplegui_boilerplate.configuration.event_bus_configuration import event_bus
from pysimplegui_boilerplate.layout.view_video_game.view import create_window
from pysimplegui_boilerplate.repository.model.video_game import VideoGame


def main() -> None:
    cursor = VideoGame.select().order_by(VideoGame.id.desc()).execute()
    data = []
    for item in cursor:
        data.append(
            [
                item.title,
                item.handheld,
                item.max_players,
                item.multiplatform,
                item.online,
                item.genres,
                item.licensed,
                item.publishers,
                item.sequel,
                item.review_score,
                item.sales,
                item.used_price,
                item.console,
                item.rating,
                item.re_release,
                item.year,
            ]
        )
    window = create_window(data)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        logger.info(f"Emitting event: {event}, values: {values}, window: {window}")
        event_bus.emit(event, values, window)
