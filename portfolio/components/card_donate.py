import reflex as rx

from portfolio.data import Extra
from portfolio.styles.styles import Size, EmSize
from portfolio.styles.color import TextColor, Color
from portfolio.styles.styles import card_style, description_style, text_content_style


def card_donate(extra: Extra) -> rx.Component:
    return rx.card(
        rx.link(
            rx.vstack(
                rx.vstack(
                    rx.hstack(
                        rx.text.strong(
                            extra.title,
                            color = TextColor.PRIMARY.value,
                        ),
                    ),
                    rx.text(
                        extra.description,
                        color = TextColor.SECONDARY.value,
                        size = Size.SMALL.value,
                    ),
                    style = text_content_style,
                    align_items = "start",
                    width = "100%",
                    spacing = Size.SMALL.value,
                ),
                spacing = "0",
                align_items = "start",
                width = "100%",
            ),
            href = extra.url,
            _hover = {
                "text_decoration": "none",
            }
        ),
        style = card_style,
        width = "100%",
    )
