import reflex as rx
from portfolio.components.media_footer import media
from portfolio.data import Media
from portfolio.styles.styles import Size


def footer(data: Media) -> rx.Component:
    return rx.vstack(
        rx.text("Get in touch  |   Made with ❤ by Walker"),
        media(data),
        spacing = Size.SMALL.value,
    )