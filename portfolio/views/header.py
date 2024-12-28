import reflex as rx

from portfolio.components.heading import heading
from portfolio.components.media_header import media
from portfolio.data import Data
from portfolio.styles.styles import Size


def header(data: Data) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                src = data.avatar,
                size = Size.BIG.value
            ),
            rx.vstack(
                heading(data.name, True),
                heading(data.skill),
                rx.text(
                    rx.icon("map-pin"),
                    data.location,
                    display = "inherit"
                ),
                spacing = Size.SMALL.value,
            ),
            spacing = Size.DEFAULT.value,
            width = "100%",
        ),
        rx.mobile_only(
            rx.hstack(
                media(data.media),
                spacing = Size.SMALL.value,
                justify = "center"
            ),
            width = "100%"
        ),
        rx.tablet_and_desktop(
            media(data.media),
            spacing = Size.SMALL.value,
            width = "100%",
        ),
        spacing = Size.DEFAULT.value,
        align_items = "stretch",
    )
